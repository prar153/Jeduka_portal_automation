from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Nav_Courses:
    coursenav_xpath="//a[@id='Courses']"
    applyid_xpath="//input[@id='name']"
    emailid_xpath="//input[@id='email_address']"
    mobileid_xpath="//input[@id='mobile_number']"
    country_xpath="//select[@id='country']"
    state_xpath="//select[@id='state']"
    city_xpath="//select[@id='city']"
    preferred_country_xpath="//select[@id='program_country']"
    preferred_course_xpath="//select[@id='program']"
    course_specialization_xpath="//select[@id='program_type']"
    submitbtn_xpath="//button[@id='signup']"
    homepage_xpath="//a[@id='Continuetohomepage']"
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
        view_all=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"// a[ @ href = 'https://www.jeduka.com/{faculty}-colleges-universities-abroad'][normalize-space() = 'View all']")))
        view_all.click()

    def view_courses(self,uni):
        viewc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"// a[ @ href='https://www.jeduka.com/usa/universities/{uni}#tabs_2']")))
        viewc.click()

    def apply_now(self,apply):
        applyc= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, f"// a[ @ href = 'https://www.jeduka.com/apply-now-{apply}']")))
        applyc.click()

    def afterapply(self,fname,email,mobile,ccountry,cstate,ccity,pcountry,pcourse,cspecial):
        full=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.applyid_xpath)))
        full.send_keys(fname)

        e=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.emailid_xpath)))
        e.send_keys(email)

        m=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.mobileid_xpath)))
        m.send_keys(mobile)

        cc=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.country_xpath)))
        Select(cc).select_by_visible_text(ccountry)

        cs=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.state_xpath)))
        Select(cs).select_by_visible_text(cstate)

        cct=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.city_xpath)))
        Select(cct).select_by_visible_text(ccity)

        pc=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.preferred_country_xpath)))
        Select(pc).select_by_visible_text(pcountry)

        pco=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.preferred_course_xpath)))
        Select(pco).select_by_visible_text(pcourse)

        css=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.course_specialization_xpath)))
        Select(css).select_by_visible_text(cspecial)

        sbtn=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.submitbtn_xpath)))
        sbtn.click()

        hpbtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.homepage_xpath)))
        hpbtn.click()

    def click_next(self):
        nextbtn=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//li[@class='page-numbers-next']//a[@class='page-numbers']")))
        nextbtn.click()