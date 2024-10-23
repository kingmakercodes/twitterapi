# information on this Twitter api is found in devjournal.txt
import tweepy


# Step 1: Define a function to create the api
def create_api():

    # setting up Twitter API credentials
    api_key= ''
    api_secret= ''
    access_token= ''
    access_token_secret= ''

    client= tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    return client


# Step 2: Create a function to tweet
def tweet_message(client, message='Have you ever tweeted something into existence?'):
    try:
        response = client.create_tweet(text=message)
        print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
    except Exception as e:
        print(f"Error while posting tweet, {e}")


# run the application
if __name__ == "__main__":
    client = create_api()
    if client:
        tweet_message(client)