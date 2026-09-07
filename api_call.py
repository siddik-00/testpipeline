import requests
import json


def get_data(url, headers=None, params=None):
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Timeout Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    return None


def post_data(url, payload, headers=None):
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None


if __name__ == "__main__":
    # Example: a public API (JSONPlaceholder)
    url = "https://jsonplaceholder.typicode.com/posts/1"

    print("--- GET Request ---")
    data = get_data(url)
    if data:
        print(json.dumps(data, indent=2))

    print("\n--- POST Request ---")
    payload = {
        "title": "Sample Post",
        "body": "This is a sample body",
        "userId": 1,
    }
    post_url = "https://jsonplaceholder.typicode.com/posts"
    result = post_data(post_url, payload)
    if result:
        print(json.dumps(result, indent=2))
