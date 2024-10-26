def send_email(message, recipient, sender = "university.help@gmail.com"):

    list_recipient = list(recipient)
    list_sender = list(sender)

    if sender == recipient:
        print('Нельзя отправить письмо самому себе')

    elif ((sender == "university.help@gmail.com")
        and (('@' in list_recipient)
        and ('.ru' in recipient or '.com' in recipient or '.net' in recipient))):
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)

    elif (sender != "university.help@gmail.com") and (('@' in list_recipient and '@' in list_sender)
        and (('.ru' in recipient or '.com' in recipient or '.net' in recipient)
        and ('.ru' in sender or '.com' in sender or '.net' in sender))):
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)


    else:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)



send_email('проверка', 'asdg@gmail.com')

send_email('привет', 'annamur25@yandex.ru', "university.info@gmail.su" )

send_email('Изучайте Python', 'annamur25@yandex.ru', "university.help@gmail.com")

send_email('Изучайте Python', 'annamur25@yandex.ru', "ABCDI@mail.com")

send_email('Напоминалка', 'university.help@gmail.com', "university.help@gmail.com")

send_email('Напоминалка', 'university.help@gmail.com', "university.helpgmail.com")