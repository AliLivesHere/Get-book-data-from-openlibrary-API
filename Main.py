import requests
import csv

api_url = "https://openlibrary.org/search.json"

parameters ={
  "q" : "*" , 
  "limit" : 50
}

response = requests.get(api_url, parameters = parameters)
response.raise_for_status()

data = response.json()