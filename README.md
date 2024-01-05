# Playwright Python for RTCamp

This repository contains Playwright tests implemented in Python for sample Amazon related Test Cases

## Test Files

### 1. test_login_page.py
### 2. test_search_page.py
### 3. test_checkout_page.py
### 4. test_wishlist_page.py

#### Test Scenarios
- validating login
- adding product to cart and perform checkout action
- validating search result
- validate product wishlist functionality

## Prerequisites

- Python installed on your machine.
- Python pip installed on your machine.

## Running the Tests

1. Clone the repository and execution:
```bash
git clone <repository_url>

repository_url = https://github.com/robertdeocampojr/rtcamp-playwright

2. Navigate to the project directory:
cd <project_directory>

3. Install all dependencies:
pip install -r requirements.txt

4. Run the tests using pytest runner and marker. (all to run all tests, login to run only login test)
pytest -m all 
pytest -m login
pytest -m wishlist
pytest -m search
pytest -m checkout
```
2. To View Results: 
```bash
go to <project_directory>/report.html
```
3. Sample Video of execution: https://www.loom.com/share/73d0fcff827f43d596d6291ff974d33d


#### Note
- While executing the test you may or may not encounter a reCAPTCHA that's why there's a sleep on login for you to manually input the code