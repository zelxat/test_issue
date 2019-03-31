# -*-coding:UTF-8-*-
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import os
import datetime
import HTML


def is_element_present(driver, how, what):
    try:
        driver.find_element(by=how, value=what)
    except NoSuchElementException:
        return False
    return True


def is_element_present(brouser, how, what):
    try:
        brouser.find_element(by=how, value=what)
    except NoSuchElementException:
        return False
    return True


def is_element_wisible(brouser, how, what):
    try:
        brouser.find_element(by=how, value=what)
    except NoSuchElementException:
        return False
    return brouser.find_element(by=how, value=what).is_displayed()


def save_sreen_shoot(brouser, usr_num):
    ud = usr_num
    path = '.\\' + ud['name'] + '\\' + '\\Screenshots\\'
    del (ud)
    now_time = datetime.datetime.now()
    name = str(now_time.hour) + str(now_time.minute) + str(now_time.second) + '.png'
    if os.path.exists(path):
        path += name
        return brouser.save_screenshot(path)
    else:
        os.makedirs(path)
        path += name
        return brouser.save_screenshot(path)


def test_resParser(dct, usr_num):
    assert isinstance(dct, dict)
    ud = usr_num
    path = '.\\' + ud + '\\'
    test_results = dct
    del (ud)

    # dict of colors for each result:
    result_colors = {
        'passed': 'lime',
        'failed': 'red',
        'error': 'yellow',
        'founded': 'lime',
        'missed': 'red',
        'blocked': 'black',
        'name': 'white'
    }

    tbl = HTML.Table(header_row=['Test', 'Result'])
    for test_id in sorted(test_results):
        # create the colored cell:
        color = result_colors[test_results[test_id]]
        colored_result = HTML.TableCell(test_results[test_id], bgcolor=color)
        # append the row with two cells:
        tbl.rows.append([test_id, colored_result])
    htmlcode = str(tbl)

    if os.path.exists(path):
        f = open(path + 'resultar.html', 'a')
        f.write(htmlcode)
        f.write('<p>')
        f.close()
        return 0
    else:
        os.makedirs(path)
        f = open(path + 'resultar.html', 'w')
        f.write(htmlcode)
        f.write('<p>')
        f.close()
        return 0
