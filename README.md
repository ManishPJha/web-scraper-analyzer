# **Web Scraper and Data Analyzer**

This is a Python-based web scraping and data analysis application built with **Streamlit**. It allows users to scrape data from websites using sitemap URLs, export the scraped data to CSV or JSON, analyze the data, and reset the database.

---

## **Features**

1. **Scrape Data**:

   - Scrape data from a sitemap URL.
   - Save the scraped data to an SQLite database.

2. **Export Data**:

   - Export the scraped data to **CSV** or **JSON**.

3. **Analyze Data**:

   - Analyze the scraped data and visualize the number of pages per domain.

4. **Reset Database**:
   - Delete all scraped data from the database.

---

## **Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/ManishPJha/web-scraper-analyzer.git
   cd web-scraper-analyzer
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

---

## **Usage**

1. **Scrape Data**:

   - Enter a sitemap URL and specify the number of pages to scrape.
   - Click **Start Scraping** to begin the scraping process.

2. **Export Data**:

   - Choose the export format (**CSV** or **JSON**).
   - Click **Export Data** to save the scraped data to a file.

3. **Analyze Data**:

   - View a bar chart showing the number of pages per domain.

4. **Reset Database**:
   - Click **Reset Database** to delete all scraped data.

---

## **File Structure**

```
web-scraper-analyzer/
├── database.py          # Database operations
├── scraper.py           # Web scraping logic
├── exporter.py          # Data export logic
├── analyzer.py          # Data analysis logic
├── streamlit_app.py     # Main Streamlit app
├── requirements.txt     # List of dependencies
├── README.md            # Project documentation
```

---

## **Dependencies**

- `streamlit`
- `aiohttp`
- `beautifulsoup4`
- `fake-useragent`
- `pandas`
- `matplotlib`
- `sqlite3`
- `python-dotenv`

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## **Contributing**

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Author**

- **Manish Jha**
- GitHub: [ManishPJha](https://github.com/ManishPJha)
- Email: mjha205@rku.ac.in
