# Email-sender
Automatiškas laiškų siuntimas

## Kontaktai
Sukurta https://github.com/Gytismar

Bet kokias klausimais rašykite gytismar@gmail.com

## Instaliavimas
```
pip install secure-smtplib
pip install requires.io
```

## Naudojimas
Naudoja python automatiškai siųsti laiškus

Laišką reikia turėti HTML formatu "Email HTML.txt" faile

Kompanijos pavadinimą ir jos paštą reikia laikyti "Kompanijos.csv" faile, kompanijų skaičius neribojamas, tačiau patartina per daug vienu metu nesiųsti, nes gali išsiųsti laiškai patekti į spam (PRADEDAMA SKAITYTI NUO ANTROS EILUTĖS)

Koreguoti Config.csv failą pagal savo duomenis

## Config failas:
1. Prisjungimas
2. Slaptažodis pašto
3. Laiško tema
4. Prisegamo failo pavadinimas (pvz. - "Bendradarbiavimo_pasiūlymas.pdf")
5. Port siuntimo (Pagal encryption - 465, 587)
6. SMTP arba EMAIL adresas (pvz. smtp.gmail.com)

## Notes
Norint siųsti iš tam tikro pašto reikia dažniausiai išjungti 2FA bei leisti siuntimą per SMTP (link į kaip tai padaryti su gmail: (https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python/27515833#27515833)

Pradinis config failas padarytas siuntimui laiškų per gmail
