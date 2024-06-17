import requests
import pandas as pd

url = "https://football98.p.rapidapi.com/premierleague/fixtures"

header = {
    "X-RapidAPI-Host": "football98.p.rapidapi.com",
    "X-RapidAPI-Key": "a6850beb1dmsh61b46eda9a90372p1b193bjsn330f9dd99f27",  # Replace with your actual API key
    "Content-Type": "application/json",
    "Accept-Encoding": "deflate"
   
}
response = requests.get(url, headers = header)
print(response)

responseData = response.json()
print(responseData)

items = responseData.get('items', [])
final_data = pd.json_normalize(items)

print(final_data)