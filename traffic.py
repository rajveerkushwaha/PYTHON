import requests

# Function to get traffic information for a website
def get_traffic_info(website):
    url = f"https://blog.cyberswipe.in/category/blog/{website}"
    response = requests.get(url)
    return response.text

# Get traffic info for cyberswipe.in
traffic_info = get_traffic_info("blog.cyberswipe.in")
traffic_info[:1000]  # Displaying a snippet of the response text to understand its structure
