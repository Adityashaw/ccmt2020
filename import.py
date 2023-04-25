" inserts data from book.csv to book db in postgres "
import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

c = 0
total = 0

f = open("books.csv")
reader = csv.reader(f)
next(reader)  # Skip header row
for isbn, title, author, year in reader:
    db.execute("INSERT INTO book (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
            {"isbn": isbn, "title": title, "author": author, "year": year})
    c = c + 1
    total = total + 1
    print(total)
    if c == 100:  # commit after 100 inserts
        db.commit()
        c = 0
db.commit()  # commit rest
