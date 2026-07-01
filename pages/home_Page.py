from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SelectPage:
    countrys_xpath="//select[@id='searchby-country']"
    courses_xpath="//select[@id='searchby-course']"
    coursetypes_xpath="//select[@id='searchby-course-specialization']"
    searchbtn_xpath="//button[normalize-space()='Search Now']"

    fiftycourse_xpath="//h3[normalize-space()='50']"
    twentysevcountries_xpath="//h3[normalize-space()='27000']"
    twentyfiveuni_xpath="//h3[normalize-space()='2500']"
    fivehundredarticles_xpath="//h3[normalize-space()='500']"

    decidetab_xpath="//a[@id='Decide-tab']"
    explorecountries_xpath="//a[normalize-space()='Explore Countries']"
    selectcourse_xpath="//a[@id='Select-tab']"
    explorecourses_xpath="//a[normalize-space()='Explore Top Courses']"
    preparedocuments_xpath="//a[@id='Prepare-tab']"
    applydocuments_xpath="//a[normalize-space()='Prepare to Apply']"
    apply_xpath="//a[@id='Apply-tab']"
    howtoapply_xpath="//a[normalize-space()='How to Apply']"

    viewallexams_xpath="// a[normalize-space() = 'View All Exams']"

# reachouttous section
    applyid_xpath = "//input[@id='name']"
    emailid_xpath = "//input[@id='email_address']"
    mobileid_xpath = "//input[@id='mobile_number']"
    country_xpath = "//select[@id='current_country']"
    state_xpath = "//select[@id='current_state']"
    city_xpath = "//select[@id='current_city']"
    subscribebtn_xpath = "//button[@id='newsletter_submit']"


    def __init__(self, driver):
        self.driver = driver

    def select_country(self,country,course,ctype):
        coun=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.countrys_xpath)))
        clists=Select(coun)
        clists.select_by_visible_text(country)

        cour = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.courses_xpath)))
        clists = Select(cour)
        clists.select_by_visible_text(course)

        court = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.coursetypes_xpath)))
        clists = Select(court)
        clists.select_by_visible_text(ctype)

        btn=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.searchbtn_xpath)))
        btn.click()

    def select_whyjeduka(self):
        fiftyc=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.fiftycourse_xpath)))
        fiftyc.click()
        self.driver.back()

        twentysevenc=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.twentysevcountries_xpath)))
        twentysevenc.click()
        self.driver.back()

        twentyfivec=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.twentyfiveuni_xpath)))
        twentyfivec.click()
        self.driver.back()

        fivehundreduni=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.fivehundredarticles_xpath)))
        fivehundreduni.click()
        self.driver.back()

# by default decide country is selected so for that
    def click_decidecountry(self):
        ec = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.explorecountries_xpath)))
        ec.click()

    def click_decidecountrynotselectedfirst(self):
        dc=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.decidetab_xpath)))
        dc.click()
        ec=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.explorecountries_xpath)))
        ec.click()

    def click_selectcourses(self):
        sc=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.selectcourse_xpath)))
        sc.click()
        tp=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.explorecourses_xpath)))
        tp.click()

    def click_preparedocuments(self):
        pd=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.preparedocuments_xpath)))
        pd.click()
        pa=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.applydocuments_xpath)))
        pa.click()

    def click_apply(self):
        ca=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.apply_xpath)))
        ca.click()
        ha=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.howtoapply_xpath)))
        ha.click()

    def click_browsebycountries(self,country):
        bbc=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,f"//h3[normalize-space()='{country}']")))
        bbc.click()

    def click_browsebycourse(self,course):
        bbco=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,f"//h3[normalize-space()='{course}']")))
        bbco.click()

    def click_studyabroadexams(self,examtype):
        sae=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,f"//a[@href='https://www.jeduka.com/exams/{examtype}']//i[@class='icofont-arrow-right']")))
        sae.click()

    def click_viewallexams(self):
        vae=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.viewallexams_xpath)))
        vae.click()

    def click_about(self, name):
        self.click_viewallexams()
        course = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[normalize-space()='About {name} Exam']")))
        course.click()

    def click_syllabus(self, syl):
        self.click_viewallexams()
        syllabus = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[normalize-space()='{syl} Syllabus']")))
        syllabus.click()

    def click_preparations(self, preparations):
        self.click_viewallexams()
        prep = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[normalize-space()='{preparations} Preparation']")))
        prep.click()

    def click_registrations(self, registrations):
        self.click_viewallexams()
        register = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[normalize-space()='{registrations} Registration']")))
        register.click()

    def click_adminandassistance(self,assistance):
        aaa=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//h4[normalize-space()='{assistance}']")))
        aaa.click()

    def click_applynow(self):
        an=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn-2 apply_btn']")))
        an.click()

    def registernow(self,fname,mobile,email,cctry,cstate,ccity,intake,pcountry,pcourse,cspecial,hlevel,work,exams,marks):
        self.click_applynow()
        full=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='name']")))
        full.send_keys(fname)

        m = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='mobile_number']")))
        m.send_keys(mobile)

        e = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='email_address']")))
        e.send_keys(email)

        cc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//select[@id='country']")))
        Select(cc).select_by_visible_text(cctry)

        cs = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//select[@id='state']")))
        Select(cs).select_by_visible_text(cstate)

        cct = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//select[@id='city']")))
        Select(cct).select_by_visible_text(ccity)

        si = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='intake']")))
        Select(si).select_by_visible_text(intake)

        pc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//select[@id='program_country']")))
        Select(pc).select_by_visible_text(pcountry)

        pco = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//select[@id='program']")))
        Select(pco).select_by_visible_text(pcourse)

        css = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//select[@id='program_type']")))
        Select(css).select_by_visible_text(cspecial)

        highlevel = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='edu_qualification']")))
        Select(highlevel).select_by_visible_text(hlevel)

        workexperience= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='work_experience']")))
        Select(workexperience).select_by_visible_text(work)

        exambtn=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,f"//label[normalize-space()='{exams}']")))
        exambtn.click()

        score=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//input[starts-with(@id,'exam_score_')]")))
        score.send_keys(marks)

        checkmark=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='checkmark']")))
        checkmark.click()

        submitbtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//button[@id='signup']")))
        submitbtn.click()

        hpbtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//a[@id='Continuetohomepage']")))
        hpbtn.click()

    def click_viewallarticles(self,country,title):
        varticles=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='view_all_btn']")))
        varticles.click()
        vspecificarticles=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,f"//a[href='https://www.jeduka.com/articles-updates/{country}/{title}']")))
        vspecificarticles.click()

    def reach_tous(self,fname,mobile,email,cctry,cstate,ccity):
        full = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.applyid_xpath)))
        full.send_keys(fname)

        m = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.mobileid_xpath)))
        m.send_keys(mobile)

        e = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.emailid_xpath)))
        e.send_keys(email)

        cc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.country_xpath)))
        Select(cc).select_by_visible_text(cctry)

        cs = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.state_xpath)))
        Select(cs).select_by_visible_text(cstate)

        cct = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.city_xpath)))
        Select(cct).select_by_visible_text(ccity)

        sbtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.subscribebtn_xpath)))
        sbtn.click()

        #
    # def select_course(self, course):
    #     cour = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.courses_xpath)))
    #     clists = Select(cour)
    #     clists.select_by_visible_text(course)

    # def select_coursetype(self,ctype):
    #     court = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,self.coursetypes_xpath)))
    #     clists = Select(court)
    #     clists.select_by_visible_text(ctype)

    # def clickSearchbtn(self):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.searchbtn_xpath))).click()

