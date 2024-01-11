from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import string


def scroll_to_element(browser, element):
    x = element.location['x']
    y = element.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (x, y)
    browser.execute_script(scroll_by_coord)
    actions = ActionChains(browser)
    actions.move_to_element(element)
    actions.perform()


def double_click(browser, element):
    actions = ActionChains(browser)
    actions.double_click(element)
    actions.perform()
    return


def find_clickable_parent(browser, element):
    while True:
        # get the parent node of the current element
        parent = element.find_element(By.XPATH, '..')
        # check if the parent element is clickable
        if parent.is_enabled() and parent.is_displayed():
            ActionChains(browser).move_to_element(parent).click().perform()
            break
        else:
            # set the current element to the parent and continue the loop
            element = parent
def find_clickable_parent_right_click(browser, element):
    while True:
        # get the parent node of the current element
        parent = element.find_element(By.XPATH, '..')
        # check if the parent element is clickable
        if parent.is_enabled() and parent.is_displayed():
            ActionChains(browser).move_to_element(parent).context_click().perform()
            break
        else:
            # set the current element to the parent and continue the loop
            element = parent
def random_name():
    characters = string.ascii_letters + string.digits  # Letters and digits
    random_name = ''.join(random.choice(characters) for _ in range(5))
    name=f"test_run_{random_name}"
    return name