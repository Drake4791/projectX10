import smtplib
from email.mime.text import MIMEText


def send_email():
    sender = ""                     #Сюда почту отправителя.
    password = ""                   #Пароль от почты отправителя.
    recipient = ""                  #Почта куда отправить email.
#ВАЖНО аккаунт отправителя-настройки бьезопасности-ВКЛ двухэтапную авт. - 
#- Пароли и приложения - Создаем приложение(Другое) и сгенерированный пароль юзаем тут.
    server = smtplib.SMTP("smtp.gmail.com", 25)         #сервак, порт и лог.
    server.starttls()
    
    try:
        with open("index.html") as file:      #Название файла
            message = file.read()
    except IOError:
        return "ЯЙЦА ФАЙЛ ГОВНО"

    try:
        server.login(sender, password)
        mimeMSG = MIMEText(message, 'html')            
        mimeMSG["From"] = sender                            #От кого письмо
        mimeMSG["To"] = recipient                           #Кому письмо
        mimeMSG["Subject"] = "Заголовок крутой"    #Сюда тему сообщения пишим.  
        server.sendmail(sender, recipient, mimeMSG.as_string())      #(отправитель, получатель, сообщение)

        return("Сообщение отправлено.")

    except Exception as _exc:                                          #На ошибки чекаем
        return f"{_exc} \n Неправильный Логин/Пароль."


def main():
    print(send_email())


if __name__ == "__main__":
    main()


