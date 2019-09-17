from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def test_ya_simple():

    chrome = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
    firefox = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.FIREFOX)

    chrome.get('https://yandex.ru')
    assert chrome.title == 'Яндекс'
    print(chrome.title)

    firefox.get('https://yandex.ru')
    assert firefox.title == 'Яндекс'
    print(firefox.title)

    chrome.quit()
    firefox.quit()
