from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class WaitingUtils:
    @staticmethod
    def wait_until_clickable(driver, locator):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[TimeoutException, NoSuchElementException,
                                                                               ElementClickInterceptedException])
        try:
            wait.until(ec.element_to_be_clickable(locator)).click()
        except TimeoutException:
            print("Timeout waiting for element to become clickable.")
            return None
        except NoSuchElementException:
            print("Element not found. Check your locator.")
            return None
        except ElementClickInterceptedException:
            print("Element is not clickable at the moment.")
            return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    @staticmethod
    def wait_until_clickable_silent(driver, locator):
        wait = WebDriverWait(driver, 6, poll_frequency=2, ignored_exceptions=[TimeoutException, NoSuchElementException,
                                                                              ElementClickInterceptedException])
        try:
            wait.until(ec.element_to_be_clickable(locator)).click()
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException, Exception):
            return None

    @staticmethod
    def wait_until_visible(driver, locator):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[TimeoutException, NoSuchElementException,
                                                                               ElementClickInterceptedException])
        try:
            element = wait.until(ec.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            print("Timeout waiting for element to become visible.")
            return None
        except NoSuchElementException:
            print("Element not found. Check your locator.")
            return None
        except ElementClickInterceptedException:
            print("Element is not clickable at the moment.")
            return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    @staticmethod
    def wait_until_visible_silent(driver, locator):
        wait = WebDriverWait(driver, 20, poll_frequency=2,
                             ignored_exceptions=[TimeoutException, NoSuchElementException,
                                                 ElementClickInterceptedException])
        try:
            element = wait.until(ec.visibility_of_element_located(locator))
            return element
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException, Exception):
            return False

    @staticmethod
    def wait_until_invisible(driver, locator):
        wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[TimeoutException, NoSuchElementException,
                                                                               ElementClickInterceptedException])
        try:
            element = wait.until(ec.invisibility_of_element_located(locator))
            return element
        except TimeoutException:
            print("Timeout waiting for element to disappear.")
            return None
        except NoSuchElementException:
            print("Element not found. Check your locator.")
            return None
        except ElementClickInterceptedException:
            print("Element is not clickable at the moment.")
            return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    @staticmethod
    def pause(seconds):
        time.sleep(seconds)

    @staticmethod
    def pause_log(duration, message):
        # duration is in miutes, not seconds

        while duration > 0:

            print(f"{message} in {duration} minute(s)")
            time.sleep(60)
            duration -= 1
