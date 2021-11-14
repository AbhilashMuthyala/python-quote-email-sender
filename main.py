
import smtplib, datetime, random

def send_email(msg):
    my_email = '<email>'
    password = '<password>'
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                        to_addrs="<to_email>",
                        msg=f"Subject: Hello \n\n {msg}")

def current_date():
    cur_time = datetime.datetime.now()
    if cur_time.weekday() == 6:
        quote = read_quotes()
        send_email(quote)

def read_quotes():
    with open('quotes.txt') as quotes_file:
        list_quotes = quotes_file.readlines()
        random_quote = random.choice(list_quotes)
        return random_quote

if __name__ == '__main__':
    current_date()
