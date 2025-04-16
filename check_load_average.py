import requests
import time
import os
from datetime import datetime



# Konfiguration
BOT_ID = os.getenv("BOT_ID")
CHAT_ID = os.getenv("CHAT_ID")
LOG_FILE = "/home/jambo2/log/load_average.log"
SLEEP_INTERVAL = 10  # Intervall in Sekunden

def get_load_average():
    with open('/proc/loadavg', 'r') as f:
        load = f.read().split()[0]
    return float(load)

def get_cpu_cores():
    return os.cpu_count()

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{BOT_ID}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"Fehler beim Senden an Telegram: {e}")

def log_message(msg):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} ---- {msg}\n")

def monitor():
    print("🚀 Überwachung gestartet. Überprüfung alle", SLEEP_INTERVAL, "Sekunden.")
    while True:
        load = get_load_average()
        cores = get_cpu_cores()

        if load >= cores:
            msg = f"⚠️ Hohe CPU-Auslastung! Aktuelle Last: {load}, CPU-Kerne: {cores}"
            send_telegram_alert(msg)
            log_message(f"HOHE LAST: {load}")
        else:
            log_message(f"OK: {load}")

        time.sleep(SLEEP_INTERVAL)

if __name__ == "__main__":
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    monitor()



