# Code to load processed data into MySQL
import mysql.connector

def load_to_mysql(df, table_name, db_config):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(f"INSERT INTO {table_name} VALUES (%s, %s, %s)", tuple(row))
    conn.commit()
    cursor.close()
    conn.close()
