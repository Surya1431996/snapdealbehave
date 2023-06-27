from selenium import webdriver

from utilities import ConfigReader


def before_scenario(context,driver):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))

