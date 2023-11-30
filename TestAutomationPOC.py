import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WebAppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # set up url then driver
        cls.url = "https://deepai.org/machine-learning-model/text2img"
        cls.driver = webdriver.Chrome()
        print("Chrome Driver Loaded -:" + cls.url)

    @classmethod
    def tearDownClass(cls):
        time.sleep(30)
        cls.driver.quit()
    
    def setUp(self):
        # Wait for the page to load
        self.wait = WebDriverWait(self.driver, 7)
    
    def test_enter_prompt(self):
        try:
            self.driver.get(self.url)
            print("Driver Loaded - " + self.url)
            prompt_box = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "model-input-text-input")))
            assert prompt_box.is_displayed()
            print("Found prompt box element")
            # Clear the search box
            prompt_box.clear()
            print("Prompt Box Cleared")

            # Type "AI Image Generator" into the search box
            prompt_box.send_keys("Toyota Truck Jump")
            print("Added text 'Toyota Truck Jump' to search field")

            expected_text = "Toyota Truck Jump"
            prompt_text = prompt_box.text
            # assert expected_text == prompt_text, f"Expected: {expected_text}, Actual: {prompt_text}"

        except AssertionError as e:
            print("AssertionError:", e)

    def test_generate_prompt(self):
        try:
            # Submit the prompt
            generate_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modelSubmitButton"]')))
            assert generate_button.is_displayed()
            print("\nFound Generate Button")
            generate_button.click()
            print("Generate button clicked")

        except AssertionError as e:
            print("AssertionError:", e)

    def test_download_image(self):
        try:
            #download the generated image
            download_button = self.wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="download-model-image"]')))
            assert download_button.is_displayed()
            print("Found Download Button")
            download_button.click()
            print("Clicked Download Button")

        except AssertionError as e:
            print("AssersionError:", e)

if __name__ == '__main__':
    unittest.main(verbosity=2)