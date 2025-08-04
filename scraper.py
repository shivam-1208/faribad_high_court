from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 👁️ Show browser
        page = browser.new_page()
        page.goto("https://faridabad.dcourts.gov.in/case-status-search-by-case-type/")

        # Fill out form fields
        page.select_option("select[name='court_complex_code']", "1")  # Example: Court Complex
        page.select_option("select[name='case_type']", "CP")          # Example: Case Type
        page.select_option("select[name='case_status']", "Pending")  # Status
        page.fill("input[name='case_year']", "2022")                 # Year

        # 🔔 Pause for manual CAPTCHA entry
        input("➡️ Please fill in the CAPTCHA in browser and click 'Search'. Then press ENTER here to continue...")

        # Wait for table to load
        page.wait_for_selector("table")  # Adjust if needed

        # Get and parse HTML
        html = page.content()
        soup = BeautifulSoup(html, "html.parser")
        results = soup.find("table")

        if results:
            print("\n✅ Results Table Found:")
            print(results.get_text())
        else:
            print("❌ No results found or table not located.")

        browser.close()

if __name__ == "__main__":
    run()

