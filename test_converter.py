import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ConverterTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)  # Keep browser open
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://127.0.0.1:5000")  # Flask app URL
        self.driver.maximize_window()

    def test_conversion(self):
        driver = self.driver

        # Enter amount
        amount_input = driver.find_element(By.ID, "amount")
        amount_input.clear()
        amount_input.send_keys("100")

        # Select "From" currency
        from_currency = driver.find_element(By.ID, "from_currency")
        from_currency.send_keys("USD")

        # Select "To" currency
        to_currency = driver.find_element(By.ID, "to_currency")
        to_currency.send_keys("EUR")

        # Click Convert button (correct ID!)
        convert_button = driver.find_element(By.ID, "convert-btn")
        convert_button.click()

        # Wait until result shows up
        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        ).text

        print("✅ Conversion Result:", result)

        # Assert that result contains 'USD' or 'EUR'
        self.assertTrue("USD" in result or "EUR" in result)

        time.sleep(5)  # Keep browser open to view result

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
