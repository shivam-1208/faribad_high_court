from flask import Flask, render_template, request
from scraper import fetch_case_data
from db import log_query

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        filing_year = request.form['filing_year']

        try:
            result, raw_html = fetch_case_data(case_type, case_number, filing_year)
            log_query(case_type, case_number, filing_year, raw_html)
            return render_template('result.html', result=result)
        except Exception as e:
            return render_template('index.html', error=str(e))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
