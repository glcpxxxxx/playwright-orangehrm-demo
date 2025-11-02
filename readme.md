🧪 OrangeHRM Demo Test Automation (Playwright + Pytest)

This is a demo test automation project built with Playwright and Pytest for the OrangeHRM Demo Website (https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
).

It automates and validates the following features:
✅ Valid Login
❌ Invalid Login
🗓️ Assign Leave
💰 Submit Claim
📋 Add Vacancy
🗑️ Delete Vacancy
🚪 Logout

⚙️ INSTALLATION AND SETUP

Follow these steps line by line to set up the project:

1. Clone the repository
git clone https://github.com/your-username/orangehrm-playwright-demo.git

2. Go to the project directory
cd orangehrm-playwright-demo

3. Create a virtual environment
python -m venv venv

4. Activate the virtual environment
Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate

5. (Option A) Install dependencies manually
pip install pytest pytest-playwright playwright pytest-html

6. (Option B) Install dependencies from requirements.txt
pip install -r requirements.txt

7. Install browsers for Playwright
playwright install

After this setup, your environment is ready to run tests.

🧪 RUNNING TESTS

▶️ Run all tests
pytest

👀 Run with visible browser window
pytest --headed

🐢 Run in slow motion (for debugging)
pytest --headed --slowmo 500

🧾 Run a specific test file
pytest tests/test_login.py

🔍 Run with detailed output
pytest -v

🏷️ Run tests by marker
pytest -m login
pytest -m claim
pytest -m vacancy
pytest -m logout
pytest -m regression
pytest -m smoke

🏷️ Run tests by multiple markers
pytest -m "login or claim"

📊 Generate an HTML test report
pytest --html=report.html --self-contained-html

🏷️ PYTEST MARKERS CONFIGURATION

To organize tests by category, define markers in a pytest.ini file:

[pytest]
markers =
 login: Tests related to Login functionality
 leave: Tests related to Leave management
 claim: Tests related to Claim submission
 vacancy: Tests related to Job Vacancies
 logout: Tests related to Logout functionality

📁 PROJECT STRUCTURE

orangehrm-playwright-demo/
│
├── tests/
│ ├── test_login.py
│ ├── test_leave.py
│ ├── test_claim.py
│ ├── test_vacancy.py
│ └── test_logout.py
│
├── pages/
│ ├── base_page.py
│ ├── login_page.py
│ ├── dashboard_page.py
│ ├── leave_page.py
│ ├── claim_page.py
│ ├── vacancy_page.py
│ └── logout_page.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

📦 DEPENDENCIES

The following dependencies are required and installed automatically:

pytest

pytest-playwright

playwright

pytest-html

To export your current environment’s packages into a requirements file, run:
pip freeze > requirements.txt

💡 TIPS

✨ Always activate your virtual environment before running tests.
👀 Use --headed to view browser execution.
🐢 Use --slowmo to slow down execution for debugging.
🏷️ Use pytest -m with markers to selectively run test categories.
🔁 The OrangeHRM Demo site resets periodically — temporary data may disappear.

👩‍💻 AUTHOR

Gianna Pahuyo
Demo QA Automation Project using Playwright + Pytest
🔗 https://opensource-demo.orangehrmlive.com