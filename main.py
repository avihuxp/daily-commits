# main.py
import datetime


def run():
    now = datetime.datetime.now()
    print(f"Script executed at: {now}")

    # --- ADD YOUR SCRIPT LOGIC HERE ---
    # Example: You could read data, process it, call an API, etc.
    print("Doing the main task...")
    # Example accessing an environment variable (if you set one up later)
    # my_api_key = os.getenv('MY_API_KEY')
    # if my_api_key:
    #     print("API Key found (partially hidden):", my_api_key[:4] + "...")
    # else:
    #     print("API Key environment variable not found.")
    # --- END OF YOUR SCRIPT LOGIC ---

    print("Script finished.")


if __name__ == "__main__":
    run()
