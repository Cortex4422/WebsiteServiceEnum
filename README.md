# WebsiteServiceEnum
A Python Script to Enum hidden services on websites via post requests


Update the below sections in the script & retrieve your cookie / jwt token via BurpSuite or from within your browser prior to running.

# Base URL and endpoint
base_url = "<URL>"
​
# Headers
headers = {
    "Cookie": "jwt=<Cookie from BURPSuite>",
    "Content-Type": "application/json"
