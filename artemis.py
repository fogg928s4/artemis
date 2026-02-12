import re, os, json
from datetime import datetime
from pathlib import Path
from contextlib import ExitStack
import requests
from bs4 import BeautifulSoup

def print_art():
    print("                           ♦                ")
    print("                          * *               ")
    print("                         *   *              ")
    print("                        *  ♦  *             ")
    print("                         :   :              ")
    print("                         : A :              ")
    print("                         : R :              ")
    print("                     __* : T : *__          ")
    print("              ..___/** T ♦ E ♦ M **\\___..   ")
    print("             /*** R ^````: M :````^ I ***\\  ")
    print("            <* A \"\"      : I :      \"\" S *> ")
    print("              `\"`        : S :        `\"`   ")
    print("                         :   :              ")
    print("                         :   :              ")
    print("                         :   :              ")
    print("                         : ♥ :              ")
    print("                         : ♥ :              ")
    print("                         : ♥ :              ")
    print("                         :   :              ")
    print("                         :   :              ")
    print("                         :   :              ")
    print("                         :   :              ")
    print("                        ♦  ♦  ♦             ")
    print("                         *   *              ")
    print("                          * *               ")
    print("                           ♦                ")
    

def load_config():
    config_path = Path('config.json')
    if not config_path.exists():
        raise FileNotFoundError("config.json no encontrado")
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Reads information from url
def fetch_HTML(request_URL, header_list):
    r = requests.get(request_URL, headers=header_list)
    if r.status_code == 200:
        print("Succesfully retrieved HTML data")
        return r.text
    else:
        print("An Error ocurred fetching the data")
        return ""

def extract_info(rawHTML, tag, tag_class):
    soup = BeautifulSoup(rawHTML, 'html.parser')
    return soup.find_all(tag, class_=tag_class)
    print(":p")

def show_output(info):
    for i in info:
        print(i.get_text(strip=True))

def main():
    print_art()
    try:
        config = load_config()
        print("Extrayendo informacion de HTML...")
        raw_html = fetch_HTML(config['url'], header_list=config['headers'])
        if raw_html == "":
            print(f'No se pudo extraer información de la URL {config['url']}')
            print(":p")
            exit()
        else: 
            info = extract_info(raw_html, config['tag'],config['tagClass'])
            show_output(info)
        
    except FileNotFoundError:
        print("\n  [!] Error: No se encontró el archivo 'config.json'.")
    except Exception as e:
        print(f"\n  [!] Error inesperado: {e}")




if __name__ == "__main__":
    main()