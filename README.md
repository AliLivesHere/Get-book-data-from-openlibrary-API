# Get-book-data-from-openlibrary-API
A Python project for getting book information from the Open Library API and saving filtered results in a CSV file.
# Open Library Book Data

This is a small Python project that I made to practice working with APIs and handling data in Python.

The project uses the Open Library API to get information about books. After getting the data, the program selects the information I need and saves it in a CSV file.

## What the program does

The program gets information about books from Open Library, including:

* Title
* Author
* Publisher
* Language
* First publish year

After getting the book data, the program checks the publish year and keeps only the books that were published after 2000.

The final results are saved in a file called `books.csv`.

## How it works

The program first sends a request to the Open Library API using the `requests` library.

Then it gets the response as JSON and goes through the book data. For each book, it gets the information that is needed and puts it into a list.

After that, the books are filtered based on their publish year. Finally, the filtered data is written to a CSV file.

## Technologies

This project uses:

* Python
* Requests
* Open Library API
* CSV

## Project Files

`Main.py`
The main Python file that gets the data, filters it, and creates the CSV file.

`books.csv`
The output file containing the book information after filtering.

## Running the Project

First, install the requests library:

```bash
pip install requests
```

Then run the Python file:

```bash
python Main.py
```

After running the program, the `books.csv` file will be created in the project folder.

## Note

This project was made as a practice project for working with APIs, filtering data, and saving data into CSV files.
