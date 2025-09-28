import pytest_bdd
import pytest
import time
import os
from pytest_bdd import scenario, given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from page_objects.web_page import AccessWebPage 
import logging

logger = logging.getLogger(__name__)

feature_file = os.path.join(os.path.dirname(__file__), "../features/mortgage.feature")


@scenario(feature_file, "User make a valid mortgage offer")
def test_make_valid_offer():
    pass
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def web_page(driver):
    return AccessWebPage(driver)

@given("the user access the Clikalia webpage")
def access_webpage(web_page):
    web_page.open_webpage()
    time.sleep(5)


@when("the user start to search an apartment on Madrid")
def search_home(web_page):
    web_page.search_home("Madrid")


@then("the user select an apartment to make an offer")
def offer(web_page):
    web_page.user_make_offer("1.100.000", "Denise", "Troglio")


# Invalid scenario:

@scenario(feature_file, "User make an invalid mortgage offer")
def test_make_invalid_offer():
    pass
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def web_page(driver):
    return AccessWebPage(driver)

@given("the user select an apartment to make an invalid offer")
def offer(web_page):
    web_page.invalid_offer("900.000")