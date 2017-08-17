import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class WebsiteTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

        # navigate to my website: https://moat.com/ 
        self.browser.get('https://moat.com/')

        #1. I decided to create a search related test case to check if data can be inputed in the text field and to check the search response time.
    def testNumber1(self):
        #searchfield
        searchfield = self.browser.find_element_by_id("pro-landing-search-box").send_keys("moat")
        #searchfield return
        searchfieldreturn = self.browser.find_element_by_id("pro-landing-search-box").send_keys(Keys.RETURN)

        #2. The reason why I created a sign up related test case was to check the behavior of the form by adding random data to the text fields. In addition, assuring that the sign up button is working.
    def testNumber2(self):

    	#signupbutton
    	signupclick = self.browser.find_element_by_link_text("Sign Up").click()
    	#firstnameinput
    	firstnameinput = self.browser.find_element_by_css_selector("input.field-input-2").send_keys("Alvin")
    	#lastnameinput
    	lastnameinput = self.browser.find_element_by_xpath("//div[@class='field-right']/input").send_keys("Lawson")
    	#emailaddressinput
    	emailaddressinput = self.browser.find_element_by_css_selector("input.field-input").send_keys("al11588")
    	#passwordinput
    	passwordinput = self.browser.find_element_by_xpath("//div[@id='signup-box']/div/form/div[4]/input").send_keys("test")
    	#companyinput
    	companyinput = self.browser.find_element_by_xpath("//div[@id='signup-box']/div/form/div[5]/input").send_keys("moat")
    	#signupbutton
    	signupbutton = self.browser.find_element_by_css_selector("button.button-signup.has-been-enabled").click()


    	#3. I created the One login related test case to verify that users already signed up to the website were able to login on the Login page.
    def testNumber3(self):
    	#loginbuttonclick
    	loginbuttonclick = self.browser.find_element_by_id("login-button").click()
    	#emailaddressinput
    	emailaddressinput = self.browser.find_element_by_id("modal-user").send_keys("email")
    	#passwordinput
    	passwordinput = self.browser.find_element_by_id("modal-password").send_keys("password")
    	#loginclick2
    	loginbuttonclick2 = self.browser.find_element_by_css_selector("button.modal-login-button.has-been-enabled").click()

    	#4. I created the schedule a product demo related test case to verify that users are able to sign up for a demo. In addition, receive emails about Moat Products, Services, and Events.  	
    def testNumber4(self):
    	#firstnameinput
    	firstnameinput = self.browser.find_element_by_xpath("//div[@class='half_width_inputs_container']/div[1]/input").send_keys("firstname")
    	#lastnameinput
    	lastnameinput = self.browser.find_element_by_xpath("//div[@class='half_width_inputs_container']/div[2]/input").send_keys("lastame")
    	#emailaddressinput
    	emailaddressinput = self.browser.find_element_by_xpath("//form[@class='request-demo-form']/div[1]/div[1]/div[1]/div[2]/input").send_keys("email")
    	#jobtitleinput
    	jobtitleinput = self.browser.find_element_by_xpath("//form[@class='request-demo-form']/div[1]/div[1]/div[1]/div[3]/input").send_keys("job title")
    	#companyinput
    	companyinput = self.browser.find_element_by_xpath("//form[@class='request-demo-form']/div[1]/div[1]/div[2]/div[1]/input").send_keys("company")
    	#countryselector
    	countryselector = self.browser.find_element_by_xpath("//form[@class='request-demo-form']/div[1]/div[1]/div[2]/div[2]/div/select//option[225]").is_selected()
    	usaselector = self.browser.find_element_by_xpath("//form[@class='request-demo-form']/div[1]/div[1]/div[2]/div[2]/div/select//option[225]").click()

    	#demoselector
        demoselector = self.browser.find_element_by_xpath("//form[@class='request-demo-form']/div[1]/div[1]/div[2]/div[3]/div/select//option[2]").is_selected()
        moatselector = self.browser.find_element_by_xpath("//form[@class='request-demo-form']/div[1]/div[1]/div[2]/div[3]/div/select//option[2]").click()




        #cleans up actions 
    def tearDown(self):
        self.browser.close()





if __name__ == '__main__':
    unittest.main() 