from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SelectPage:
    countrys_xpath="//input[@id='searchby-country']"
    courses_xpath="//input[@id='searchby-course']"
    coursetypes_xpath="//input[@id='searchby-course-specialization']"
    def __init__(self, driver):
        self.driver = driver

    def select_country(self,country):
        coun=self.driver.find_element(By.XPATH,self.countrys_xpath)
        clists=Select(coun)
        clists.select_by_visible_text(country)

    def select_course(self, course):
        cour = self.driver.find_element(By.XPATH, self.countrys_xpath)
        clists = Select(cour)
        clists.select_by_visible_text(course)

    def select_coursetype(self,ctype):
        court = self.driver.find_element(By.XPATH, self.countrys_xpath)
        clists = Select(court)
        clists.select_by_visible_text(ctype)