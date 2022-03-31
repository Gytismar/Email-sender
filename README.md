# Email-sender
Automatiškas laiškų siuntimas

Sukurta https://github.com/Gytismar, bet kokias klausimais rašykite gytismar@gmail.com

Naudoja python automatiškai siųsti laiškus naudojantis CSV failą skaityti duomenims

Laišką reikia turėti HTML formatu "Email HTML.txt" faile

Rinkodaros komandos ir jos paštą reikia laikyti "Kompanijos.csv" faile, kompanijų skaičius neribojamas, tačiau patartina per daug nesiųsti, nes gali išsiųsti laiškai patekti į spam (PRADEDAMA SKAITYTI NUO ANTROS EILUTĖS)

Config faile:
1. Prisjungimas
2. Slaptažodis pašto
3. Laiško tema
4. Prisegamo failo pavadinimas (pvz. - "Bendradarbiavimo_pasiūlymas.pdf")
5. Port siuntimo (Pagal encryption - 465, 587)
6. SMTP arba EMAIL adresas (pvz. smtp.gmail.com)

Norint siųsti iš tam tikro pašto reikia dažniausiai išjungti 2FA bei leisti siuntimą per SMTP (link į kaip tai padaryti su gmail: (https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python/27515833#27515833)

Pradinis config failas padarytas siuntimui laiškų per gmail

Reikia pirma instaliuoti:
1. pip install secure-smtplib
2. pip install requires.io
