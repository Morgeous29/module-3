def send_email(message, recipient,  sender = "university.help@gmail.com"):
    if '@' not in recipient or '@' not in sender or not recipient.endswith(
            ('.com', '.ru', '.net')) or not sender.endswith(('.com', '.ru', '.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это письмо невозможно отправить по первому условию программы', 'lexakirillov290497@mail.ru', 'lexakirillov290497@mail.uk')
send_email('Это письмо невозможно отправить по второму условию программы', 'university.help@gmail.com', 'university.help@gmail.com')
send_email('Это письмо корректно отправится', 'lexakirillov290497@gmail.com')
send_email('Это письмо будет с отправлено, но отправитель будет нестандартный', 'lexakirillov290497@mail.ru', 'lexakirillov290497@gmail.com')