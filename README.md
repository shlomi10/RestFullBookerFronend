
# Restful Booker Tests 🏨
[![Playwright](https://img.shields.io/badge/Playwright-1.52.0-green.svg?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-Test_Framework-green.svg?style=for-the-badge&logo=pytest)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-Reports-orange.svg?style=for-the-badge&logo=allure)](https://docs.qameta.io/allure/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg?style=for-the-badge&logo=docker)](https://docs.docker.com/compose/)
[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/shlomi10/pango/test.yml?label=CI%20Build&style=for-the-badge&logo=github-actions)](https://github.com/shlomi10/RestFullBookerFronend/actions)
[![Allure Report](https://img.shields.io/badge/Allure%20Report-View%20Live-purple?style=for-the-badge&logo=github)](https://shlomi10.github.io/RestFullBookerFronend/)

This project contains automated UI tests for the Restful Booker web application using Playwright with Python and pytest.

## Project Structure 📁
```
RestfullBookerFrontend/
├── pages/
│   ├── admin_page.py
│   ├── base_page.py
│   ├── edit_page_room.py
│   └── home_page.py
├── tests/
│   ├── base_class.py
│   ├── conftest.py
│   └── test_booker_webApp.py
├── utils/
│   └── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── ui_tests.yml
└── README.md
```

## Features ✨
- 🧩 Page Object Model for maintainable test logic
- 🎭 Playwright for fast browser automation
- 🧪 Pytest for test execution
- 📊 Allure for test reporting
- 📸 Screenshot capture on failure
- 🔍 Tracing support for failed tests
- 📝 Logging for step-level diagnostics
- 🐳 Full Docker support
- 🔄 CI/CD via GitHub Actions

## Prerequisites
- Python 3.12+
- pip (Python package installer)

## Installation
```bash
git clone https://github.com/shlomi10/restfulbooker-tests.git
cd restfulbooker-tests
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

## ⚙️ Configuration
Update `.env` inside the `utils/` folder:
```ini
BASE_URL=https://automationintesting.online
ADMIN_USER=admin
ADMIN_PW=password
```

## Running Tests 🚀
Run all tests:
```bash
pytest tests/
```

Run a specific test:
```bash
pytest tests/test_booker_webApp.py::TestRestfulBookerWebApp::test_add_room
```

Run with Allure reporting:
```bash
pytest tests/ --alluredir=./allure-results
```

## Running with Docker 🐳
Build and run all tests with Allure:
```bash
docker compose up --build
```

Run a specific test:
```bash
docker compose run --rm tests pytest tests/test_booker_webApp.py::TestRestfulBookerWebApp::test_add_room
```

## CI/CD Pipeline 🔄

This project uses GitHub Actions for continuous integration and deployment of test reports.

### GitHub Actions Workflow

The workflow automatically:
- Runs tests on pushes to the main branch and pull requests
- Executes tests in Docker containers
- Generates Allure reports
- Publishes reports to GitHub Pages

To manually trigger the workflow:
1. Go to the Actions tab in your GitHub repository
2. Select the "UI Tests" workflow
3. Click "Run workflow"

The test results are available on GitHub Pages after workflow completion.

## 🔎 View Allure Report

- 🔗 GitHub Pages (CI):
  [https://shlomi10.github.io/RestFullBookerFronend/](https://shlomi10.github.io/RestFullBookerFronend/)

- 🌐 Local (Docker):
  ```
  http://localhost:5050/projects/default/reports/latest/index.html
  ```

## 🧪 Test Cases
1. **Room Management**:
   * `test_add_room`: Add rooms with various options
   * `test_update_room`: Modify existing room data
   * `test_delete_room`: Remove a room

## Logging
Execution logs are saved in `ui_tests-logs/`. They are also attached in the Allure report.

## Debugging
* 📸 Screenshots: Saved in `screenshots/` on failure
* 📂 Traces: Saved in `trace/` and can be viewed with:
```bash
playwright show-trace trace/trace.zip
```

## Page Objects
* `BasePage`: Shared element actions
* `HomePage`: Home view operations
* `AdminPage`: Admin panel and room manager
* `EditRoomPage`: Room editing actions

## 👥Contributing
1. Fork the repo
2. Create your branch
3. Commit changes
4. Open a pull request

Follow Conventional Commits for commit messages.

## 📜 License
MIT License © 2025 Shlomi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Future Enhancements 🚀
* Performance Testing (Locust)
* Cross-browser support (Firefox, Safari)
* Mobile simulation testing
* Visual regression testing
* Data-driven testing
* Parallel test execution
* Security and accessibility checks
* Multi-environment support
