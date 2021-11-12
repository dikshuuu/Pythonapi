import pyodbc
from app import app

conn = pyodbc.Connection(
    "Driver = {SQL Sever Native Client 11.0};"
    "Server=.\SQLEXPRESS;"
    "Database=test;"
    "Trusted_Connection=yes;"
)