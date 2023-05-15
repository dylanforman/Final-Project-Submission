import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from djangoProject.symptom import Symptom


class FormSubmissionTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")

    def test(self):

        self.driver.get("http://localhost:8000")

        textarea = self.driver.find_element(By.NAME, "symptoms")

        textarea.send_keys("Test data")
        start_time = time.time()
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "#symptom-form button[type='submit']")
        submit_button.click()

        time.sleep(2)
        end_time = time.time() - start_time
        print(f"Time taken: {end_time} seconds")
        self.assertIn("get_diagnosis", self.driver.current_url)

    def tearDown(self):
        # Close the browser
        self.driver.quit()

class FormValidationTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")

    def test(self):

        self.driver.get("http://localhost:8000")
        current_url = self.driver.current_url

        submit_button = self.driver.find_element(By.CSS_SELECTOR, "#symptom-form button[type='submit']")
        submit_button.click()


        self.assertEqual(self.driver.current_url, current_url)

    def tearDown(self):
        # Close the browser
        self.driver.quit()
#
# class FormDataHandling(TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
#
#     def test(self):
#
#         self.driver.get("http://localhost:8000")
#
#         textarea = self.driver.find_element(By.NAME, "symptoms")
#         textarea.send_keys("Test data")
#
#         submit_button = self.driver.find_element(By.CSS_SELECTOR, "#symptom-form button[type='submit']")
#         submit_button.click()
#
#         result = self.symptom.get_symptoms(self, "Test data")
#         self.assertIn("get_diagnosis", self.driver.current_url)
#
#     def tearDown(self):
#         # Close the browser
#         self.driver.quit()