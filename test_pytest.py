import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

def setup_function():
    global driver

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get('https://alnafi.com/sign-in')

def teardown_function():
    driver.quit()


@pytest.mark.parametrize("username, passwd", [("test_user", 'Test_pass'), ('test_user2', 'Test_pass2'), ('Test3', 'Test345')])
def test_login(username, passwd):
    print("Logging in Alnafi dashboard")
    driver.find_element(By.ID, 'Username/ Email').send_keys(username)
    driver.find_element(By.ID, 'Password').send_keys(passwd)