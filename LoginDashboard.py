import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class LoginPage:
    textbox_username_id="username"
    textbox_password_id="password"
    button_login_xpath="/html/body/div/div/div[2]/div/div/div/div/div[2]/form/div[3]/button"

    def __init__(self, driver):
        self.driver = driver

############################## LOGIN ############################################################

#set the username
    def setusername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

#set the password
    def setpassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

#click the login button
    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

############################## DASHBOARD ############################################################

#click decline card and click dashboard back
    def clickcard(self):
        dashbutton = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/h5')
        dashbutton.click()
        time.sleep(10)
        back = self.driver.find_element(By.XPATH, "/html/body/div/nav/div/div/ul[1]/li[1]/a")
        back.click()

#click the dropdown button and choose FiberCut to look the bar
    def selectbar(self):
        select = Select(self.driver.find_element_by_id("chart_type"))
        select.select_by_visible_text("Fiber Cut")

 #scroll down to the bottom of the page
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# click the dropdown button and choose unmatched to look the number of data
    def reportsource(self):
        select = Select(self.driver.find_element_by_id("source_type"))
        select.select_by_visible_text("Unmatched")

# click any data to look on the recent worklist
    def recentworklist(self):
        pressalert = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/ul/li[1]/div")
        pressalert.click()
        time.sleep(5)
        backbutton = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button/div/span")
        backbutton.click()

################################ MAP #############################################

# click the Map at Menu Bar
    def Map(self):
        menubarmap = self.driver.find_element(By.XPATH, "/html/body/div[1]/nav/div/div/ul[1]/li[2]/a")
        menubarmap.click()

# enter the address
    def searchaddress(self):
        search = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/input')
        search.send_keys('TM CYBERJAYA TOWER, Cyberjaya, Selangor, Malaysia')
        time.sleep(5)
        search.send_keys(Keys.ENTER)

# choose the cable type
    def cabletype(self):
        clickbutton = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/form/div/div[2]/div/label/input")
        clickbutton.click()
        time.sleep(5)
        clickbutton1 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/form/div/div[1]/div/label/input")
        clickbutton1.click()

################################ REPORT #############################################

# expand the bar
    def reports(self):
        expand = self.driver.find_element(By.XPATH,"/html/body/div[1]/nav/div/div/ul[1]/div[1]/li/a")
        expand.click()

# view the worklist
    def worklist(self):
        clickoption = self.driver.find_element(By.XPATH, "/html/body/div[1]/nav/div/div/ul[1]/div[1]/li/div/ul/li[3]/a")
        clickoption.click()
        time.sleep(15)
# choose any worklist
        choose = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/table/tbody/tr[7]")
        choose.click()

# edit the field team member
    def selectfieldteammember(self):
        edit = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[3]/i")
        edit.click()
        time.sleep(5)
#select any of the field team member name
        select1 = Select(self.driver.find_element_by_id("assignee_upd"))
        select1.select_by_visible_text("Shahrol Nizam bin Md Isa")
        time.sleep(5)
# enter the remark for the field team member
        remark = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/textarea')
        remark.send_keys('Test')
        time.sleep(5)
# save the changes
        save = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[3]/i[2]")
        save.click()
        time.sleep(5)
# back to the list of the worklist
        backbutton = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button/div/span")
        backbutton.click()
        time.sleep(5)
# click the download button to download the worklist document
        download = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/button[1]")
        download.click()

################################ MANAGEMENT #############################################

# expand the bar
    def management(self):
        expand1 = self.driver.find_element(By.XPATH,"/html/body/div[1]/nav/div/div/ul[1]/div[2]/li/a")
        expand1.click()

# view the user
    def user(self):
        clickoption1 = self.driver.find_element(By.XPATH, "/html/body/div[1]/nav/div/div/ul[1]/div[2]/li/div/ul/li[3]/a")
        clickoption1.click()

# enter the user role at the search box
    def searchuserrole(self):
        search1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/label/input')
        search1.send_keys('Regular')
        time.sleep(5)
# click the search button
        clicksearch = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/i")
        clicksearch.click()
        time.sleep(5)
# choose any of the user from the list
        choose1 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/table/tbody/tr[8]")
        choose1.click()
# scroll down to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
# click the back button
        backbutton = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/form/button/div/span")
        backbutton.click()

################################ MY PROFILE #############################################

# click my profile
    def profile(self):
        clickoption2 = self.driver.find_element(By.XPATH,"/html/body/div[1]/nav/div/div/ul[1]/li[3]/a")
        clickoption2.click()
        time.sleep(5)
# edit myprofile by clicking the button
        editprofile = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/button")
        editprofile.click()
        time.sleep(5)
# enter the changes need to be done
        enter = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div[3]/div[1]/form/div[1]/div[1]/div[2]/div/input')
        enter.send_keys("6")
        time.sleep(5)
# scroll down to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
# save the changes that had be done
        save = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[3]/div[2]/div[1]/button")
        save.click()
#back to the dashboard
        back = self.driver.find_element(By.XPATH, "/html/body/div/nav/div/div/ul[1]/li[1]/a")
        back.click()

################################ LOG OUT #############################################

# click the username at the top right to logout
    def logout(self):
        clickoption3 = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/nav/div/ul/li/a/div/div/span")
        clickoption3.click()
        time.sleep(5)
# click the logout button
        clicklogout = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/nav/div/ul/li/div/button[2]")
        clicklogout.click()