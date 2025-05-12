import sqlite3
import pandas as pd

# Connect to your SQLite database
conn = sqlite3.connect('users.db')

# Show all tables
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Tables:", tables)

# View users
users_df = pd.read_sql_query("SELECT * FROM users;", conn)
print("\nUsers Table:")
print(users_df)

# View predictions
pred_df = pd.read_sql_query("SELECT * FROM predictions;", conn)
print("\nPredictions Table:")
print(pred_df)

conn.close()
