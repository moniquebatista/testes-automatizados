import time
import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class TestCT04:
    def test_ct04_realizar_compra(self):
        driver = conftest.driver
        login_page = LoginPage()

        login_page.fazer_login("standard_user", "secret_sauce")

        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[text() = 'Add to cart']").click()

        driver.find_element(By.XPATH, "//*[@class = 'shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        driver.find_element(By.ID, "continue-shopping").click()

        driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").click()
        driver.find_element(By.XPATH, "//*[text() = 'Add to cart']").click()

        driver.find_element(By.XPATH, "//*[@class = 'shopping_cart_link']").click()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()

        driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        driver.find_element(By.ID, "first-name").send_keys("Monique")
        driver.find_element(By.ID, "last-name").send_keys("Batista")
        driver.find_element(By.ID, "postal-code").send_keys("449000-000")
        time.sleep(5)
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()
        assert driver.find_element(By.XPATH, "//h2[@class='complete-header']").is_displayed()
        time.sleep(2)
