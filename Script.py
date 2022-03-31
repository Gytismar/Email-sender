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

datafile = "Kompanijos.csv" #FAILAS PRADEDAMAS SKAITYTI NUO ANTROS EILUTĖS, komandos pavadinimas ir tada 
data = list(csv.reader(open(datafile, encoding='utf-8')))

infofile = "Config.csv"
Sender_info = list(csv.reader(open(infofile, encoding='utf-8')))

#datafile - kompanijos ir jų paštai
#infofile - prisijungimas,slaptažodis,port ir pan.

# Sender_info[0][1] - iš kokio pašto siųs
# Sender_info[1][1] - pašto slaptažodis
# Sender_info[2][1] - laiško tema
# Sender_info[3][1] - Attachment pavadinimas
# Sender_info[4][1] - port numeris
# Sender_info[5][1] - SMTP arba EMAIL adresas

sender_email = Sender_info[0][1]
password = Sender_info[1][1]
subject = Sender_info[2][1]
port = Sender_info[4][1]
SMTPAdress = Sender_info[5][1]

rowcount = 0 #eilučių kiekis
for row in open(datafile):
  rowcount+= 1

for x in range(1,rowcount): #for loop siuntimui laiškų
  receiver_email = data[x][1]
  
  #Sukuriamas MIMEMultipart objektas
  msg = MIMEMultipart("alternative")
  msg["Subject"] = subject                       #Laiško pavadinimas
  msg["From"] = sender_email                     #Rodys kas siunčia
  msg["To"] = data[x][1]                         #Kam siunčia
  filename = Sender_info[3][1]                   #Prisegamas failas

  read_file = io.open("Email HTML.txt", "r", encoding = "utf8") #skaitys laišką iš Email HTML.txt (Laiškas būtinai html formatu)
  html = read_file.read()  
  html = html.replace('$$$$',data[x][0])                        #skaito failą ir pakeičia '$$$$' į rinkodaros komandos, į kurią siuničamas laiškas, pavadinimą
  read_file.close()                                             

  part = MIMEText(html, "html")
  msg.attach(part)

  # Pridedamas prisegamas failas
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