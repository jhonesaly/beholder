import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import time

def check_website_change(url):
    toaster = ToastNotifier()
    previous_content = None
    i = 0

    while True:
        i += 1
        print(f"Observação {i}")
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

        time.sleep(10)

if __name__ == "__main__":
    # Importa a URL do arquivo de configuração
    with open('main.conf', 'r') as config_file:
        config = config_file.read()
        exec(config)

    check_website_change(URL_ALVO)
