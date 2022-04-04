#Sukurta https://github.com/Gytismar
#Bet kokias klausimais rašykite gytismar@gmail.com

from asyncore import read
import smtplib, ssl, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import io
import csv
import json
import time

def mainScript():
    f = open('config.json')
    dataFromJson = json.load(f)
    f.close()

    datafile = dataFromJson["csvDir"] #FAILAS PRADEDAMAS SKAITYTI NUO ANTROS EILUTĖS, komandos pavadinimas ir tada 
    data = list(csv.reader(open(datafile, encoding='utf-8')))


    sender_email = dataFromJson["Prisijungimas"]
    password = dataFromJson["Slaptazodis"]
    sleeptime = dataFromJson["Sleep"]
    subject = dataFromJson["Theme"]
    port = int(dataFromJson["Port"])
    SMTPAdress = dataFromJson["SMTP"]

    rowcount = 0 #eilučių kiekis
    for row in open(datafile):
        rowcount+= 1

    for x in range(1,rowcount): #for loop siuntimui laiškų
        time.sleep(sleeptime)
        receiver_email = data[x][1]
        #Sukuriamas MIMEMultipart objektas
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject                       #Laiško pavadinimas
        msg["From"] = sender_email                     #Rodys kas siunčia
        msg["To"] = data[x][1]                         #Kam siunčia
        filename = dataFromJson["Attachment"]                   #Prisegamas failas

        read_file = io.open(dataFromJson["txtDir"], "r", encoding = "utf8") #skaitys laišką iš Email HTML.txt (Laiškas būtinas html formatu)
        html = read_file.read()  
        html = html.replace('$$$$',data[x][0])                        #skaito failą ir pakeičia '$$$$' į rinkodaros komandos, į kurią siuničamas laiškas, pavadinimą
        read_file.close()                                             

        part = MIMEText(html, "html")
        msg.attach(part)

        # Pridedamas prisegamas failas
        if dataFromJson["Attachment"] != '':
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            "attachment", filename= filename
        )
        msg.attach(part)

        # Sukuriamas SMTP prisijungimas ir išsiunčiamas laiškas
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTPAdress, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, msg.as_string()
            )