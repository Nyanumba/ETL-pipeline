import requests
import pandas 
import sqlalchemy

#http://api.coincap.io/v2/assets
#http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow

url = "http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"
header = {
    "Content-Type": "application/json",
    "Accept-Encoding": "deflate"
}
response = requests.get(url, headers = header)
print(response)

response_data = response.json()
#print(response_data)

df = pandas.json_normalize(response_data, 'items')
print(df)



