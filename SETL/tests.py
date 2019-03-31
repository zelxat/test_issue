# -*-codinf^UTF-8-*-
import funk as f
from selenium.webdriver.common.keys import Keys
import time


def test_login_present(driver):
    if f.is_element_present(driver, 'id', 'login'):
        return {'Login field present': 'passed'}
    return {'Login field present': 'failed'}


def test_pass_present(driver):
    if f.is_element_present(driver, 'id', 'newPassword'):
        return {'Password field present': 'passed'}
    return {'Password field present': 'failed'}


def test_len_min_login(driver):
    driver.find_element_by_id('login').send_keys('qw')
    driver.find_element_by_id('lastname').send_keys('  ')
    time.sleep(0.3)
    if driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/form/section[3]/div/div/div[3]').text == 'Логин должен быть от 3 до 32 символов':
        return {"Len login_min test": 'passed'}
    return {"Len login_min test": 'failed'}


def test_len_min_pass(driver):
    driver.find_element_by_id('newPassword').send_keys('qwertyu')
    driver.find_element_by_id('lastname').send_keys('  ')
    time.sleep(0.2)
    if driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/form/section[4]/div/div[1]/div[2]').text == 'Пароль должен содержать от 8 до 32 символов, ' \
                                                                                    'включать хотя бы одну заглавную латинскую букву, одну строчную и одну цифру':
        return {"Len pass_min test": 'passed'}
    return {"Len pass_min test": 'failed'}


def test_len_max_login(driver):
    driver.find_element_by_id('login').send_keys('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')  # 33 символа
    driver.find_element_by_id('lastname').send_keys('  ')
    time.sleep(0.2)
    if driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/form/section[3]/div/div/div[3]').text == 'Логин должен быть от 3 до 32 символов':
        return {"Len login_max test": 'passed'}
    return {"Len login_max test": 'failed'}


def test_len_max_pass(driver):
    driver.find_element_by_id('newPassword').send_keys(
        'A2aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')  # удовлетворяем условие по сложности пароля но нарушаем длинну
    driver.find_element_by_id('lastname').send_keys('  ')
    time.sleep(0.5)
    if driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/form/section[4]/div/div[1]/div[2]').text == 'Пароль должен содержать от 8 до 32 символов, ' \
                                                                                    'включать хотя бы одну заглавную латинскую букву, одну строчную и одну цифру':
        return {"Len pass_max test": 'passed'}
    return {"Len pass_max test": 'failed'}


def test_exist_login(driver):
    driver.find_element_by_id('login').send_keys('hlebtostovyy')
    driver.find_element_by_id('lastname').send_keys('  ')
    time.sleep(0.4)
    if driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/form/section[3]/div/div/div[3]').text == 'Почтовый ящик недоступен для регистрации. ' \
                                                                                 'Попробуйте другой':
        return {"Len login exist test": 'passed'}
    return {"Len login existx test": 'failed'}  # Почтовый ящик недоступен для регистрации. Попробуйте другой


def test_cyryllic_login(driver):
    driver.find_element_by_id('login').send_keys('кирилица')
    driver.find_element_by_id('lastname').send_keys('  ')
    time.sleep(0.4)
    if driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/form/section[3]/div/div/div[3]').text == 'Недопустимый логин':
        return {'Login cyrillic test': 'passed'}
    return {'Login cyrillic test': 'failed'}  # /html/body/div[1]/div/div[2]/form/section[3]/div/div/div[3]


def test_cyryllic_pass(driver):
    driver.find_element_by_id('newPassword').send_keys('кирилицаалалалал')
    driver.find_element_by_id('firstname').send_keys('   ')
    driver.find_element_by_id('lastname').send_keys(Keys.TAB)
    driver.implicitly_wait(0.7)
    if driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/form/section[4]/div/div[1]/div[2]').text == 'Вы вводите русские буквы':
        return {'Password cyrillic test': 'passed'}
    return {'Password cyrillic test': 'failed'}  # /html/body/div[1]/div/div[2]/form/section[4]/div/div[1]/div[2]
