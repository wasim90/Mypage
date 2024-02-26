اینجاست README برای پروژه‌های Flask:

---

## Flask Projects README

### Project 1: Single Page Application

#### Description:
This project consists of a single HTML page (`page.html`) styled with CSS (`styles.css`). The page displays basic information about the owner and provides contact details. Additionally, there are two Python scripts (`mypage.py` and `pageprofile.py`) that use Flask to serve the HTML page.

#### Files:
1. **page.html**:
   - Description: HTML template for the single-page application.
   - Usage: Open this file in a web browser to view the page.

2. **styles.css**:
   - Description: CSS file containing styles for `page.html`.
   - Usage: This file is linked to `page.html` to style the content.

3. **mypage.py**:
   - Description: Python script using Flask to serve `page.html`.
   - Usage: Run this script using Python to start a Flask server serving the single-page application.

4. **pageprofile.py**:
   - Description: Python script using Flask to redirect to `/profile`, which serves `page.html`.
   - Usage: Run this script using Python to start a Flask server. Accessing the root URL (`/`) redirects to `/profile`, serving the single-page application.

#### How to Run:
1. Ensure you have Python installed on your system.
2. Install Flask if you haven't already (`pip install Flask`).
3. Run `mypage.py` or `pageprofile.py` using Python (`python mypage.py` or `python pageprofile.py`).
4. Open a web browser and navigate to `http://localhost:5000` to view the single-page application.

---

