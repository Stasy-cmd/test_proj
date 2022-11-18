import csv
import os
from pathlib import Path
import psycopg2
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(".env" )

conn = psycopg2.connect(
    f"host={os.environ.get('HOST')} "
    f"dbname={os.environ.get('NAME')} "
    f"user={os.environ.get('USER')} "
    f"password={os.environ.get('PASSWORD')} "
    f"port={os.environ.get('PORT')} ")
cur = conn.cursor()
with open('library_writer.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        cur.execute(
        "INSERT INTO library_writer VALUES (%s, %s)",
        row
    )
conn.commit()
with open('library_book.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        cur.execute(
        "INSERT INTO library_book VALUES (%s, %s, %s)",
        row
    )
conn.commit()