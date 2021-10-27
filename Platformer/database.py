import pyodbc

connection_string = "driver={SQL SERVER}; server=.\\SQLEXPRESS; database=PygamePlatformer; trusted_connection=YES;"


def get_scoreboard():
    query = "SELECT TOP (10) *  FROM Users ORDER BY Seconds"
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data


def insert_user(username, coins, seconds, deaths):
    query = f"INSERT INTO Users (Username, Coins, Seconds, Deaths) VALUES ('{username}', {coins}, {seconds}, {deaths})"
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
