'Рассылка писем'
def send_email(message, recipient, sender = "university.help@gmail.com"):
    mail = 0
    z = []
    for k in recipient:
        if k == "@":
            mail += 1
            for l in sender:
                if l == "@":
                    mail += 1
    if mail < 2:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
        return
    if recipient[-1] == "m" and recipient[-2] == "o" and recipient[-3] == "c":
        True
    else:
        if recipient[-1] == "t" and recipient[-2] == "e" and recipient[-3] == "n":
            True
        else:
            if recipient[-1] == "u" and recipient[-2] == "r":
                True
            else:
                print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
                return
    if sender[-1] == "m" and sender[-2] == "o" and sender[-3] == "c":
        True
    else:
        if sender[-1] == "t" and sender[-2] == "e" and sender[-3] == "n":
            True
        else:
            if sender[-1] == "u" and sender[-2] == "r":
                True
            else:
                print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
                return
    if recipient == sender:
        print("Нельзя отправить письмо самому себе")
        return
    if sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
        return
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')
