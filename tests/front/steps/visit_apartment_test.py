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

feature_file = os.path.join(os.path.dirname(__file__), "../features/visit_apartment.feature")


@scenario(feature_file, "User visits an apartment in Madrid")
def test_visit_apartment():
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


@when("the user start to search a apartment on Madrid")
def search_home(web_page):
    web_page.search_home("Madrid")


@then("the user select a apartment")
def select_apartment(web_page):
    web_page.select_a_home()


@given("the client schedules a visit")
def schedule_visit(web_page):
    web_page.visit("Denise", "Troglio")