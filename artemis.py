import re, os, json
from datetime import datetime
from pathlib import Path
from contextlib import ExitStack
import requests

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

def fetch_HTML(requestURL):
    r = requests.get(requestURL)
    if r.status_code == 200:
        print("Succesfully retrieved HTML data")
        return r.text
    else:
        print("An Error ocurred fetching the data")
        return ""


def main():
    print_art()
    try:
        config = load_config()
        print("Extrayendo informacion de HTML...")
        fetch_HTML(config['url'])
    except FileNotFoundError:
        print("\n  [!] Error: No se encontró el archivo 'config.json'.")
    except Exception as e:
        print(f"\n  [!] Error inesperado: {e}")




if __name__ == "__main__":
    main()