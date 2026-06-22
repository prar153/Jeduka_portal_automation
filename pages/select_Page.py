from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SelectPage:
    countrys_xpath="//select[@id='searchby-country']"
    courses_xpath="//select[@id='searchby-course']"
    coursetypes_xpath="//select[@id='searchby-course-specialization']"
    searchbtn_xpath="//button[normalize-space()='Search Now']"
    def __init__(self, driver):
        self.driver = driver

    def select_country(self,country):
        coun=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.countrys_xpath)))
        clists=Select(coun)
        clists.select_by_visible_text(country)

    def select_course(self, course):
        cour = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.courses_xpath)))
        clists = Select(cour)
        clists.select_by_visible_text(course)

    def select_coursetype(self,ctype):
        court = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.coursetypes_xpath)))
        clists = Select(court)
        clists.select_by_visible_text(ctype)

    def clickSearchbtn(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.searchbtn_xpath))).click()