from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import Cohere
from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware

import os

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, adjust as necessary
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Retrieve Cohere API key from environment variables for security
api_key = "MxvL30WkPvcCspBoqRuRPWDIZpBSgZdZwvkY4sqA"
if not api_key:
    raise ValueError("Cohere API key not found. Please set the COHERE_API_KEY environment variable.")

# Initialize Cohere LLM correctly
cohere_llm = Cohere(cohere_api_key=api_key)

# Define prompt template
outfit_prompt = PromptTemplate(
    input_variables=["weather", "occasion", "colors", "gender"],
    template="""Given the weather as {weather}, the occasion as {occasion}, the favorite colors {colors}, 
    and the gender as {gender}, suggest a fashionable outfit. 
    Include clothing and accessories, making sure the outfit is stylish and practical."""
)

# Setup LLMChain
outfit_chain = LLMChain(llm=cohere_llm, prompt=outfit_prompt)

# Define request model
class OutfitRequest(BaseModel):
    gender: str
    weather: str
    occasion: str
    colors: str

# Define API endpoint
@app.post("/recommend_outfit")
def get_outfit_recommendation(request: OutfitRequest):
    # Ensure gender input is valid
    if request.gender.lower() not in ["male", "female", "unisex"]:
        raise HTTPException(status_code=400, detail="Gender must be 'male', 'female', or 'unisex'.")

    try:
        # Generate outfit recommendation
        recommended_outfit = outfit_chain.run(
            weather=request.weather, 
            occasion=request.occasion, 
            colors=request.colors, 
            gender=request.gender
        )
        return {"recommended_outfit": recommended_outfit}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while generating the recommendation: {str(e)}")
