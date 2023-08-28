from selenium import webdriver
import time
import unittest

from selenium.webdriver.common.by import By


class TestWebsite(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.jules.app")

    def tearDown(self):
        self.driver.quit()

    def test_title(self):
        self.assertEqual(self.driver.title, "Jules")

    def test_main_page(self):
        self.driver.get("http://jules.app/sign-in")
        time.sleep(3)
        self.assertEqual(self.driver.current_url, "https://jules.app/sign-in")

    def test_navigation(self):
        self.driver.get("http://www.jules.app")
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/form/div/div[4]/a').click()
        self.assertEqual(self.driver.current_url, "https://jules.app/sign-up")
        self.driver.quit()

    def test_log_in(self):
        self.driver.get("http://www.jules.app")
        time.sleep(3)
        email_input = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/form/div/div[1]/div/div/input')
        pass_input = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/form/div/div[2]/div/div/input')
        email_input.send_keys("johndoe@example.com")
        time.sleep(3)
        pass_input.send_keys("123456789")
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/form/div/div[3]/button/span[1]').click()
        time.sleep(3)
        self.driver.quit()

    def test_sign_up(self):

        self.driver.maximize_window()
        self.driver.get("http://www.jules.app")
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/form/div/div[4]/a').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[2]/div/div[3]/label/span[1]/span/input').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[2]/div/div[5]/button/span[1]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input').send_keys("Alexandru")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#root > div > div.css-p0w51b > div.css-13k67qp > div > div:nth-child(4) > button > span.MuiButton-label').click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#root > div > div.css-p0w51b > div.css-13k67qp > div > div.css-wbkzs1 > div > div > input').send_keys("Bogoros")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#root > div > div.css-p0w51b > div.css-13k67qp > div > div:nth-child(4) > button > span.MuiButton-label').click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#root > div > div.css-p0w51b > div.css-13k67qp > div > div.css-wbkzs1 > div > div > input').send_keys("Manescu_Andreea@yahoo.com")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#root > div > div.css-p0w51b > div.css-13k67qp > div > div:nth-child(4) > button > span.MuiButton-label').click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#root > div > div.css-p0w51b > div.css-13k67qp > div > div:nth-child(2) > div > div > input').send_keys("Examen12345!")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#root > div > div.css-p0w51b > div.css-13k67qp > div > div:nth-child(10) > button > span.MuiButton-label').click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#root > div > div.css-p0w51b > div.css-13k67qp > div > div.css-wbkzs1 > div > div > input').send_keys("Examen12345!")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'#root > div > div.css-p0w51b > div.css-13k67qp > div > div:nth-child(4) > button > span.MuiButton-label').click()
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
