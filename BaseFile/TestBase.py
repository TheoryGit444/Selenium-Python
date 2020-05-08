from Utility import readconfig
from selenium import webdriver
sauce_username ="puday30"
sauce_access_key ="b1e8e930-63e5-4480-afb1-340227eb6a71"
remote_url = "https://ondemand.saucelabs.com:443/wd/hub"

class testbase():

    def __init__(self):

        self.sauce_username = "ravisharma"
        self.sauce_access_key = "38de4964-354d-4d80-bdf9-2717e4cd1b74"
        #30106150-9b07-4120-833b-ef1df173eff8
        self.remote_url = "https://ondemand.saucelabs.com:443/wd/hub"

       # self.path ="C:\\Users\\ravin\\Desktop\\chromedriver.exe"
        self.url ="https://web-neighbors.staging.ziplyn.com/"


        #self.browser=readconfig.readconfig("section1","Browser")

        self.user ="ravikumar"
        self.pwd="ravikumar@123"

        self.user1="priyankacontractor"
        self.pwd1="priyanka@123"

        sauceOptions = {
            'screenResolution': '1280x768',
            'seleniumVersion': '3.141.59',
            'build': 'Onboarding ZuudooApp - Python + UnitTest',
            'name': 'regression_demo',
            'username': self.sauce_username,
            'accessKey': self.sauce_access_key,
            # tags to filter test reporting.
            'tags': ['instant-sauce', 'ruby-rspec', 'module4'],
            # setting sauce-runner specific parameters such as timeouts helps
            # manage test execution speed.
            'maxDuration': 1800,
            'commandTimeout': 300,
            'idleTimeout': 1000
        }
        # In ChromeOpts, we define browser and/or WebDriver capabilities such as
        # the browser name, browser version, platform name, platform version
        chromeOpts = {
            'platformName': 'Windows 10',
            'browserName': 'chrome',
            'browserVersion': 'latest',
            'goog:chromeOptions': {'w3c': True},
            'sauce:options': sauceOptions,
            'extendedDebugging': True,
            'capturePerformance': True
        }
        self.driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=chromeOpts)

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