import os
import openai
import tweepy
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Set up OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up Twitter (X)
auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_API_KEY"),
    os.getenv("TWITTER_API_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_SECRET")
)
twitter_api = tweepy.API(auth)


# Generate Post Content
def generate_post(prompt="Write a short, catchy post about the impact of AI on daily life."):
    print("🧠 Generating post with OpenAI...")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.8,
    )
    content = response['choices'][0]['message']['content'].strip()
    print(f"✅ Post generated:\n{content}\n")
    return content
    

# Post to X
def post_to_x(content):
    try:
        twitter_api.update_status(content)
        print("✅ Successfully posted to X (Twitter)!")
    except Exception as e:
        print(f"❌ Failed to post: {e}")

# Main Agent
def main():
    
    prompt = "Write a 280-character post for X about how AI tools can save time for developers."
    post = generate_post(prompt)
    post_to_x(post)

if __name__ == "__main__":
    main()
