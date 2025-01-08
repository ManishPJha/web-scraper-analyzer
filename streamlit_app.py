import aiohttp
import streamlit as st
from database import init_db, save_to_db, reset_database
from scraper import scrape_website_from_sitemap
from exporter import export_to_csv, export_to_json
from analyzer import analyze_data
import asyncio

# Initialize the database
init_db()


# Streamlit UI
def main():
    st.title("Web Scraper and Data Analyzer")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    options = ["Scrape Data", "Export Data", "Analyze Data", "Reset Database"]
    choice = st.sidebar.selectbox("Choose an option", options)

    if choice == "Scrape Data":
        st.header("Scrape Data from Sitemap")
        sitemap_url = st.text_input("Enter sitemap URL:")
        limit = st.number_input(
            "Enter the number of pages to scrape (0 for all):", min_value=0
        )

        if st.button("Start Scraping"):
            if not sitemap_url:
                st.error("Please enter a sitemap URL.")
            else:
                with st.spinner("Scraping in progress..."):

                    async def run_scraping():
                        async with aiohttp.ClientSession() as session:
                            data = await scrape_website_from_sitemap(
                                session, sitemap_url, limit
                            )
                            save_to_db(data)
                            st.success(
                                f"Scraping completed. {len(data)} pages saved to database."
                            )

                    asyncio.run(run_scraping())

    elif choice == "Export Data":
        st.header("Export Data")
        export_format = st.radio("Choose export format:", ("CSV", "JSON"))

        if st.button("Export Data"):
            if export_format == "CSV":
                export_to_csv()
                st.success("Data exported to scraped_data.csv")
            elif export_format == "JSON":
                export_to_json()
                st.success("Data exported to scraped_data.json")

    elif choice == "Analyze Data":
        st.header("Analyze Scraped Data")
        result = analyze_data()
        if isinstance(result, str):
            st.warning(result)
        else:
            st.pyplot(result)

    elif choice == "Reset Database":
        st.header("Reset Database")
        if st.button("Reset Database"):
            reset_database()
            st.success("All scraped data has been deleted from the database.")


# Run the Streamlit app
if __name__ == "__main__":
    main()
