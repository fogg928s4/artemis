import re, os, json
from datetime import datetime
from pathlib import Path
from contextlib import ExitStack

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

def main():
    load_config()
    print_art()
    print("Extrayendo informacion de HTML...")


if __name__ == "__main__":
    main()