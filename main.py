import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import time

def check_website_change(url, interval_minutes=1):
    toaster = ToastNotifier()
    previous_content = None

    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            current_content = str(soup)

            if previous_content is not None and current_content != previous_content:
                toaster.show_toast("Mudança Detectada", "A página alvo foi alterada!")
            
            previous_content = current_content

        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter a página: {e}")

        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    # Substitua a URL pela página que você deseja monitorar
    target_url = "https://exemplo.com"
    check_website_change(target_url)
