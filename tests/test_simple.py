from selenium.webdriver.firefox.webdriver import WebDriver


def test_ya_simple():
    driver = WebDriver(executable_path='C://selenium//chromedriver.exe')

    driver.get('https://yandex.ru')

    assert driver.title == 'Яндекс'

    driver.close()