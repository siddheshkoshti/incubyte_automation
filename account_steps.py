from behave import *
from pythonProject1.pages.home_page import HomePage
from pythonProject1.pages.register_page import RegisterPage
from pythonProject1.pages.login_page import LoginPage
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)





@given('the user is on the home page')
def step_open_home(context):
    context.home = HomePage(context.driver)
    context.home.load()

@when('the user navigates to the create account page')
def step_navigate_to_register(context):
    context.home.go_to_register()

@when('the user fills the registration form with valid data')
def step_fill_registration(context):
    context.register = RegisterPage(context.driver)
    context.email, context.password = context.register.register_new_user()

@then('the user should be registered successfully')
def step_registration_success(context):
    assert context.register.check_success_message()

@when('the user logs out')
def step_logout(context):
    context.register.logout()

@when('the user logs in with the registered credentials')
def step_login(context):
    context.login = LoginPage(context.driver)
    context.login.login(context.email, context.password)

@then('the user should be logged in successfully')
def step_login_success(context):
    assert context.login.is_logged_in()
