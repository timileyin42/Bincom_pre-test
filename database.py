import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Function to save color frequencies to PostgreSQL
def save_to_db(color_counter):
    # Get the DATABASE_URI from environment variables
    DATABASE_URI = os.getenv("DATABASE_URI")

    # Establish connection using the connection string
    conn = psycopg2.connect(DATABASE_URI)

    # Perform database operations
    cur = conn.cursor()

    # Create table if it doesn't exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS color_frequencies (
            color VARCHAR(20),
            frequency INT
        );
    """)

    # Insert color frequencies into the database
    for color, freq in color_counter.items():
        cur.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s);", (color, freq))

    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

