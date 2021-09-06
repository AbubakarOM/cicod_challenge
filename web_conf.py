from selenium import webdriver


class WebConfig:
    """
    This creates the instance of a web driver
    to help automate the web app.
    """

    def __init__(self):
        self.driver = webdriver.Chrome()

    def launch_browser(self, url):
        self.driver.get(url)
