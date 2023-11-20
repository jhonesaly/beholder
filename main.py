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
            current_content = soup.prettify()  # Convertendo o objeto BeautifulSoup para string formatada

            if previous_content is not None and current_content != previous_content:
                changes = find_changes(previous_content, current_content)
                if changes:
                    toast_message = "Mudança Detectada:\n" + changes
                    toaster.show_toast("Mudança Detectada", toast_message)

            previous_content = current_content

        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter a página: {e}")

        time.sleep(10)

def find_changes(previous_content, current_content):
    # Encontre diferenças entre o conteúdo anterior e atual (pode precisar de uma biblioteca adicional)
    # Neste exemplo, estamos apenas comparando as strings diretamente
    if previous_content != current_content:
        return "Conteúdo anterior:\n{}\n\nConteúdo atual:\n{}".format(previous_content, current_content)
    else:
        return None

if __name__ == "__main__":
    # Importa a URL do arquivo de configuração
    with open('main.conf', 'r') as config_file:
        config = config_file.read()
        exec(config)

    check_website_change(URL_ALVO)
