## 🎭 Playwright Python Test Automation Framework

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/) [![Playwright](https://img.shields.io/badge/Playwright-1.57-green.svg)](https://playwright.dev/python/) [![pytest](https://img.shields.io/badge/pytest-Framework-orange.svg)](https://pytest.org/) [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern, production-ready test automation framework built with Playwright for Python and pytest, implementing industry best practices including the Page Object Model (POM) design pattern, data-driven testing with Faker, pytest-bdd for behavior-driven development, and robust reporting capabilities.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Architecture](#️-architecture)
- [Technology Stack](#️-technology-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Running Tests](#-running-tests)
- [Reports and Logging](#-reports-and-logging)
- [Configuration](#️-configuration)
- [Best Practices Implemented](#-best-practices-implemented)
- [Contributing](#-contributing)

---

## 🎯 Overview

This framework demonstrates a scalable and maintainable approach to modern web application test automation using Playwright. It showcases professional testing practices suitable for enterprise-level applications, featuring modular design, reusable components, comprehensive test coverage, and support for multiple browsers.

**Learning Source:** Based on "Playwright with Python" concepts and best practices from test automation courses.

---

## ✨ Key Features

### Core Capabilities

- ✅ **Page Object Model (POM)**: Clean separation of test logic and page elements
- ✅ **Playwright Automation**: Fast, reliable, modern browser automation
- ✅ **Data-Driven Testing**: Parameterized tests with Faker for realistic data generation
- ✅ **BDD Support**: Behavior-driven development with pytest-bdd
- ✅ **Multi-Browser Support**: Chrome, Firefox, and Webkit compatibility
- ✅ **Cross-Platform**: Works on Windows, macOS, and Linux
- ✅ **HTML Reports**: Beautiful, detailed test execution reports (pytest-html)
- ✅ **Parallel Execution**: Distributed testing with pytest-xdist
- ✅ **API Testing**: Integrated API testing capabilities
- ✅ **Async Support**: Tests can use async/await patterns

### Advanced Features

- 🔧 Pytest fixtures for setup and teardown
- 🔧 Custom utilities and helper methods
- 🔧 Command-line arguments for flexible test execution
- 🔧 Environment variable management with python-dotenv
- 🔧 Polish locale support with Faker for test data
- 🔧 Integration-ready for CI/CD pipelines (GitHub Actions, Jenkins, etc.)
- 🔧 Security-focused credential management

---

## 🏗️ Architecture

The framework follows the **Page Object Model (POM)** design pattern, which provides:

```
┌─────────────────┐
│   Test Cases    │  ← High-level test scenarios
└────────┬────────┘
         │
    ┌────▼─────┐
    │   Page   │  ← Page Object classes
    │  Objects │
    └────┬─────┘
         │
    ┌────▼─────┐
    │Resources │  ← Utilities & base classes
    │& Fixtures│
    └────┬─────┘
         │
    ┌────▼─────┐
    │Playwright│  ← Browser automation engine
    └──────────┘
```

**Benefits:**
- Reduced code duplication
- Easy maintenance when UI changes
- Improved test readability
- Better separation of concerns
- Reusable components

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Programming Language** | Python 3.8+ |
| **Web Automation** | Playwright 1.57 |
| **Testing Framework** | Pytest 9.x |
| **BDD Framework** | pytest-bdd 8.1 |
| **Reporting** | pytest-html 4.2 |
| **Test Data** | Faker 40.x |
| **Parallel Testing** | pytest-xdist 3.8 |
| **Environment Management** | python-dotenv 1.2 |
| **Browsers** | Chromium, Firefox, Webkit |

---

## 📁 Project Structure

```
playwright-python/
│
├── playwright/                    # Main test directory
│   ├── page_objects/             # Page Object Model classes
│   │   ├── login.py              # Login page elements and methods
│   │   ├── login_practice.py     # Practice login page
│   │   ├── shop.py               # Shop page elements and methods
│   │   ├── dashboard.py          # Dashboard page
│   │   ├── orders.py             # Orders page
│   │   └── order_details.py      # Order details page
│   │
│   ├── resources/                # Helper utilities
│   │   ├── api_base.py           # API testing base class
│   │   └── generic.py            # Generic helper methods
│   │
│   ├── features/                 # BDD feature files
│   │
│   ├── utils/                    # Utility files
│   │
│   ├── test_playwright_basics.py      # Basic Playwright tests
│   ├── test_playwright_basics_2.py    # Additional basic tests
│   ├── test_playwright_pom.py         # POM pattern tests
│   ├── test_shop_pom.py               # E2E shop tests with POM
│   ├── test_playwright_async.py       # Async tests
│   ├── test_pytest-bdd-example.py     # BDD examples
│   └── test_codegen.py                # Codegen examples
│
├── tests/                        # Fast unit tests for page objects (no browser/network)
│   ├── test_login_and_shop_pom_unit.py
│   ├── test_orders_flow_pom_unit.py
│   └── test_streamlit_page_objects_unit.py
│
├── assets/                       # Report assets
│   └── style.css                # Custom report styling
│
├── conftest.py                   # Pytest configurations and fixtures
├── pytest.ini                    # Pytest configuration file
├── requirements.txt              # Project dependencies
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
└── README.md                    # Project documentation
```

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/apadlo/playwright-python.git
   cd playwright-python
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install
   ```

5. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env file with your actual credentials
   ```

   Fill in your credentials:
   ```
   USER_PASSWORD=your_user_password_here
   TEST_EMAIL=your_email@example.com
   PRACTICE_USERNAME=rahulshettyacademy
   PRACTICE_PASSWORD=your_practice_password_here
   PRACTICE_WRONG_PASSWORD=test_wrong_password
   ```

6. **Important**: Never commit the `.env` file to version control. It is already listed in `.gitignore`.

---

## 🚀 Usage

### Basic Test Execution

Run all tests with default browser (Chrome):
```bash
pytest
```

### Run Specific Test File
```bash
pytest playwright/test_shop_pom.py
```

### Run Tests in a Directory
```bash
pytest playwright/
```

### Run with Specific Browser
```bash
pytest --browser_name chrome
pytest --browser_name firefox
```

### Generate HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run with Verbose Output
```bash
pytest -v -s
```

### Run Specific Test Method
```bash
pytest playwright/test_shop_pom.py::TestShopPOM::test_product_present_after_login -v
```

### Run Tests by Markers
```bash
pytest -m sanity
pytest -m regression
pytest -m smoke
pytest -m unit
pytest -m "e2e and not streamlit"
pytest -m streamlit
```

### Run Tests in Parallel
```bash
pytest -n auto  # Use all available CPU cores
pytest -n 4     # Use 4 workers
```

### Run in Headless Mode
Headless is now default. For local headed runs use:
```bash
pytest --headed
```

### Jenkins / CI command examples
Use these commands in Jenkins pipeline stages (Linux shell):

```bash
# 1) Install dependencies
python -m pip install -r requirements.txt
playwright install --with-deps chromium

# 2) Fast gate (recommended PR check)
pytest -m "unit or smoke" -q

# 3) Expanded browser suite (excluding Streamlit external checks)
pytest -m "e2e and not streamlit" --browser_name=chrome -q

# 4) Streamlit checks (optional, external dependency)
pytest -m streamlit --browser_name=chrome -q

# 5) Full suite
pytest -m "unit or smoke or e2e or streamlit or sanity or regression" --browser_name=chrome
```

---

## 🧪 Running Tests

### End-to-End Test Example

The framework includes complete e-commerce workflow tests:

```python
# test_shop_pom.py demonstrates:
- Navigate to login page
- Enter credentials and authenticate
- Wait for shop page to load
- Verify product presence
- Complete purchase flow
```

### Data-Driven Test Example

Tests with realistic data generation using Faker:

```python
# Using polish_user_factory fixture:
- Generate Polish user data (names, emails, PESEL, etc.)
- Parameterized testing with multiple data sets
- Form validation with realistic data
- Dynamic data handling for each test run
```

### BDD Test Example

Behavior-driven tests with pytest-bdd:

```python
# test_pytest-bdd-example.py demonstrates:
- Feature file structure
- Given/When/Then steps
- Scenario outlines
- Reusable step definitions
```

### Async Test Example

Asynchronous test execution:

```python
# test_playwright_async.py demonstrates:
- Async/await patterns
- Concurrent operations
- Performance optimization
```

---

## 📊 Reports and Logging

### HTML Reports

Generate detailed HTML reports:
```bash
pytest --html=reports/report.html --self-contained-html
```

**Features:**
- Test execution summary
- Pass/Fail status with percentages
- Execution time for each test
- Screenshots for failed tests (when configured)
- Detailed error messages and stack traces
- Custom styling from `assets/style.css`

### Metadata

Add test metadata for better reporting:
```bash
pytest --html=reports/report.html --metadata "Tester" "Your Name" --metadata "Environment" "Production"
```

### Console Output

View detailed output during test execution:
```bash
pytest -v -s  # Verbose with stdout/stderr
```

---

## ⚙️ Configuration

### Browser Configuration

Modify `conftest.py` to customize browser settings:

```python
@pytest.fixture
def browser_instance(playwright, request):
    browser_name = request.config.getoption("--browser_name")
    match browser_name:
        case "chrome":
            browser = playwright.chromium.launch(headless=False)
        case "firefox":
            browser = playwright.firefox.launch(headless=False)
        case _:
            raise ValueError(f"Unsupported browser: {browser_name}")
    # Customize context options, viewport, etc.
```

### Pytest Configuration

Update `pytest.ini` to configure test execution:

```ini
[pytest]
markers =
    sanity: Quick smoke tests
    regression: Full regression suite
    api: API tests
    ui: UI tests
```

### Test Data Configuration

Use Faker for dynamic test data or create custom factories in `conftest.py`:

```python
@pytest.fixture()
def polish_user_factory():
    # Generate realistic Polish user data
    # Includes names, emails, PESEL, phone numbers, etc.
```

### Environment Variables

Manage sensitive data securely with `.env` file:
- Never commit credentials to source control
- Use `.env.example` as a template
- Load with `python-dotenv` in test files

---

## 🎓 Best Practices Implemented

### Design Patterns

- ✅ **Page Object Model**: Separation of test logic and UI interactions
- ✅ **DRY Principle**: Reusable utilities and base classes
- ✅ **Single Responsibility**: Each page object manages only its page
- ✅ **Factory Pattern**: Test data generation with Faker

### Test Design

- ✅ **Independent Tests**: No test dependencies or shared state
- ✅ **Descriptive Names**: Clear, self-documenting test method naming
- ✅ **Setup/Teardown**: Proper resource management with fixtures
- ✅ **Auto-Waiting**: Playwright's built-in smart waiting mechanisms
- ✅ **Selectors**: Robust, maintainable locator strategies

### Code Quality

- ✅ **Modular Structure**: Easy to navigate and maintain
- ✅ **Type Hints**: Python type annotations for better IDE support
- ✅ **Docstrings**: Comprehensive documentation for classes and methods
- ✅ **Error Handling**: Robust exception management
- ✅ **Security First**: Credentials managed via environment variables

### Testing Approach

- ✅ **Fast Execution**: Playwright's modern architecture
- ✅ **Reliable Tests**: Auto-waiting and retry mechanisms
- ✅ **Cross-Browser**: Test on Chromium, Firefox, and Webkit
- ✅ **Parallel Testing**: Scale with pytest-xdist
- ✅ **CI/CD Ready**: Easy integration with GitHub Actions, Jenkins, etc.

### Security

- ✅ **Environment Variables**: Sensitive data never hardcoded
- ✅ **Gitignore Rules**: Prevent accidental credential commits
- ✅ **Example Templates**: `.env.example` for guidance
- ✅ **Documentation**: Clear security guidelines

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Guidelines

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards

- Follow PEP 8 style guide
- Add docstrings to new classes and methods
- Write tests for new features
- Update documentation as needed

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **Playwright Team**: For the amazing browser automation tool
- **Pytest Community**: For the excellent testing framework
- **Rahul Shetty Academy**: For providing practice websites and learning resources

---

## 📧 Contact

For questions, suggestions, or issues, please open an issue on GitHub.

**Repository**: [https://github.com/apadlo/playwright-python](https://github.com/apadlo/playwright-python)

---

Made with ❤️ by [apadlo](https://github.com/apadlo)
