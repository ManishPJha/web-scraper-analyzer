import csv
import json
from database import fetch_data


def export_to_csv():
    """Export data to a CSV file."""
    rows = fetch_data()
    with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "URL", "Title", "Content", "HTML"])  # Write header
        writer.writerows(rows)  # Write rows


def export_to_json():
    """Export data to a JSON file."""
    rows = fetch_data()
    data = []
    for row in rows:
        data.append(
            {
                "id": row[0],
                "url": row[1],
                "title": row[2],
                "content": row[3],
                "html": row[4],
            }
        )
    with open("scraped_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
