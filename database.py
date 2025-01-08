import sqlite3

# Database setup
DATABASE_NAME = "scraped_data.db"


def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS scraped_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            title TEXT,
            content TEXT,
            html TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def save_to_db(data):
    """Save scraped data to the database."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.executemany(
        """
        INSERT INTO scraped_data (url, title, content, html)
        VALUES (?, ?, ?, ?)
        """,
        [(item["url"], item["title"], item["content"], item["html"]) for item in data],
    )
    conn.commit()
    conn.close()


def reset_database():
    """Reset the database by deleting all scraped data."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM scraped_data")
    conn.commit()
    cursor.close()
    conn.close()


def fetch_data():
    """Fetch all data from the database."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scraped_data")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
