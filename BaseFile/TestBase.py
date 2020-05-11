from Utility import readconfig
from selenium import webdriver
sauce_username ="puday30"
sauce_access_key ="b1e8e930-63e5-4480-afb1-340227eb6a71"
remote_url = "https://ondemand.saucelabs.com:443/wd/hub"

class testbase():

    def __init__(self):

        self.username = "jipriyaji"
        self.access_key = "ZgABv7GLauSgj0s6JG73Lz6vW5y6O6YbvnZEu8udFf9cdVH9Sx"
        #30106150-9b07-4120-833b-ef1df173eff8
        self.remote_url = "hub.lambdatest.com/wd/hub"

       # self.path ="C:\\Users\\ravin\\Desktop\\chromedriver.exe"
        self.url ="https://web-neighbors.staging.ziplyn.com/"


        #self.browser=readconfig.readconfig("section1","Browser")

        self.user ="ravikumar"
        self.pwd="ravikumar@123"

        self.user1="priyankacontractor"
        self.pwd1="priyanka@123"

        desired_cap = {
            'platform': "win10",
            'browserName': "chrome",
            'version': "67.0",
            # Resolution of machine
            "resolution": "1024x768",
            "name": "Zuuddo Regression Test ",
            "build": "Zuuddo Regression Test",
            "network": True,
            "video": True,
            "visual": True,
            "console": True,
        }

        # URL: https://{username}:{accessToken}@hub.lambdatest.com/wd/hub
        url = "https://"+self.username+":"+self.access_key+"@"+self.remote_url

        print("Initiating remote driver on platform: "+desired_cap["platform"]+" browser: "+desired_cap["browserName"]+" version: "+desired_cap["version"])
        self.driver = webdriver.Remote(
            desired_capabilities=desired_cap,
            command_executor= url
        )

        #self.driver = Chrome(executable_path=self.path)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()



    def launchpage(self):

        self.driver.get(self.url)
        self.driver.set_page_load_timeout(20)
        self.driver.implicitly_wait(10)



        return self.driver

    def getuser(self):

        return self.user

    def getuserpassword(self):

        return self.pwd