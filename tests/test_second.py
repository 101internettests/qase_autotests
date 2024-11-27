import os
import uuid
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages.base_page import BasePage

HEADLESS = os.getenv("HEADLESS") == "True"


class TestsSeoCheck(BasePage):
    READ_MORE_BUTTON_FIRST = (
        By.XPATH, "(//button[@class='Button_button__wliYd Button_secondary__LGYa1 Button_sm__VkQR3'])[1]"
    )
    SCROLL_ONE = (
        By.XPATH, "//h2[text()='Провайдеры домашнего интернета в Санкт-Петербурге']"
    )

    def _click_if_exists(self):
        try:
            self.scroll()
            # Wait for the button to be clickable after scrolling
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TestsSeoCheck.READ_MORE_BUTTON_FIRST)
            )
            button.click()
            print("Clicked on the button")
        except NoSuchElementException:
            print("Button not found")
        except TimeoutException:
            print("Waiting for the button to become clickable timed out")
        except Exception as e:
            print(f"Error clicking the button: {e}")

    def scroll(self):
        try:
            time.sleep(2)  # Allow some time for the page to load initially
            scroll_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(TestsSeoCheck.SCROLL_ONE)
            )

            # Scroll into view using JavaScript
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
                                       scroll_element)
            print("Scrolled to the element")

            # Optionally, wait a moment to ensure scrolling completes
            time.sleep(1)

        except TimeoutException:
            print("Timed out waiting for the scroll target element to become visible")
        except Exception as e:
            print(f"Error scrolling to element: {e}")


class TestSearChrome:
    def test_check_search_chrome(self, driver):
        if HEADLESS:
            driver.set_window_size(1920, 1080)
        else:
            driver.maximize_window()

        urls = [
            "https://piter-online.net/"
        ]
        names = [
            "Главная"
        ]

        for screen, name in zip(urls, names):
            try:
                uuid4 = uuid.uuid4()
                tags = TestsSeoCheck(driver, screen)

                tags._click_if_exists()

                driver.get(screen)
                time.sleep(2)
                driver.execute_cdp_cmd('Page.enable', {})
                driver.execute_cdp_cmd('Page.setDeviceMetricsOverride', {
                    'width': 1920,
                    'height': 6000,
                    'deviceScaleFactor': 1,
                    'mobile': False,
                    'fitWindow': False
                })

                time.sleep(1)
                screenshot_path = f'C:/Users/Katerina/Desktop/screens/{name}.png'
                driver.save_screenshot(screenshot_path)
                print(f"Скриншот сохранен: {screenshot_path}")

            except Exception as e:
                print(f"Ошибка при работе с {screen}: {e}")