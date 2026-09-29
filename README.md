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

-----------------------------------------------------------------------------------

# اطلاعات کتاب‌های Open Library

این یک پروژه کوچک پایتون است که من برای تمرین کار با APIها و کار با داده‌ها در پایتون ساخته‌ام.

این پروژه از API سایت Open Library برای دریافت اطلاعات کتاب‌ها استفاده می‌کند. بعد از دریافت داده‌ها، برنامه اطلاعات مورد نیاز را انتخاب می‌کند و آن‌ها را در یک فایل CSV ذخیره می‌کند.

## برنامه چه کاری انجام می‌دهد؟

این برنامه اطلاعات کتاب‌ها را از Open Library دریافت می‌کند، از جمله:

* عنوان
* نویسنده
* ناشر
* زبان
* سال اولین انتشار

بعد از دریافت اطلاعات کتاب‌ها، برنامه سال انتشار را بررسی می‌کند و فقط کتاب‌هایی را نگه می‌دارد که بعد از سال ۲۰۰۰ منتشر شده‌اند.

نتایج نهایی در فایلی به نام `books.csv` ذخیره می‌شوند.

## برنامه چگونه کار می‌کند؟

برنامه ابتدا با استفاده از کتابخانه `requests` یک درخواست به API سایت Open Library ارسال می‌کند.

سپس پاسخ را به صورت JSON دریافت می‌کند و اطلاعات کتاب‌ها را بررسی می‌کند. برای هر کتاب، اطلاعات مورد نیاز را دریافت کرده و آن‌ها را در یک لیست قرار می‌دهد.

بعد از آن، کتاب‌ها بر اساس سال انتشار فیلتر می‌شوند. در نهایت، داده‌های فیلترشده در یک فایل CSV نوشته می‌شوند.

## تکنولوژی‌های استفاده شده

این پروژه از موارد زیر استفاده می‌کند:

* Python
* Requests
* Open Library API
* CSV

## فایل‌های پروژه

`Main.py`
فایل اصلی پایتون است که اطلاعات را دریافت می‌کند، آن‌ها را فیلتر می‌کند و فایل CSV را ایجاد می‌کند.

`books.csv`
فایل خروجی است که اطلاعات کتاب‌ها بعد از فیلتر شدن در آن قرار می‌گیرد.

## اجرای پروژه

ابتدا کتابخانه requests را نصب کنید:

```bash
pip install requests
```

سپس فایل پایتون را اجرا کنید:

```bash
python Main.py
```

بعد از اجرای برنامه، فایل `books.csv` در پوشه پروژه ایجاد می‌شود.

## توضیح

این پروژه به عنوان یک پروژه تمرینی برای کار با APIها، فیلتر کردن داده‌ها و ذخیره داده‌ها در فایل CSV ساخته شده است.
