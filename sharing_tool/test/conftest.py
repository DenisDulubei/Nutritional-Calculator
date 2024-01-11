import os
import pytest
import json
from selenium import webdriver



@pytest.fixture(scope='session')
def config():
    current_file_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(current_file_path)
    project_root = os.path.dirname(parent_directory)
    config_path = os.path.join(project_root, "src", "config", "tests_config.json")
    with open(config_path) as config_file:
        config = json.load(config_file)
    return config


def set_options(opts, config):
    if config['driver']['headless']:
        opts.add_argument('--headless')
        width = config['driver']['window_size']['width']
        height = config['driver']['window_size']['height']
        opts.add_argument(f'--window-size={width},{height}')
    opts.add_argument("--log-level=3")
    opts.add_argument("--disable-logging")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-notifications")

@pytest.fixture(scope="session")
def browser(config):
    if config['driver']['browser'] == 'Firefox':
        opts = webdriver.FirefoxOptions()
        set_options(opts, config)
        driver = webdriver.Firefox(options=opts)

    elif config['driver']['browser'] == 'Chrome':
        opts = webdriver.ChromeOptions()
        set_options(opts, config)
        driver = webdriver.Chrome(options=opts)

    elif config['driver']['browser'] == 'Edge':
        opts = webdriver.EdgeOptions()
        set_options(opts, config)
        driver = webdriver.Edge(options=opts)

    else:
        raise Exception(f'Unknown type of browser')

    driver.implicitly_wait(config['driver']['implicit_wait'])
    driver.maximize_window()

    yield driver

    driver.quit()