from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture
def setUp():
    global driver, name, year, director, distributor, producer
    name = input("Enter Movie Name: ")
    year = input("Enter Year: ")
    director = input("Enter Director Name: ")
    distributor = input("Enter Distributor Name: ")
    producer = input("Enter Producer Name: ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()


def test_movieform(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    time.sleep(1)
    driver.find_element_by_name("mname").send_keys(name)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(year)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(director)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(distributor)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(producer)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[3]").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()