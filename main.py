# main.py
import datetime
import os
import sys

from openai import OpenAI


def run():
    now = datetime.datetime.now()
    print(f"Script execution started at: {now.strftime('%Y-%m-%d %H:%M:%S UTC')}")

    # Get API Key from Environment Variable
    api_key = os.getenv('GEMINI_API_KEY')

    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not found.")
        print("Make sure you have added the secret to your GitHub repository settings.")
        sys.exit(1)

    try:
        # Configure the OpenAI client to use Gemini's API
        client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

        # Define the prompt
        prompt = "Generate a short, optimistic, and fun daily horoscope for today. Keep it general, not tied to any specific zodiac sign. Maximum 3 sentences."
        print(f"\nUsing prompt: '{prompt}'")

        # Call the Gemini API using OpenAI's SDK
        print("Generating horoscope with Gemini...")
        response = client.chat.completions.create(
            model="gemini-2.0-flash",
            n=1,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        # Print the result
        print("\n--- Daily Horoscope ---")
        print(response.choices[0].message.content)
        print("-----------------------\n")

    except Exception as e:
        print(f"\nAn error occurred while interacting with the Gemini API: {e}")

    print(f"Script finished at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")


if __name__ == "__main__":
    run()
