from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.common.exceptions import *
from time import sleep

from web_conf import WebConfig
from files import labels


class Runner:
    """
    This class file contains all the necessary test
    methods needed to execute the test cases. It
    is designed dynamically for re-usability purpose.

    """

    def __init__(self):
        """Instantiates the webdriver class"""
        self.site = WebConfig()

    def set_up(self):
        """Launches the COCID site"""
        # sleep(2)
        self.site.launch_browser(labels.url)

    def SignUp(self):
        self.set_up()
        self.insert_cred()
        self.click_Start()

    def click(self, element):
        """
        Since there will be a number of click action,
        The method is made to be reusable
        """
        try:
            Wait(self.site.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
            dom = self.site.driver.find_element_by_css_selector(element)
            self.site.driver.execute_script("arguments[0].click();", dom)

        except TimeoutException or ElementClickInterceptedException or NoSuchElementException or \
               StaleElementReferenceException as exception:
            Wait(self.site.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
            self.site.driver.find_element_by_css_selector(element).click()

            raise exception

    def insert_cred(self):
        """To choose a country, insert the SignUp details"""
        self.click(labels.ncc)
        actions = ActionChains(self.site.driver)
        selector = self.site.driver.find_element_by_css_selector(labels.country_code)
        actions.move_to_element(selector).click().perform()
        self.site.driver.find_element_by_css_selector(labels.phone_number).send_keys(labels.digits_phone_number)
        self.site.driver.find_element_by_css_selector(labels.pswd).send_keys(labels.code)

    def pick_country_code(self):
        self.click(labels.phone_country)
        actions = ActionChains(self.site.driver)
        selector = self.site.driver.find_element_by_css_selector(labels.cntry)
        actions.move_to_element(selector).click().perform()

# @step(u'I am on the CICOD SignUp Page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given I am on the CICOD SignUp Page')
#     wait = Wait(context.wait, 60)
#     wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, labels.start_l))
#     context.driver.find_eleent_by_CSS_selector(labels.start_trial).click()


# @when(u'I enter the web "URL" on the browser')
# def step_impl(self):
#     raise NotImplementedError(u'STEP: When I enter the web "URL" on the browser')


@when(u'I click on "SignUp')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on "SignUp')
    wait = Wait(context.wait, 60)
    wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, labels.start_trial))
    context.driver.find_eleent_by_CSS_selector(labels.start_trial).click()

@when(u'I insert the "Email"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I insert the "Email"')
    wait = Wait(context.wait, 60)
    wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, labels.email_trial))
    context.driver.find_eleent_by_CSS_selector(labels.email_trial).send_keys(labels.input_email)
    sleep(5)

@when(u'I select the "country code"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select the "country code"')
    wait = Wait(context.wait, 60)
    wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, labels.country_code))
    context.driver.find_eleent_by_CSS_selector(labels.country_code).click()
    sleep(5)

@when(u'I insert the "phone number"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I insert the "phone number"')
    wait = Wait(context.wait, 60)
    wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, labels.phone_number))
    context.driver.find_eleent_by_CSS_selector(labels.phone_number).send_keys(labels.digits_phone_number)
    sleep(5)

@when(u'I inser the "business name"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I inser the "business name"')
    wait = Wait(context.wait, 60)
    wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, labels.business_name))
    context.driver.find_eleent_by_CSS_selector(labels.business_name).send_keys(labels.input_business_name)
    sleep(5)

@when(u'I click "Next"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click "Next"')
    wait = Wait(context.wait, 60)
    wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, labels.next_button))
    context.driver.find_eleent_by_CSS_selector(labels.next_button).click()
    sleep(5)

@then(u'I select the "Plan"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I select the "Plan"')
    wait = Wait(context.wait, 60)
    wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, labels.plan_page_select))
    context.driver.find_eleent_by_CSS_selector(labels.plan_page_select).click()
    sleep(5)

@when(u'I click the "Terms of use"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the "Terms of use"')
    wait = Wait(context.wait, 60)
    wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, labels.plan_next))
    context.driver.find_eleent_by_CSS_selector(labels.plan_next).click()
    sleep(5)

@when(u'I click "Start free trial"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click "Start free trial"')
    wait = Wait(context.wait, 60)
    wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, labels.plan_page_select))
    context.driver.find_eleent_by_CSS_selector(labels.plan_page_select).click()
    sleep(5)

@then(u'I should see a message display telling to go and varify my account from my "Email"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see a message display telling to go and varify my account from my "Email"') 
    wait = Wait(context.wait, 60)
    wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, labels.plan_page_select))
    context.driver.find_eleent_by_CSS_selector(labels.plan_page_select).click()
    sleep(5)

@then(u'I copy "password" from my Email')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I copy "password" from my Email')


@then(u'I insert my current password')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I insert my current password')


@then(u'I insert my new password')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I insert my new password')


@then(u'I insert my new password to confirm')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I insert my new password to confirm')


@then(u'I click Done')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I click Done')


@then(u'I close the browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I close the browser')