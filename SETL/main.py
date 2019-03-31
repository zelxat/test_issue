# -*-coding:UTF-8-*-
from _json import make_encoder

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import funk as f
import tests
import datetime
import time

base_url = 'https://id.rambler.ru/account/registration?back=https%3A%2F%2Fwww.rambler.ru%2F&rname=head'
normal_stat = 200


def main():
    date_now = str(datetime.date.today())
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(base_url)
    if driver.title == 'Регистрация на Рамблер/':
        print('Target page is loaded')
    else:
        print('Somthing wrong')
        exit(1)
        driver.close()
    # test start here
    f.test_resParser(tests.test_login_present(driver), date_now)
    f.test_resParser(tests.test_pass_present(driver), date_now)
    driver.refresh()
    time.sleep(0.5)
    f.test_resParser(tests.test_len_min_login(driver), date_now)
    driver.refresh()
    time.sleep(0.5)
    f.test_resParser(tests.test_len_min_pass(driver), date_now)
    driver.refresh()
    time.sleep(0.5)
    f.test_resParser(tests.test_len_max_login(driver), date_now)
    driver.refresh()
    time.sleep(0.5)
    f.test_resParser(tests.test_len_max_pass(driver), date_now)
    time.sleep(0.5)
    f.test_resParser(tests.test_cyryllic_login(driver), date_now)
    driver.refresh()
    time.sleep(0.5)
    f.test_resParser(tests.test_cyryllic_pass(driver), date_now)
    driver.refresh()
    time.sleep(0.5)
    f.test_resParser(tests.test_exist_login(driver), date_now)
    time.sleep(0.5)
    driver.delete_all_cookies()

    driver.close()
    print('Test\'s done')
    print('Result data in ' + date_now + ' folder')


if __name__ == "__main__":
    main()
