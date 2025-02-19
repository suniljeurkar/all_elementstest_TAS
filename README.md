# Playwright Automation Test - Test Elements Page (Version 2) 💻🛠️

## 📈 Overview
This repository contains an updated version of the automated test suite built using **Python, Playwright, and Pytest**. The tests interact with various web elements on a sample testing website to demonstrate Playwright's capabilities for UI automation. This version includes improvements in test structure by utilizing **pytest fixtures**.

## 🌟 New in Version 2
- ✅ Implemented `@pytest.mark.usefixtures("browser_settings")` to handle browser setup using fixtures.
- ✅ Removed browser initialization from the `AllElements` class constructor.
- ✅ Passed `page`, `context`, and `browser` as parameters to the `AllElements` class.
- ✅ Simplified `test_runner` function.

## 🌟 Features
The test suite covers the following elements:
- 🔢 Text input fields
- 🔐 Password input fields
- 📝 Multi-line text areas
- 📅 Dropdown selection
- 🔘 Radio buttons
- 🟩 Checkboxes
- 💡 Spinner inputs
- 📂 File uploads
- 📆 Date pickers
- 📢 Popup handling
- 📃 New tab handling
- 💡 Submit button click and validation

## 🛠️ Prerequisites
Make sure you have the following installed:
- Python 3.x
- Playwright
- Pytest

## 👉 Installation
```bash
pip install pytest playwright
playwright install
```

## 💡 Running the Tests
To execute the test cases, run the following command:
```bash
pytest test_elements_v2.py
```

## 📐 Test Structure
- The `AllElements` class receives `page`, `context`, and `browser` objects through dependency injection.
- A `browser_settings` fixture is expected to provide these objects.
- Each test method creates an instance of the `AllElements` class and performs the interactions.
- The tests are marked with `@pytest.mark.regression` to categorize them.

## 🌐 Test Elements Site
The tests interact with a sample website hosted at:
https://testautomationsite.in/testelements.html

### ⚠️ Disclaimer
The above website is hosted solely for testing and learning purposes. There is no guarantee that the site will be available in the future. If the site becomes unavailable, the tests may fail.

## 📝 Notes
- The script is configured to run in non-headless mode for demonstration purposes.
- Several `time.sleep()` calls are included to handle timing issues, which can be replaced with more robust `wait_for` conditions if needed.
- The file upload section is commented out; you can modify the path according to your local file system if you wish to test file uploads.
- Using pytest fixtures helps in maintaining test modularity and better resource management.

## 📧 Contact
Feel free to reach out if you encounter any issues or need assistance!

