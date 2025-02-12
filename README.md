# Outfit Recommendation API

This is a FastAPI-based application that provides outfit recommendations based on weather, occasion, favorite colors, and gender. It uses the Cohere language model to generate stylish and practical outfit suggestions.

## Features

- **Outfit Recommendations**: Get personalized outfit suggestions based on user inputs.
- **Customizable Inputs**: Specify weather, occasion, favorite colors, and gender for tailored recommendations.
- **FastAPI Backend**: Built with FastAPI for high performance and easy integration.
- **CORS Support**: Configured to allow cross-origin requests for frontend integration.

## Prerequisites

Before running the application, ensure you have the following:
- Python 3.8 or higher
- A Cohere API key (set as an environment variable or hardcoded in the script)
- Required Python packages (listed in requirements.txt)

## Usage

You can use any API client (like Postman or curl) to interact with the API. Below is an example using curl:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/recommend-outfit' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "weather": "sunny",
  "occasion": "casual",
  "favorite_colors": ["blue", "white"],
  "gender": "female"
}'
