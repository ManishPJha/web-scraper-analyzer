import pandas as pd
import matplotlib.pyplot as plt
from database import fetch_data


def analyze_data():
    """Analyze the scraped data."""
    rows = fetch_data()

    if not rows:
        return "No data available for analysis."

    # Convert to a DataFrame
    df = pd.DataFrame(rows, columns=["ID", "URL", "Title", "Content", "HTML"])

    # Example: Count the number of pages per domain
    df["domain"] = df["URL"].apply(lambda x: x.split("/")[2])
    domain_counts = df["domain"].value_counts()

    # Plot the results
    fig, ax = plt.subplots(figsize=(10, 6))
    domain_counts.plot(kind="bar", ax=ax)
    plt.xlabel("Domain")
    plt.ylabel("Count")
    plt.tight_layout()

    return fig
