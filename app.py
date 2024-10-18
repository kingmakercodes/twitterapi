import tweepy

def create_api():

    # setting up Twitter API credentials

    consumer_key= '9Ad6e317EpV0D5VRIP3NnJDCE'
    consumer_secret= 'Qr1ugCdP1HNOIp8tYgcdThlt9I7tGyYuYOBjDuaIio1bXe5m5e'
    access_token= '1847303622918303744-w0v9642QfKoWV4PEKJna9cG1Z0NemA'
    access_token_secret= '9wdpvwZo7k7KMdSZKW8gzyjcEINXK92WBOV8WiBISXzzi'

    client= tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    return client


# Step 2: Create a function to tweet
def tweet_message(client, message="Tweet that idea into existence. Now!"):
    try:
        response = client.create_tweet(text=message)
        print(f"Tweet posted successfully! Tweet ID: {response.data['id']}")
    except Exception as e:
        print("Error while posting tweet", e)


if __name__ == "__main__":
    client = create_api()
    if client:
        tweet_message(client)