import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup Chrome driver once
        options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_homepage_title(self):
        """Check homepage loads and title is correct"""
        self.driver.get("http://127.0.0.1:5000/")
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertIn("Currency Converter", self.driver.page_source)

    def test_calculator_page(self):
        """Test a simple calculation 1 + 2"""
        self.driver.get("http://127.0.0.1:5000/calculator")
        self.wait.until(EC.presence_of_element_located((By.ID, "display")))

        # Click 1
        self.driver.find_element(By.XPATH, "//button[normalize-space()='1']").click()
        # Click +
        self.driver.find_element(By.XPATH, "//button[i[contains(@class,'fa-plus')]]").click()
        # Click 2
        self.driver.find_element(By.XPATH, "//button[normalize-space()='2']").click()
        # Click =
        self.driver.find_element(By.XPATH, "//button[normalize-space()='=']").click()

        time.sleep(1)
        result = self.driver.find_element(By.ID, "display").get_attribute("value")
        self.assertEqual(result, "3")

if __name__ == "__main__":
    unittest.main()


#how are u i m yuubi 