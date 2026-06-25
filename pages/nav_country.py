from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Nav_Country:
    countrynav_xpath="//a[normalize-space()='Country']"
    specificcost_xpath="//span[contains(text(),'Cost of Studying')]"
    specificuniversities_xpath="//span[contains(text(),'Universities')]"
    masters_xpaath="//span[contains(text(),'Master')]"
    scholarship_xpath="//span[contains(text(),'Scholarship')]"
    studentvisa_xpath = "//span[contains(text(),'Student Visa')]"
    intake_xpath="//span[contains(text(),'Intake')]"
    faq_xpath="//span[contains(text(),'FAQ -')]"

    def __init__(self,driver):
        self.driver = driver

    def click_country(self):
        c=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.countrynav_xpath)))
        act = ActionChains(self.driver)
        act.move_to_element(c).perform()

    def select_specificcountry(self,country):
        specific_country=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[contains(@class ,'dropdown-item')][normalize-space()={country}]")))
        specific_country.click()

    def selectcost(self):
        cost=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.specificcost_xpath)))
        cost.click()

    def select_universities(self):
        uni=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.specificuniversities_xpath)))
        uni.click()

    def select_masters(self):
        masters= WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.masters_xpaath)))
        masters.click()

    def select_studentvisa(self):
        svisa=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.studentvisa_xpath)))
        svisa.click()

    def select_scholarship(self):
        sch = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.scholarship_xpath)))
        sch.click()
        self.driver.back()

    def select_intake(self):
        intakes = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.intake_xpath)))
        intakes.click()

    def select_faq(self):
        faq = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.faq_xpath)))
        faq.click()



