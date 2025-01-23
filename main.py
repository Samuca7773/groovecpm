from groovecpm import GrooveCPM
import sys
import os
from time import sleep
from rich.console import Console
import pyfiglet
import threading
import requests

console = Console()
enter_pressed = False



def clear():
    os.system("cls" if os.name == 'nt' else "clear")

def check_enter():
    global enter_pressed
    input()
    enter_pressed = True

def banner():
    global enter_pressed
    clear()
    text1 = pyfiglet.figlet_format("   GROOVE\n          CPM")
    threading.Thread(target=check_enter, daemon=True).start()
    
    while not enter_pressed:
        clear()
        console.print(f"[bold red]{text1}")
        console.print("     [bold red]..pressione enter para prosseguir..")
        sleep(0.01)

    login()

def login():
    clear()
    account_email = console.input(" [[bold red]?[/bold red]][bold white] DIGITE SEU EMAIL >> [/bold white]")
    account_password = console.input(" [[bold red]?[/bold red]][bold white] DIGITE SUA SENHA >> [/bold white]")
    access_key = console.input(" [[bold red]?[/bold red]][bold white] DIGITE SUA CHAVE DE ACESSO >> [/bold white]")
    
    sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
    sys.stdout.flush()
    if not account_email or not account_password or not access_key:
        sleep(2)
        sys.stdout.write(f"\033[1;31mNADA PODE FICAR EM BRANCO\033[0m\n")
        sleep(2)
        login()
    
    url_data = "https://ipinfo.io/json?token=10a94f3a0b0ec0"
    response = requests.post(url_data)
    if response.status_code == 200:
        data = response.json()
        ip = data.get("ip")
        country = data.get("country")
        region = data.get("region")
        global cpm
        cpm = GrooveCPM(access_key)
        login_response = cpm.login(account_email, account_password, ip, region, country)
        if cpm.auth_token:
            sys.stdout.write(f"\033[1;31mSUCESSO\033[0m\n")
            sleep(2)
            menu()
        else:
            sys.stdout.write(f"\033[1;31m{login_response}\033[0m\n")
            sleep(2)
            login()
    else:
        console.print(" [[bold red]![/bold red]][bold white] NÃO FOI POSSIVEL OBTER SEU IP[/bold white]")
        sleep(2)
        menu()

        
def get_data():
    data = cpm.get_player_data()
    #id
    if data.get("localid") is not None:
        console.print(f" [[bold red]![/bold red]][bold white] ID                 >[/bold white] [bold red]{data.get('localid')}[/bold red]")
    else:
        console.print(f" [[bold red]![/bold red]][bold white] ID                 >[/bold white] [bold red]INDEFINIDO[/bold red]")
    
    # nome
    if data.get("name") is not None:
        console.print(f" [[bold red]![/bold red]][bold white] NOME               >[/bold white] [bold red]{data.get('name')}[/bold red]")
    else:
        console.print(f" [[bold red]![/bold red]][bold white] NOME               >[/bold white] [bold red]INDEFINIDO[/bold red]")
    
    # coin
    if data.get("coin") is not None:
        console.print(f" [[bold red]![/bold red]][bold white] COINS              >[/bold white] [bold red]{data.get('coin')}[/bold red]")
    else:
        console.print(f" [[bold red]![/bold red]][bold white] COINS              >[/bold white] [bold red]INDEFINIDO[/bold red]")
    
    # money
    if data.get("money") is not None:
        console.print(f" [[bold red]![/bold red]][bold white] DINHEIROS          >[/bold white] [bold red]{data.get('money')}[/bold red]")
    else:
        console.print(f" [[bold red]![/bold red]][bold white] DINHEIROS          >[/bold white] [bold red]INDEFINIDO[/bold red]")
    
    # fumaça
    if data.get("smoke") == 1.0:
        console.print(f" [[bold red]![/bold red]][bold white] FUMAÇA             >[/bold white] [bold red]LIBERADA[/bold red]")
    elif data.get("smoke") == 0.0:
        console.print(f" [[bold red]![/bold red]][bold white] FUMAÇA             >[/bold white] [bold red]NÃO LIBERADA[/bold red]")
    else:
        console.print(f" [[bold red]![/bold red]][bold white] FUMAÇA             >[/bold white] [bold red]INDEFINIDO[/bold red]")
        
    # w16
    if data.get("w16") == 1.0:
        console.print(f" [[bold red]![/bold red]][bold white] W16                >[/bold white] [bold red]LIBERADA[/bold red]")
    elif data.get("w16") == 0.0:
        console.print(f" [[bold red]![/bold red]][bold white] W16                >[/bold white] [bold red]NÃO LIBERADA[/bold red]")
    else:
        console.print(f" [[bold red]![/bold red]][bold white] W16                >[/bold white] [bold red]INDEFINIDO[/bold red]")
        
    # casa paga
    if data.get("house") == 1:
        console.print(f" [[bold red]![/bold red]][bold white] CASA PAGA          >[/bold white] [bold red]LIBERADA[/bold red]")
    elif data.get("house") == 0:
        console.print(f" [[bold red]![/bold red]][bold white] CASA PAGA          >[/bold white] [bold red]NÃO LIBERADA[/bold red]")
    else:
        console.print(f" [[bold red]![/bold red]][bold white] CASA PAGA          >[/bold white] [bold red]INDEFINIDO[/bold red]")
    # corridas ganhas
    if data.get("race_win"):
        console.print(f" [[bold red]![/bold red]][bold white] CORRIDAS GANHAS    >[/bold white] [bold red]{data.get('race_win')}[/bold red]")
    else:
        console.print(f" [[bold red]![/bold red]][bold white] CORRIDAS GANHAS    >[/bold white] [bold red]INDEFINIDO[/bold red]")
    
    # Corridas perdidas 
    if data.get("race_lose"):
        console.print(f" [[bold red]![/bold red]][bold white] CORRIDAS PERDIDAS  >[/bold white] [bold red]{data.get('race_lose')}[/bold red]")
    else:
        console.print(f" [[bold red]![/bold red]][bold white] CORRIDAS PERDIDAS  >[/bold white] [bold red]INDEFINIDO[/bold red]")
    
    # Gasolina
    if data.get("gasoline") == 1.0:
        console.print(f" [[bold red]![/bold red]][bold white] GASOLINA ILIMITADA >[/bold white] [bold red]LIBERADA[/bold red]")
    elif data.get("gasoline") == 0.0:
        console.print(f" [[bold red]![/bold red]][bold white] GASOLINA ILIMITADA >[/bold white] [bold red]NÃO LIBERADA[/bold red]")
    else:
        console.print(f" [[bold red]![/bold red]][bold white] GASOLINA ILIMITADA >[/bold white] [bold red]INDEFINIDO[/bold red]")
    
    # Motor 
    if data.get("engine_damage") == 1.0:
        console.print(f" [[bold red]![/bold red]][bold white] MOTOR INQUEBRAVEL  >[/bold white] [bold red]LIBERADO[/bold red]")
    elif data.get("engine_damage") == 0.0:
        console.print(f" [[bold red]![/bold red]][bold white] MOTOR INQUEBRAVEL  >[/bold white] [bold red]NÃO LIBERADO[/bold red]")
    else:
        console.print(f" [[bold red]![/bold red]][bold white] MOTOR INQUEBRAVEL   >[/bold white] [bold red]INDEFINIDO[/bold red]")
    console.print("\n")
        

def menu():
    clear()
    console.print(" [bold white]INFORMAÇÕES[/bold white]")
    console.print(" [[bold red]![/bold red]] [bold white]DONO               > [/bold white][bold red]t.me/Samuca_007[/bold red]")
    console.print(" [[bold red]![/bold red]] [bold white]PAINEL             > [/bold white][bold red]VIP[/bold red]")
    get_data()
    console.print(" [bold white]MENU[/bold white]")
    console.print(" [[bold red]01[/bold red]][bold white] INJETAR COIN[/bold white]")
    console.print(" [[bold red]02[/bold red]][bold white] INJETAR DINHEIRO[/bold white]")
    console.print(" [[bold red]03[/bold red]][bold white] LIBERAR ROUPAS[/bold white]")
    console.print(" [[bold red]04[/bold red]][bold white] LIBERAR RODAS[/bold white]")
    console.print(" [[bold red]05[/bold red]][bold white] LIBERAR ANIMAÇÕES[/bold white]")
    console.print(" [[bold red]06[/bold red]][bold white] ID PERSONALIZADO[/bold white]")
    console.print(" [[bold red]07[/bold red]][bold white] NOME GRANDE[/bold white]")
    console.print(" [[bold red]08[/bold red]][bold white] LIBERAR BUZINAS[/bold white]")
    console.print(" [[bold red]09[/bold red]][bold white] LIBERAR TODOS CARROS[/bold white]")
    console.print(" [[bold red]10[/bold red]][bold white] DELETAR CONTA[/bold white]")
    console.print(" [[bold red]11[/bold red]][bold white] LIBERAR FUMAÇA[/bold white]")
    console.print(" [[bold red]12[/bold red]][bold white] LIBERAR W16[/bold white]")
    console.print(" [[bold red]13[/bold red]][bold white] LIBERAR CASA PAGA[/bold white]")
    console.print(" [[bold red]14[/bold red]][bold white] DELETAR AMIGOS[/bold white]")
    console.print(" [[bold red]15[/bold red]][bold white] ALTERAR CORRIDAS GANHAS[/bold white]")
    console.print(" [[bold red]16[/bold red]][bold white] ALTERAR CORRIDAS PERDIDAS[/bold white]")
    console.print(" [[bold red]17[/bold red]][bold white] KING RANK[/bold white]")
    console.print(" [[bold red]18[/bold red]][bold white] GASOLINA ILIMITADA[/bold white]")
    console.print(" [[bold red]19[/bold red]][bold white] MOTOR INQUEBRAVEL[/bold white]")
    console.print(" [[bold red]20[/bold red]][bold white] CLONAR CARROS[/bold white]")
    console.print(" [[bold red]00[/bold red]][bold white] SAIR[/bold white]")
    
    
    service = console.input(" [[bold red]?[/bold red]][bold white] DIGITE A OPÇÃO DESEJADA >> [/bold white]")

    # Verificador
    # Injetar coin
    if service == "1":
        amount = console.input(" [[bold red]?[/bold red]][bold white] DIGITE A QUANTIDADE DE COINS >> [/bold white]") 
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        if not amount:
            sleep(1)
            sys.stdout.write(f"\033[1;31mNADA PODE FICAR EM BRANCO\033[0m\n")
            sys.stdout.flush()
            sleep(2)
            menu()
        try:
            amount_int = int(amount)
        except ValueError:
            sleep(1)
            sys.stdout.write(f"\033[1;31mISSO NÃO E UM NÚMERO\033[0m\n")
            sys.stdout.flush()
            sleep(2)
            menu()
        response = cpm.set_coin(amount_int)
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
    # Injetar money
    elif service == "2":
        amount = console.input(" [[bold red]?[/bold red]][bold white] DIGITE A QUANTIDADE DE DINHEIRO >> [/bold white]") 
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        if not amount:
            sleep(1)
            sys.stdout.write(f"\033[1;31mNADA PODE FICAR EM BRANCO\033[0m\n")
            sleep(2)
            menu()
        try:
            amount_int = int(amount)
        except ValueError:
            sleep(1)
            sys.stdout.write(f"\033[1;31mISSO NÃO E UM NÚMERO\033[0m\n")
            sys.stdout.flush()
            sleep(2)
            menu()
        response = cpm.set_money(amount_int)
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
        
    # Liberar roupas
    elif service == "3":
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        response = cpm.unlock_cosmetics()
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
    
    # Liberar rodas
    elif service == "4":
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        response = cpm.unlock_wheels()
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
        
    # Liberar animações
    elif service == "5":
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        response = cpm.unlock_animations()
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
    
    # Alterar ID
    elif service == "6":
        new_id = console.input(" [[bold red]?[/bold red]][bold white] DIGITE O NOVO ID >> [/bold white]")
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        if not new_id:
            sleep(1)
            sys.stdout.write(f"\033[1;31mNADA PODE FICAR EM BRANCO\033[0m\n")
            sys.stdout.flush()
            sleep(2)
            menu()
            
        response = cpm.set_id(new_id)
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
    
    # Alterar nome
    elif service == "7":
        new_name = console.input(" [[bold red]?[/bold red]][bold white] DIGITE O NOVO NOME >> [/bold white]")
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        if not new_name:
            sleep(1)
            sys.stdout.write(f"\033[1;31mNADA PODE FICAR EM BRANCO\033[0m\n")
            sys.stdout.flush()
            sleep(2)
            menu()
            
        response = cpm.set_name(new_name)
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
    
    # Liberar buzinas
    elif service == "8":
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        response = cpm.unlock_buzines()
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
    
    # Liberar carros
    elif service == "9":
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        response = cpm.unlock_all_cars()
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
    
    # Deletar conta
    elif service == "10":
        confirm = console.input(" [[bold red]?[/bold red]][bold white] Digite 'confirmar' > [/bold white]")
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        if confirm != "confirmar":
            sys.stdout.write(f"\033[1;31mEXCLUSÃO CANCELADA\033[0m\n")
            sys.stdout.flush()
            sleep(2)
            menu()
        response = cpm.delete_account()
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        login()
    
    # Liberar fumaça
    # contasjjdjxndnwiiwjs@gmail.com
    elif service == "11":
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        response = cpm.unlock_smoke()
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
    
    # Liberar w16
    elif service == "12":
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        response = cpm.unlock_w16()
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
    
    # Liberar casa paga
    elif service == "13":
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        response = cpm.unlock_house()
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
    
    # Deletar amigos
    elif service == "14":
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        response = cpm.delete_friends()
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
    
    # Alterar corridas ganhas
    elif service == "15": 
        amount = console.input(" [[bold red]?[/bold red]][bold white] DIGITE A QUANTIDADE DE CORRIDAS >> [/bold white]")
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        if not amount:
            sleep(1)
            sys.stdout.write(f"\033[1;31mNADA PODE FICAR EM BRANCO\033[0m\n")
            sys.stdout.flush()
            sleep(2)
            menu()
        try:
            amount_int = int(amount)
        except ValueError:
            sleep(1)
            sys.stdout.write(f"\033[1;31mISSO NÃO E UM NÚMERO\033[0m\n")
            sys.stdout.flush()
            sleep(2)
            menu()
        response = cpm.set_race_win(amount_int)
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
    
    # Alterar corridas perdidas
    elif service == "16":
        amount = console.input(" [[bold red]?[/bold red]][bold white] DIGITE A QUANTIDADE DE CORRIDAS >> [/bold white]")
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        if not amount:
            sleep(1)
            sys.stdout.write(f"\033[1;31mNADA PODE FICAR EM BRANCO\033[0m\n")
            sys.stdout.flush()
            sleep(2)
            menu()
        try:
            amount_int = int(amount)
        except ValueError:
            sleep(1)
            sys.stdout.write(f"\033[1;31mISSO NÃO E UM NÚMERO\033[0m\n")
            sys.stdout.flush()
            sleep(2)
            menu()
        response = cpm.set_race_lose(amount_int)
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
    
    # King rank
    elif service == "17":
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        response = cpm.set_player_rank()
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
    
    # Gasolina Ilimitada
    elif service == "18":
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        response = cpm.unlimited_gasoline()
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
        
    # Desativar dano ao motor
    elif service == "19":
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        response = cpm.disable_engine_damage()
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sys.stdout.flush()
        sleep(2)
        menu()
    
    # Clonar conta
    elif service == "20":
        email = console.input(" [[bold red]?[/bold red]][bold white] DIGITE O EMAIL QUE IRÁ RECEBER >> [bold white]")
        password = console.input(" [[bold red]?[/bold red]][bold white] DIGITE A SENHA >> [/bold white]")
        sys.stdout.write(" [\033[1;33m%\033[1;97m] PROCESSANDO: \033[0m")
        sys.stdout.flush()
        if not email or not password:
            sleep(1)
            sys.stdout.write(f"\033[1;31mNADA PODE FICAR EM BRANCO\033[0m\n")
            sys.stdout.flush()
            sleep(2)
            menu()
        
        response = cpm.clone_cars(email, password)
        sys.stdout.write(f"\033[1;31m{response}\033[0m\n")
        sleep(2)
        menu()
    
    # Sair do sistema
    elif service == "00":
        console.print(" [[bold red]![/bold red]] [bold white]SAINDO..[/bold white]")
    else:
        console.print(" [[bold red]![/bold red]][bold white] OPÇÃO INVÁLIDA[/bold white]")
        sleep(2)
        menu()
    
if __name__ == "__main__":
    banner()