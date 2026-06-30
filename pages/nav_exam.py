from selenium.webdriver import ActionChains
from selenium.webdriver.common import driver_finder
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Nav_exam:
    examnav_xpath="//a[@id='Exam']"
    eligibilty_xpath="//span[normalize-space()='Eligibility']"
    syllabus_xpath="//span[normalize-space()='Syllabus']"
    exampattern_xpath="//span[normalize-space()='Exam Pattern']"
    preparation_xpath="//span[normalize-space()='Preparation']"
    examfees_xpath="//span[normalize-space()='Exam Fees']"
    examdates_xpath="//span[normalize-space()='Exam Dates']"
    registration_xpath="//span[normalize-space()='Registration']"
    score_xpath="//span[normalize-space()='Score']"
    def __init__(self,driver):
        self.driver=driver

    def hovernav_exam(self):
        c = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.examnav_xpath)))
        act = ActionChains(self.driver)
        act.move_to_element(c).perform()

    def click_about(self,name):
        course=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='About {name}']")))
        course.click()

    def click_syllabus(self,syl):
        syllabus=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='{syl} Syllabus']")))
        syllabus.click()

    def click_exampattern(self,exampattern):
        ep=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[contains(text(),'{exampattern} Exam Pattern')]")))
        ep.click()

    def click_preparations(self,preparations):
        prep=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='{preparations} Preparations']")))
        prep.click()

    def click_registrations(self,registrations):
        register=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='{registrations} Registration']")))
        register.click()

    def click_ineligibility(self):
        el=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.eligibilty_xpath)))
        el.click()

    def click_insyllabus(self):
        syl=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.syllabus_xpath)))
        syl.click()

    def click_inexampattern(self):
        epp=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.exampattern_xpath)))
        epp.click()

    def click_inpreparation(self):
        pp=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.preparation_xpath)))
        pp.click()

    def click_inexamfees(self):
        ef=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.examfees_xpath)))
        ef.click()

    def click_inexamdates(self):
        ed=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.examdates_xpath)))
        ed.click()

    def click_inregister(self):
        cr=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.registration_xpath)))
        cr.click()

    def click_inscore(self):
        cs=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.score_xpath)))
        cs.click()

    def click_readingsection(self,read):
        rs=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='Reading section of {read}']")))
        rs.click()

    def click_writingsection(self,write):
        ws = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[normalize-space()='Writing section of {write}']")))
        ws.click()

    def click_listeningsection(self,listen):
        ls=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='Listening section of the {listen}']")))
        ls.click()

    def click_speakingsection(self,speak):
        ss=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='The speaking section of {speak}']")))
        ss.click()

    def click_dos(self,d):
        do=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[contains(text(),'Do’s and don’ts before and on the {d} test day')]")))
        do.click()

    def click_mistakes(self,mistake):
        mist=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[normalize-space()='Common mistakes made by {mistake} test takers']")))
        mist.click()

    def click_tips(self,tip):
        tips=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//a[@href='https://www.jeduka.com/exams/{tip}/guide/test-day']")))
        tips.click()