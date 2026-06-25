from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Nav_Courses:
    coursenav_xpath="//a[@id='Courses']"
    def __init__(self, driver):
        self.driver = driver

    def hover_course(self):
        course=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.coursenav_xpath)))
        act=ActionChains(self.driver)
        act.move_to_element(course).perform()

    def select_course(self,c):
        sp_course=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='{c}']")))
        self.driver.execute_script("arguments[0].click()",sp_course)

    def select_viewall(self,faculty):
        view_all=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"// a[ @ href = 'https://www.jeduka.com/'{faculty}'-colleges-universities-abroad'][normalize - space() = 'View all']")))
        view_all.click()

    def view_courses(self,uni):
        viewc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"// a[ @ href='https://www.jeduka.com/usa/universities/'{uni}'#tabs_2']")))
        viewc.click()

    def apply_now(self,apply):
        applyc= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, f"// a[ @ href = 'https://www.jeduka.com/apply-now-'{apply}'']")))
        applyc.click()

    def click_next(self):
        nextbtn=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//li[@class='page-numbers-next']//a[@class='page-numbers']")))
        nextbtn.click()