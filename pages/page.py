import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.some_locator import SeoTextLocator
from pages.base_page import BasePage


class TestsSeoCheck(BasePage):
    def click_if_exists_first_seo(self):
        try:
            self.element_is_visible(SeoTextLocator.READ_MORE_BUTTON_FIRST).click()
            print(f"Кликнули на кнопку")
        except NoSuchElementException:
            print(f"Кнопка не найдена")

    def click_if_exists_second_seo(self):
        try:
            self.element_is_visible(SeoTextLocator.READ_MORE_BUTTON_SECOND).click()
            print(f"Кликнули на кнопку")
        except NoSuchElementException:
            print(f"Кнопка не найдена")

    def click_if_exists_third_seo(self, count):
        try:
            # Find all elements that match the FAQ_READ locator
            elements = self.driver.find_elements(*SeoTextLocator.FAQ_READ)

            # Check if the count is within the range of available elements
            if 0 <= count < len(elements):
                elements[count].click()  # Click the specified element
                print(f"Кликнули на кнопку #{count + 1}")  # Log the click attempt
            else:
                print(f"Индекс {count} выходит за пределы доступных элементов. Доступные: {len(elements)}.")

        except NoSuchElementException:
            print("Кнопка не найдена.")
        except ElementClickInterceptedException:
            print("Не удалось кликнуть на кнопку, элемент перекрыт.")
        except Exception as e:
            print(f"Ошибка при клике на кнопку: {e}")

    def scroll(self):
        try:
            time.sleep(3)  # Give extra time for the page to load
            scroll_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(SeoTextLocator.SCROLL_ONE)
            )

            # Ensure the element is within view
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
            time.sleep(1)  # Allow time for scroll to complete
            print("Scrolled to the element")

        except TimeoutException:
            print("Timed out waiting for the scroll target element to become visible")
        except Exception as e:
            print(f"Error scrolling to element: {e}")

    def scroll_second(self):
        try:
            time.sleep(3)  # Give extra time for the page to load
            scroll_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(SeoTextLocator.SCROLL_TWO)
            )

            # Ensure the element is within view
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
            time.sleep(1)  # Allow time for scroll to complete
            print("Scrolled to the element")

        except TimeoutException:
            print("Timed out waiting for the scroll target element to become visible")
        except Exception as e:
            print(f"Error scrolling to element: {e}")

    def scroll_third(self):
        try:
            time.sleep(3)  # Give extra time for the page to load
            scroll_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(SeoTextLocator.SCROLL_THREE)
            )

            # Ensure the element is within view
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
            time.sleep(1)  # Allow time for scroll to complete
            print("Scrolled to the element")

        except TimeoutException:
            print("Timed out waiting for the scroll target element to become visible")
        except Exception as e:
            print(f"Error scrolling to element: {e}")

    def scroll_four(self):
        try:
            time.sleep(3)  # Give extra time for the page to load
            scroll_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(SeoTextLocator.SCROLL_FOUR)
            )

            # Ensure the element is within view
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
            time.sleep(1)  # Allow time for scroll to complete
            print("Scrolled to the element")

        except TimeoutException:
            print("Timed out waiting for the scroll target element to become visible")
        except Exception as e:
            print(f"Error scrolling to element: {e}")

    def scroll_five(self):
        try:
            time.sleep(3)  # Give extra time for the page to load
            scroll_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(SeoTextLocator.SCROLL_FIVE)
            )

            # Ensure the element is within view
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
            time.sleep(1)  # Allow time for scroll to complete
            print("Scrolled to the element")

        except TimeoutException:
            print("Timed out waiting for the scroll target element to become visible")
        except Exception as e:
            print(f"Error scrolling to element: {e}")
