🧪 OrangeHRM Demo Test Automation (Playwright + Pytest)

This is a demo test automation project built with Playwright and Pytest for the OrangeHRM Demo Website  
.

It automates and validates the following features:  
✅ Valid Login  
❌ Invalid Login  
🗓️ Assign Leave  
💰 Submit Claim  
📋 Add Vacancy  
🗑️ Delete Vacancy  
🚪 Logout  

⚙️ Installation and Setup

Follow these steps line by line to set up the project:

1. **Clone the repository**
    ```bash
    git clone https://github.com/your-username/orangehrm-playwright-demo.git
2. **Go to the project directory**
    ```bash
    cd orangehrm-playwright-demo
3. **Create a virtual environment**
    ```bash
    python -m venv venv
4. **Activate the virtual environment**
    ```bash
    venv\Scripts\activate
5. **Install dependencies**
    ```bash
    pip install -r requirements.txt
6. **Install browsers for Playwright**
    ```bash
    playwright install
- **Run all tests:** 
    ```bash
    pytest
- **Run with visible browser window:** 
    ```bash
    pytest --headed
- **Run in slow motion (for debugging):** 
    ```bash
    pytest --headed --slowmo 500
- **Run a specific test file:**
    ```bash
    pytest tests/test_login.py
- **Run with detailed output:**
    ```bash
    pytest -v
- **Run tests by marker:** 
    ```bash 
    pytest -m regression
- **Run test with multiple markers:**
    ```bash
    pytest -m "login or vacancy"
- **Generate an HTML test report:**
    ```bash
    pytest --html=report.html --self-contained-html

**🏷️ Pytest Markers Configuration**   
**You can define markers in a pytest.ini file to organize your tests by category:**  
    [pytest]
    markers =  
        login: Tests related to Login functionality  
        leave: Tests related to Leave management  
        claim: Tests related to Claim submission  
        vacancy: Tests related to Job Vacancies  
        logout: Tests related to Logout functionality  


**📁 Recommended Project Structure**
    orangehrm-playwright-demo/  
    │  
    ├── tests/  
    │   ├── test_login.py  
    │   ├── test_leave.py  
    │   ├── test_claim.py  
    │   ├── test_vacancy.py  
    │   └── test_logout.py  
    │  
    ├── pages/  
    │   ├── base_page.py  
    │   ├── login_page.py  
    │   ├── dashboard_page.py  
    │   ├── leave_page.py  
    │   ├── claim_page.py  
    │   ├── vacancy_page.py  
    │   └── logout_page.py  
    │  
    ├── conftest.py  
    ├── pytest.ini  
    ├── requirements.txt  
    └── README.md  

**📦 Dependencies**  
    The following dependencies are required and installed automatically:  
    pytest  
    pytest-playwright  
    playwright  
    pytest-html  

**To export your current environment’s packages into a file:**
    
    pip freeze > requirements.txt

*** 💡 Tips ***  
        ✨ Always activate your virtual environment before running tests.
        👀 Use --headed to view browser execution.  
        🐢 Use --slowmo to slow down execution for debugging.  
        🏷️ Use pytest -m followed by a marker name to run specific test groups.  
        🔁 The OrangeHRM Demo site resets periodically — data is temporary.  


**👩‍💻 AUTHOR**  
        Gianna Pahuyo  
        Demo QA Automation Project using Playwright + Pytest  
        🔗 https://opensource-demo.orangehrmlive.com  

Thank you!
