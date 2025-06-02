import requests
import time
import os

BOT_ID = os.getenv("BOT_ID")
CHAT_ID = os.getenv("CHAT_ID")
LOG_FILE = "/your/path/to/log/load_average.log"
SLEEP_TIME = 10  # Проверять каждые 10 секунд

def get_load():
    with open("/proc/loadavg") as f:
        load = f.read().split()[0]
    return float(load)

def get_cores():
    return os.cpu_count()

def send_alert(text):
    url = f"https://api.telegram.org/bot{BOT_ID}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    try:
        requests.post(url, data=data)
    except:
        print("Fehler beim Senden an Telegram:")

def write_log(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

def monitor():
    print("Überwachung gestartet. Überprüfung alle...")
    while True:
        load = get_load()
        cores = get_cores()
        msg = f"Load: {load}, Cores: {cores}"

        if load >= cores:
            alert_msg = f"Hohe CPU-Auslastung! Aktuelle Last: {load}"
            send_alert(alert_msg)
            write_log(alert_msg)
        else:
            write_log(msg)

        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    monitor()

