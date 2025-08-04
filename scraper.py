import requests
from bs4 import BeautifulSoup

def fetch_case_data(case_type, case_number, filing_year):
    url = "https://services.ecourts.gov.in/ecourtindia_v6/?p=casestatus/index&state_cd=06&dist_cd=6"

    payload = {
        'state_cd': '06',
        'dist_cd': '6',
        'court_code': '1',
        'court_complex_code': '1',
        'case_type': case_type,
        'case_no': case_number,
        'case_year': filing_year
    }

    session = requests.Session()
    response = session.post(url, data=payload)
    if not response.ok:
        raise Exception("Failed to fetch data from eCourts.")

    soup = BeautifulSoup(response.text, 'html.parser')
    parties = soup.find("td", text="Petitioner and Advocate")
    if not parties:
        raise Exception("Case not found or structure changed.")

    result = {
        "parties": parties.find_next("td").get_text(strip=True),
        "filing_date": "N/A",
        "next_hearing": "N/A",
        "latest_pdf": None
    }

    return result, response.text
