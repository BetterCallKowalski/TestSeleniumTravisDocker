from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def test_yandex_simple():

    firefox = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.FIREFOX)

    firefox.get('https://yandex.ru')
    assert firefox.title == 'Яндекс'

    firefox.quit()
