# import allure
# # from helper_module.screenshot_engine.javascript_executor import *
# # from helper_module.screenshot_engine.image_processor import ImageProcessor
# from time import sleep
#
# from conftest import driver
#
#
# class ScreenshotHelper(driver):
#     DEFAULT_WIDTH = 1920
#     DEFAULT_HEIGHT = 1080
#
#     def check_by_screenshot(self, driver):
#         sleep(0.5)
#         page_height = driver.execute_script('return document.body.parentNode.scrollHeight')
#         driver.set_window_size(self.DEFAULT_WIDTH, page_height)
#         sleep(1)
#         screenshot_driver_bytes = driver.get_screenshot_as_png()
#
#         image_prod = self.load_image_from_bytes(screenshot_driver_bytes)
#         image_beta = self.load_image_from_bytes(screenshot_driver_bytes)
#         allure.attach(self.image_to_bytes(image_beta), 'stage', allure.attachment_type.PNG)
#
