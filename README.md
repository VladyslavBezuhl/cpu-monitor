# CPU-Lastüberwachung mit Telegram-Benachrichtigung

Ein einfaches Python-Projekt zur Überwachung der CPU-Auslastung eines Linux-Systems. Wenn die durchschnittliche Systemlast die Anzahl der CPU-Kerne erreicht oder übersteigt, wird automatisch eine Benachrichtigung über Telegram versendet. Zusätzlich werden Logs lokal gespeichert.

## Funktionen

- Liest die aktuelle Systemlast aus `/proc/loadavg`
- Versendet Warnmeldungen über Telegram-Bot
- Protokolliert Lastwerte in eine Logdatei
- Kann in einem Docker-Container ausgeführt werden

## Projektstruktur

├── check_load_average.py       # Hauptskript
├── Dockerfile                  # Docker-Konfiguration
├── requirements.txt            # Python-Abhängigkeiten
├── .env                        # Umgebungsvariablen
└── .dockerignore               # Dateien, die vom Build ausgeschlossen werden



## Einrichtung

Erstelle eine Datei mit dem Namen `.env` im Projektverzeichnis mit folgendem Inhalt:

BOT_ID=dein_bot_token           # Dein Bot Token
CHAT_ID=deine_chat_id           # Deine Chat ID
SLEEP_INTERVAL=10               # Schlafintervall in Sekunden



## Container starten

  docker run -d \
  --name cpu-check-app \
  --env-file .env \
  -v /home/deinuser/log:/home/deinuser/log \
  --mount type=bind,source=/proc,target=/host_proc,readonly \
  cpu-check-app


## Test

Du kannst die CPU künstlich auslasten, um die Benachrichtigungsfunktion zu testen:

python3 -c "while True: pass"
