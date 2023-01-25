import smtplib
import os

print("****Welcome to Email Sending BOT****")
# print("Please select from the following")
# print("1. Initialize (add or change sending mail)")
# print("2. Send Mail")
# print("3. Exit")
# choice=int(input("Enter your choice: "))

try: 
    while True:
        print("Please select from the following")
        print("1. Initialize (add or change sending mail)")
        print("2. Send Mail")
        print("3. Exit")
        choice=int(input("\nEnter your choice: "))
        os.system('cls')
        match choice:
            case 1:
                with open("your_gmail.txt",'w') as sender_gmail:
                    sgmail=input("Enter your gmail: ")
                    if(not sgmail.endswith("@gmail.com")):
                        raise ValueError("Error: gmail not ends with \"@gmail.com\"")
                    sender_gmail.write(sgmail)
                with open("pass.txt",'w') as sender_pass:
                    print("(To generate app password: READ readme.txt)")
                    passwd=input("App password: ")
                    sender_pass.write(passwd)
                os.system('cls')
            case 2:
                with open("your_gmail.txt",'r') as sgf:
                    sender_gmail=sgf.read()
                with open("pass.txt",'r') as passf:
                    passwd=passf.read()
                
                receiver_gmail=input("To (Receiver gmail): ")
                if(not receiver_gmail.endswith("@gmail.com")):
                        raise ValueError("Error: gmail not ends with \"@gmail.com\"")
                subject=input("Subject: ")
                mess=input("Message (Enter Send to send mail):\n")
                while True:
                    if(mess=='Send' or mess=='SEND' or mess=='send' or mess=='"send"'):
                        break
                    with open("message.txt",'a') as mess_file:
                        mess_file.write('\n'+mess)
                    mess=input()
                with open("message.txt",'r') as f:
                    mess=f.read()
                with open("message.txt",'w') as mess_file:
                    mess_file.write("")
                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(sender_gmail,passwd)
                message='Subject: {}\n\n{}'.format(subject,mess)
                server.sendmail(sender_gmail,receiver_gmail,message)
                server.close()
                print("Mail Send!!")
                os.system('cls')
            case 3:
                print("Keep Gmail and App password saved?")
                a=int(input("1. Yes\n2. No\n>>>"))
                while True:
                    match a:
                        case 1:
                            os.system('attrib +h message.txt')
                            os.system('attrib +h pass.txt')
                            os.system('attrib +h your_gmail.txt')
                            exit()
                        case 2:
                            os.remove("message.txt")
                            os.remove("pass.txt")
                            os.remove("your_gmail.txt")
                            exit()
                        case _:
                            print("Invalid Input!!")
            case _:
                print("Invalid input!!")
except Exception as e:
    print(e)
