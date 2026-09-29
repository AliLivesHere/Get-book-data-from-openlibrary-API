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

books = []
for book in data["docs"]:
    title = book.get("title", "N/A")
    author = ", ".join(book.get("author_name", ["N/A"]))
    publisher = ", ".join(book.get("publisher", ["N/A"]))
    language = book.get("language", ["N/A"])
    publish_year = book.get("first_publish_year", "N/A")
    books.append([title, author, publisher, language, publish_year])
    
filter = []
for book in books:
  year = book["publish_year"]
  if year and year > 2000:
    filter.append(book)
