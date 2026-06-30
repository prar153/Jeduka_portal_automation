from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Nav_Article:
    examarticle_xpath="//a[@id='Articles']"
    fullnameid_xpath = "//div[@class='form-group']//input[@id='name']"
    emailid_xpath = "//div[@class='form-group']//input[@id='email_address']"
    mobileid_xpath = "//div[@class='form-group']//input[@id='mobile_number']"
    country_xpath = "//select[@id='country']"
    state_xpath = "//select[@id='state']"
    city_xpath = "//select[@id='city']"
    preferred_country_xpath = "//select[@id='program_country']"
    preferred_course_xpath = "//select[@id='program']"
    course_specialization_xpath = "//select[@id='program_type']"
    submitbtn_xpath = "//button[@id='signup']"
    homepage_xpath = "//a[@id='Continuetohomepage']"
    def __init__(self,driver):
        self.driver=driver

    def hovernav_article(self):
        c = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.examarticle_xpath)))
        act = ActionChains(self.driver)
        act.move_to_element(c).perform()

    def click_topreasons(self,country):
        tr=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='Top Reasons to Study in {country}']")))
        tr.click()

    def click_usatophundred(self):
        th=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Top 100 Ranking Universities in USA']")))
        th.click()

    def click_canadatoptwenty(self):
        tt=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Top 20 Ranking Universities in Canada']")))
        tt.click()

    def click_toprank(self,con):
        tr=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='Top Ranking Universities in {con}']")))
        tr.click()

    def click_stayback(self,ctry):
        sb=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='Stay back in {ctry}']")))
        sb.click()

    def click_howtoapplycanadaandswitzerland(self,cttry):
        hacs=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='How to Apply to {cttry} Universities?']")))
        hacs.click()

    def click_howtoapply(self,ctryy):
        ha=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='How to Apply to Universities in {ctryy}?']")))
        ha.click()

    def click_staybackusacanadaandfrance(self,c):
        sbcf=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='Study in {c} Without IELTS']")))
        sbcf.click()

    def click_staybackctry(self,ct):
        csb=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='Study in {ct} for FREE']")))
        csb.click()

    def afterapply(self,fname,email,mobile,ccountry,cstate,ccity,pcountry,pcourse,cspecial):
        full=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.fullnameid_xpath)))
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
        self.driver.execute_script("arguments[0].click();", sbtn)

        hpbtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.homepage_xpath)))
        hpbtn.click()




