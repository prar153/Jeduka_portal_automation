from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Nav_Jedukazone:
    jedukazone_xpath="//a[@id='JedukaZone']"
    events_xpath="//a[normalize-space()='Events']"
    cv_xpath="//a[normalize-space()='CV']"
    studentvisa_xpath="//a[normalize-space()='Student Visa Process']"
    aboutus_xpath="//a[@class='dropdown-item'][normalize-space()='About Us']"
    askquestion_xpath="//a[normalize-space()='Ask a question']"
    chat_xpath="//a[normalize-space()='Chat with Jeduka Expert']"
    contactus_xpath="//a[contains(@class,'dropdown-item')][normalize-space()='Contact Us']"
    viewall_xpath="//a[contains(@href,'https://www.jeduka.com/education-loan')][normalize-space()='View all']"
# afterapply xpath
    fullname_xpath = "//div[@class='form-group']//input[@id='name']"
    email_xpath = "//div[@class='form-group']//input[@id='email_address']"
    mobile_xpath = "//div[@class='form-group']//input[@id='mobile_number']"
    country_xpath = "//select[@id='country']"
    state_xpath = "//select[@id='state']"
    city_xpath = "//select[@id='city']"
    preferred_country_xpath = "//select[@id='program_country']"
    preferred_course_xpath = "//select[@id='program']"
    course_specialization_xpath = "//select[@id='program_type']"
    submittbtn_xpath = "//button[@id='signup']"
    homepage_xpath = "//a[@id='Continuetohomepage']"

# contact xpath
    cfullname_xpath = "//input[@id='name']"
    cemail_xpath ="//input[@id='email_address']"
    cmobile_xpath = "//input[@id='mobile_number']"
    ccountry_xpath = "//select[@id='country']"
    cstate_xpath = "//select[@id='state']"
    ccity_xpath = "//select[@id='city']"
    cpreferred_country_xpath = "//select[@id='program_country']"
    cpreferred_course_xpath = "//select[@id='program']"
    ccourse_specialization_xpath = "//select[@id='program_type']"
    csubmittbtn_xpath = "//button[@id='signup']"
    chomepage_xpath = "//a[@id='Continuetohomepage']"

    def __init__(self,driver):
        self.driver = driver

    def hovernav_jedukazone(self):
        c = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.jedukazone_xpath)))
        act = ActionChains(self.driver)
        act.move_to_element(c).perform()

    def click_loaneduaction(self,country):
        loan=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='Education loan for {country}']")))
        loan.click()

    def click_tips(self,course):
        tips=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='Tips to write SOP for {course}']")))
        tips.click()

    def click_LOR(self,level):
        study=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='LOR for {level}']")))
        study.click()

    def click_events(self):
        ev=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.events_xpath)))
        ev.click()

    def click_cv(self):
        cv=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.cv_xpath)))
        cv.click()

    def click_studentvisa(self):
        sv=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.studentvisa_xpath)))
        sv.click()

    def click_about(self):
        ca=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.aboutus_xpath)))
        ca.click()

    def click_chat(self):
        cc=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.chat_xpath)))
        cc.click()

    def click_askaques(self):
        caq=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.askquestion_xpath)))
        caq.click()

    def click_contactus(self):
        cu=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.contactus_xpath)))
        cu.click()

    def click_viewall(self):
        va=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.viewall_xpath)))

    def afterapply(self, fname, email, mobile, ccountry, cstate, ccity, pcountry, pcourse, cspecial):
        full = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.fullname_xpath)))
        full.send_keys(fname)

        e = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_xpath)))
        e.send_keys(email)

        m = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.mobile_xpath)))
        m.send_keys(mobile)

        cc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.country_xpath)))
        Select(cc).select_by_visible_text(ccountry)

        cs = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.state_xpath)))
        Select(cs).select_by_visible_text(cstate)

        cct = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.city_xpath)))
        Select(cct).select_by_visible_text(ccity)

        pc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.preferred_country_xpath)))
        Select(pc).select_by_visible_text(pcountry)

        pco = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.preferred_course_xpath)))
        Select(pco).select_by_visible_text(pcourse)

        css = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.course_specialization_xpath)))
        Select(css).select_by_visible_text(cspecial)

        sbtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.submittbtn_xpath)))
        self.driver.execute_script("arguments[0].click();", sbtn)

        hpbtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.homepage_xpath)))
        hpbtn.click()

    def contactus(self, fname, email, mobile, ccountry, cstate, ccity, pcountry, pcourse, cspecial):
        full = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cfullname_xpath)))
        full.send_keys(fname)

        e = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cemail_xpath)))
        e.send_keys(email)

        m = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cmobile_xpath)))
        m.send_keys(mobile)

        cc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.ccountry_xpath)))
        Select(cc).select_by_visible_text(ccountry)

        cs = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cstate_xpath)))
        Select(cs).select_by_visible_text(cstate)

        cct = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.ccity_xpath)))
        Select(cct).select_by_visible_text(ccity)

        pc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cpreferred_country_xpath)))
        Select(pc).select_by_visible_text(pcountry)

        pco = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cpreferred_course_xpath)))
        Select(pco).select_by_visible_text(pcourse)

        css = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ccourse_specialization_xpath)))
        Select(css).select_by_visible_text(cspecial)

        sbtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.csubmittbtn_xpath)))
        self.driver.execute_script("arguments[0].click();", sbtn)

        hpbtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.chomepage_xpath)))
        hpbtn.click()
