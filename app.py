# information on this Twitter api is found in devjournal.txt
import tweepy
import os
import openai
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# access the keys from environment variables
api_key= os.getenv('API_KEY')
api_secret= os.getenv('API_SECRET_KEY')
access_token= os.getenv('ACCESS_TOKEN_KEY')
access_token_secret= os.getenv('ACCESS_TOKEN_SECRET_KEY')
openai_api_key= os.getenv('OPENAI_API_KEY')

# Step 1: Define a function to create the api
def create_api():

    # setting up Twitter API credentials
    api_client= tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )
    return api_client


# Step 2: define a function to generate content using OpenAI's API
def generate_tweet():
    openai.api_key= openai_api_key

    # customise prompt to generate tweets about old money culture
    prompt= 'Generate a tweet about making positive affirmations, tweeting them on Twitter in hopes that it comes into existence.'

    try:
        response= openai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': 'You are a tweet generator for tweets that may come true.'},
                {'role': 'user', 'content': prompt}
            ],
            max_tokens=50
        )
        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        print(f'Error generating content: {e}')
        return 'Tweeting into existence: the act of manifesting your wildest dreams by affirming them on Twitter.'


# Step 3: define a function to tweet the generated message
def tweet_message(client):
    message= generate_tweet()
    try:
        response= client.create_tweet(text=message)
        print(f'Tweet posted successfully! Tweet ID: {response.data["id"]}')
    except Exception as e:
        print(f'Error while posting tweet: {e}')


# run the application
if __name__ == "__main__":
    client = create_api()
    if client:
        tweet_message(client)