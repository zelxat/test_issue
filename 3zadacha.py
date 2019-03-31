#-*-coding:UTF-8-*-
import imaplib
import getpass
import datetime

ans = raw_input("Здравствуйте, хотите использовать тестовый ящик? (y/n)")
if ans == 'y':
    obj = imaplib.IMAP4_SSL('imap.rambler.ru', 993)
    obj.login("hlebtostovyy@rambler.ru", "753951qweR")
    obj.select('INBOX')
    status, response = obj.search(None, '(UNSEEN)')
    now = datetime.datetime.now()
    result = now.strftime("%d-%m-%Y %H:%M you have ") + str(len(response[0].split())) + ' непрочитанных сообщений'
    print(result)
    f = open('test_m.dat', 'a')
    f.write(result + '\n')
    f.close()
    obj.logout()
elif ans == 'n':
    print('Перед использоанием убедитесь, что в настройках вашего ящика \n' \
          'разрешены почтовые программы')
    mail = raw_input('Введие ваш email _> ')
    pasw = raw_input('Введите пароль _> ')
    obj = imaplib.IMAP4_SSL('imap.rambler.ru', 993)
    obj.login(mail, pasw)
    obj.select('INBOX')
    status, response = obj.search(None, '(UNSEEN)')
    now = datetime.datetime.now()
    result = now.strftime("%d-%m-%Y %H:%M you have ") + str(len(response[0].split())) + ' непрочитанных сообщений'
    print(result)
    f = open('pers_m.dat', 'a')
    f.write(result + '\n')
    f.close()
    obj.logout()
else:
    print(' я не понел :V')
raw_input(u"Нажмите любую кнопку для выхода.")
