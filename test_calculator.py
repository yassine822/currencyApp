import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def run_test():
    options = webdriver.ChromeOptions()
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("http://127.0.0.1:5000/calculator")
        wait.until(EC.presence_of_element_located((By.ID, "display")))

        def click_button_by_text(text, delay=1):
            btn = driver.find_element(By.XPATH, f"//button[normalize-space()='{text}']")
            btn.click()
            time.sleep(delay)

        def click_operator(icon_class, delay=1):
            btn = driver.find_element(By.XPATH, f"//button[.//i[contains(@class,'{icon_class}')]]")
            btn.click()
            time.sleep(delay)

        def run_case(sequence, description):
            """Run one calculation case (list of button presses)."""
            # clear first (if you have a C or AC button)
            try:
                clear_btn = driver.find_element(By.XPATH, "//button[normalize-space()='C']")
                clear_btn.click()
                time.sleep(1)
            except:
                pass

            print(f"\nRunning test: {description}")
            for step in sequence:
                step()
            time.sleep(1)

            # get result
            display_value = driver.find_element(By.ID, "display").get_attribute("value")
            print(f"Result = {display_value}")
            time.sleep(2)

        # === Test Cases ===
        cases = [
            (
                [
                    lambda: click_button_by_text("1"),
                    lambda: click_operator("fa-plus"),
                    lambda: click_button_by_text("2"),
                    lambda: click_button_by_text("="),
                ],
                "1 + 2"
            ),
            (
                [
                    lambda: click_button_by_text("9"),
                    lambda: click_operator("fa-minus"),
                    lambda: click_button_by_text("4"),
                    lambda: click_button_by_text("="),
                ],
                "9 - 4"
            ),
            (
                [
                    lambda: click_button_by_text("5"),
                    lambda: click_operator("fa-times"),
                    lambda: click_button_by_text("3"),
                    lambda: click_button_by_text("="),
                ],
                "5 × 3"
            ),
            (
                [
                    lambda: click_button_by_text("8"),
                    lambda: click_operator("fa-divide"),
                    lambda: click_button_by_text("2"),
                    lambda: click_button_by_text("="),
                ],
                "8 ÷ 2"
            ),
        ]

        for seq, desc in cases:
            run_case(seq, desc)

        print("\n✅ All calculator tests completed.")

        
        time.sleep(10)

    finally:
        driver.quit()


if __name__ == "__main__":
    run_test()

# tests/test_calculator.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def run_test():
    options = webdriver.ChromeOptions()
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("http://127.0.0.1:5000/calculator")
        wait.until(EC.presence_of_element_located((By.ID, "display")))

        def click_button_by_text(text, delay=1):
            btn = driver.find_element(By.XPATH, f"//button[normalize-space()='{text}']")
            btn.click()
            time.sleep(delay)

        def click_operator(icon_class, delay=1):
            btn = driver.find_element(By.XPATH, f"//button[.//i[contains(@class,'{icon_class}')]]")
            btn.click()
            time.sleep(delay)

        def run_case(sequence, description):
            """Run one calculation case (list of button presses)."""
            # clear first (if you have a C or AC button)
            try:
                clear_btn = driver.find_element(By.XPATH, "//button[normalize-space()='C']")
                clear_btn.click()
                time.sleep(1)
            except:
                pass

            print(f"\nRunning test: {description}")
            for step in sequence:
                step()
            time.sleep(1)

            # get result
            display_value = driver.find_element(By.ID, "display").get_attribute("value")
            print(f"Result = {display_value}")
            time.sleep(2)

        # === Test Cases ===
        cases = [
            (
                [
                    lambda: click_button_by_text("1"),
                    lambda: click_operator("fa-plus"),
                    lambda: click_button_by_text("2"),
                    lambda: click_button_by_text("="),
                ],
                "1 + 2"
            ),
            (
                [
                    lambda: click_button_by_text("9"),
                    lambda: click_operator("fa-minus"),
                    lambda: click_button_by_text("4"),
                    lambda: click_button_by_text("="),
                ],
                "9 - 4"
            ),
            (
                [
                    lambda: click_button_by_text("5"),
                    lambda: click_operator("fa-times"),
                    lambda: click_button_by_text("3"),
                    lambda: click_button_by_text("="),
                ],
                "5 × 3"
            ),
            (
                [
                    lambda: click_button_by_text("8"),
                    lambda: click_operator("fa-divide"),
                    lambda: click_button_by_text("2"),
                    lambda: click_button_by_text("="),
                ],
                "8 ÷ 2"
            ),
        ]

        for seq, desc in cases:
            run_case(seq, desc)

        print("\n✅ All calculator tests completed.")

        
        time.sleep(10)

    finally:
        driver.quit()


if __name__ == "__main__":
    run_test()

