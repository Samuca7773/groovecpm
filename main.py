import os
from time import sleep
from rich.console import Console
from rich_gradient import Gradient
from rich.text import Text
from rich.prompt import Prompt
from groovecpm import GrooveCPM
import sys
console = Console()

__TELEGRAM__ = "t.me/Samuca_007"
colors = ["FF0000", "FFA500", "FFFF00", "FFA500"]
interrogation = "[?]"
process = "[%]"
attention = "[!]"

banner = '''
██╗░░██╗░█████╗░░█████╗░██╗░░██╗
██║░░██║██╔══██╗██╔══██╗██║░██╔╝
███████║███████║██║░░╚═╝█████═╝░
██╔══██║██╔══██║██║░░██╗██╔═██╗░
██║░░██║██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
'''
banner2 = '''
░█████╗░██████╗░███╗░░░███╗
██╔══██╗██╔══██╗████╗░████║
██║░░╚═╝██████╔╝██╔████╔██║
██║░░██╗██╔═══╝░██║╚██╔╝██║
╚█████╔╝██║░░░░░██║░╚═╝░██║
░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝
'''


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def center_text(text):
    width = console.width
    lines = text.splitlines()
    centered_lines = [line.center(width) for line in lines]
    return "\n".join(centered_lines)        
    

def gradient_text(text, symbol='', end=""):
    gradient_text = Gradient(f"{symbol}{text}", colors=[colors[0], colors[1], colors[2], colors[3]]) 
    console.print(gradient_text, end=end)

def gradient_input(prompt_text, symbol, end=' '):
    gradient_text = Gradient(f"{symbol} {prompt_text}", colors=[colors[0], colors[1], colors[2], colors[3]])
    console.print(gradient_text, end=end) 
    user_input = input()
    return user_input




def login():
    clear()   
    centered_banner = center_text(banner)
    centered_banner2 = center_text(banner2)
    gradient_text(centered_banner)
    gradient_text(centered_banner2)
    print("\n")
    email = gradient_input("DIGITE SEU EMAIL >>", interrogation)
    password = gradient_input("DIGITE SUA SENHA >>", interrogation)
    access_key = gradient_input("DIGITE SUA CHAVE DE ACESSO >>", interrogation)
    gradient_text(" PROCESSANDO: ", process)
    if not email or not password or not access_key:
        sleep(1)
        console.print("NADA PODE FICAR EM BRANCO!")
        sleep(1)
        login()
    
    global cpm
    cpm = GrooveCPM(access_key)
    login_response = cpm.login(email, password)
    if cpm.auth_token:
        console.print("SUCESSO")
        sleep(1)
        menu()
    else:
        console.print(login_response)
        sleep(1)
        login()

def load_player_data():
    print("\n")
    gradient_text("         DEUS SEJA LOUVADO", end="\n")
    gradient_text("==========[ INFORMAÇÕES ]==========", end='\n')
    data = cpm.get_player_data()
    gradient_text(f" DONO      > t.me/Samuca_007", symbol=attention, end='\n')
    gradient_text(f" NOME      > {data.get('name')} ", symbol=attention, end='\n')
    gradient_text(f" ID        > {data.get('id')}", symbol=attention, end='\n')
    gradient_text(f" COIN      > {data.get('coin')}", symbol=attention, end='\n')
    gradient_text(f" DINHEIRO  > {data.get('money')}", symbol=attention, end='\n')
    
def load_key_data():
    data = cpm.get_key_data()
    gradient_text("========[ CHAVE DE ACESSO ]========", end='\n')
    gradient_text(f" SUA CHAVE > {data.get('key')}", symbol=attention, end='\n')
    gradient_text(f" VALIDADE  > {data.get('status')}", symbol=attention, end='\n')
    gradient_text(f" TELEFONE  > {data.get('telefone')}", symbol=attention, end='\n')
    
def menu():
    clear()
    centered_banner = center_text(banner)
    centered_banner2 = center_text(banner2)
    gradient_text(centered_banner)
    gradient_text(centered_banner2)
    load_player_data()
    load_key_data()
    gradient_text("=============[ MENU ]==============", end="\n")
    gradient_text(" INJETAR COIN", symbol="[01]", end='\n')
    gradient_text(" INJETAR DINHEIRO", symbol="[02]", end='\n')
    gradient_text(" KING RANK", symbol="[03]", end='\n')
    gradient_text(" ID PERSONALIZADO", symbol="[04]", end='\n')
    gradient_text(" NOME GRANDE", symbol="[05]", end='\n')
    gradient_text(" NOME COLORIDO", symbol="[06]", end='\n')
    gradient_text(" DELETAR CONTA", symbol="[07]", end='\n')
    gradient_text(" DELETAR AMIGOS", symbol="[08]", end='\n')
    gradient_text(" LIBERAR TODOS CARROS", symbol="[09]", end='\n')
    gradient_text(" LIBERAR CARROS PAGOS", symbol="[10]", end='\n')
    gradient_text(" SIRENE EM TODOS CARROS", symbol="[11]", end='\n')
    gradient_text(" LIBERAR W16", symbol="[12]", end='\n')
    gradient_text(" LIBERAR RODAS", symbol="[13]", end='\n')
    gradient_text(" DESATIVAR DANO NO MOTOR", symbol="[14]", end='\n')
    gradient_text(" GASOLINA ILIMITADA", symbol="[15]", end='\n')
    gradient_text(" LIBERAR CASA PAGA", symbol="[16]", end='\n')
    gradient_text(" LIBERAR FUMAÇA", symbol="[17]", end='\n')
    gradient_text(" ALTERAR CORRIDAS GANHAS", symbol="[18]", end='\n')
    gradient_text(" ALTERAR CORRIDAS PERDIDAS", symbol="[19]", end='\n')
    gradient_text(" LIBERAR ANIMAÇÕES", symbol="[20]", end='\n')
    gradient_text(" LIBERAR ROUPAS", symbol="[21]", end='\n')
    gradient_text(" COMPLETAR LEVELS", symbol="[22]", end='\n')
    gradient_text(" RESETAR LEVELS", symbol="[23]", end='\n')
    gradient_text(" LIBERAR BUZINAS", symbol="[24]", end='\n')
    gradient_text(" CLONAR CARROS", symbol="[25]", end='\n')
    gradient_text(" REMOVER FRENTE DO CARRO", symbol="[26]", end="\n")
    gradient_text(" REMOVER TRÁS DO CARRO", symbol="[27]", end="\n")
    gradient_text(" TODOS CARROS COM KM MAXÍMO", symbol="[28]", end="\n")
    gradient_text(" SAIR", symbol="[00]", end='\n')
    
    gradient_text("==============[ CPM ]==============", end="\n")
    service = gradient_input("DIGITE UM NÚMERO >>", symbol=interrogation)
    # Injetar Coin
    if service == "1":
        amount = gradient_input("QUANTIDADE >>", symbol=interrogation)
        gradient_text(" PROCESSANDO: ", process)
        if not amount:
            console.print("NADA PODE FICAR EM BRANCO!", end="\n")
            sleep(1)
            menu()
        try:
            amount_int = int(amount)
        except ValueError:
            console.print("ISSO NÃO É UM NÚMERO!", end="\n")
            sleep(1)
            menu()
        
        response = cpm.set_coin(amount_int)
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    elif service == "2":
        amount = gradient_input("QUANTIDADE >>", symbol=interrogation)
        gradient_text(" PROCESSANDO: ", process)
        if not amount:
            console.print("NADA PODE FICAR EM BRANCO!", end="\n")
            sleep(1)
            menu()
        try:
            amount_int = int(amount)
        except ValueError:
            console.print("ISSO NÃO É UM NÚMERO!", end="\n")
            sleep(1)
            menu()
        
        response = cpm.set_money(amount_int)
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # King rank
    elif service == "3":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.set_player_rank()
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # ID Personalizado
    elif service == "4":
        new_id = gradient_input("NOVO ID >>", symbol=interrogation)
        gradient_text(" PROCESSANDO: ", process)
        if not new_id:
            console.print("NADA PODE FICAR EM BRANCO!", end="\n")
            sleep(1)
            menu()
        response = cpm.set_id(new_id)
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Nome grande
    elif service == "5":
        new_name = gradient_input("NOVO NOME >>", symbol=interrogation)
        gradient_text(" PROCESSANDO: ", process)
        if not new_name:
            console.print("NADA PODE FICAR EM BRANCO!", end="\n")
            sleep(1)
            menu()
            
        response = cpm.set_name(new_name)
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Nome colorido
    elif service == "6":
        new_name = gradient_input("NOVO NOME >>", symbol=interrogation)
        gradient_text(" PROCESSANDO: ", process)
        if not new_name:
            console.print("NADA PODE FICAR EM BRANCO!", end="\n")
            sleep(1)
            menu()
        
        response = cpm.set_name_rainbow(new_name)
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Deletar conta
    elif service == "7":
        confirm = gradient_input("DIGITE 'confirmar' >>", symbol=attention)
        if confirm == 'confirmar':
            gradient_text(" PROCESSANDO: ", process)
            response = cpm.delete()
            console.print(response, end="\n")
            sleep(1)
            login()
        else:
            gradient_text(" PROCESSANDO: ", process)
            console.print("CANCELADA!", end="\n")
            sleep(1)
            menu()
    
    # Deletar amigos
    elif service == "8":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.delete_friends()
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Liberar todos carros
    elif service == "9":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.unlock_all_cars()
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Liberar carros pagos
    elif service == "10":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.unlock_all_paid_cars()
        console.print(response, end="\n")
        sleep(1)
        menu()
        
    # liberar sirene em todos carros
    elif service == "11":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.unlock_all_cars_sirens()
        console.print(response, end="\n")
        sleep(1)
        menu()
   
    # Liberar w16
    elif service == "12":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.unlock_w16()
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Desbloquear rodas 
    elif service == "13":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.unlock_wheels()
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Desbloquear engine damage
    elif service == "14":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.disable_engine_damage()
        console.print(response, end="\n")
        sleep(1)
        menu()
   
   # Gasolina ilimitada
    elif service == "15":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.unlimited_fuel()
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Liberar casa paga
    elif service == "16":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.unlock_house()
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Liberar fumaça
    elif service == "17":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.unlock_smoke()
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Alterar corridas ganhas
    elif service == "18":
        new_race = gradient_input("QUANTIDADE >>", symbol=interrogation)
        gradient_text(" PROCESSANDO: ", process)
        if not new_race:
            console.print("NADA PODE FICAR EM BRANCO", end="\n")
            sleep(1)
            menu()
        try:
            new_race_int = int(new_race)
        except ValueError:
            console.print("ISSO NÃO É UM NÚMERO!", end="\n")
            sleep(1)
            menu()
        
        response = cpm.set_race_win(new_race_int)
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Alterar corridas perdidas
    elif service == "19":
        new_race = gradient_input("QUANTIDADE >>", symbol=interrogation)
        gradient_text(" PROCESSANDO: ", process)
        if not new_race:
            console.print("NADA PODE FICAR EM BRANCO", end="\n")
            sleep(1)
            menu()
        try:
            new_race_int = int(new_race)
        except ValueError:
            console.print("ISSO NÃO É UM NÚMERO!", end="\n")
            sleep(1)
            menu()
        
        response = cpm.set_race_lose(new_race_int)
        console.print(response, end="\n")
        sleep(1)
        menu()
        
    # Liberar animações
    elif service == "20":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.unlock_all_animations()
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Liberar roupas
    elif service == "21":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.unlock_all_cosmetics()
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Completar todos levels
    elif service == "22":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.unlock_all_levels()
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Resetar todos levels
    elif service == "23":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.reset_all_levels()
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Liberar buzinas
    elif service == "24":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.unlock_horns()
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Clonar carros
    elif service == "25":
        email_clone = gradient_input("EMAIL >>", symbol=interrogation)
        password_clone = gradient_input("SENHA >>", symbol=interrogation)
        gradient_text(" PROCESSANDO: ", process)
        if not email_clone or not password_clone:
            console.print("NADA PODE FICAR EM BRANCO", end="\n")
            sleep(1)
            menu()
        response = cpm.clone_cars(email_clone, password_clone)
        console.print(response, end="\n")
        sleep(1)
        menu()
    
    # Remover parte da frente do carro
    elif service == "26":
        car_id = gradient_input("DIGITE O ID >>", symbol=interrogation)
        gradient_text(" PROCESSANDO: ", process)
        if not car_id:
            console.print("NADA PODE FICAR EM BRANCO", end="\n")
            sleep(1)
            menu()
        try:
            car_id_int = int(car_id)
        except ValueError:
            console.print("ISSO NÃO É UM NÚMERO!", end="\n")
            sleep(1)
            menu()
        
        response = cpm.remove_front_parts(car_id_int)
        console.print(response)
        sleep(1)
        menu()

    elif service == "27":
        car_id = gradient_input("CARRO ID >>", symbol=interrogation)
        gradient_text(" PROCESSANDO: ", process)
        if not car_id:
            console.print("NADA PODE FICAR EM BRANCO", end="\n")
            sleep(1)
            menu()
        try:
            car_id_int = int(car_id)
        except ValueError:
            console.print("ISSO NÃO É UM NÚMERO!", end="\n")
            sleep(1)
            menu()
        
        response = cpm.remove_back_parts(car_id_int)
        console.print(response)
        sleep(1)
        menu()
    
    elif service == "28":
        gradient_text(" PROCESSANDO: ", process)
        response = cpm.all_cars_max_mileage()
        console.print(response, end="\n")
        sleep(1)
        menu()
        
    # Sair do script
    elif service == "00":
        gradient_text(" SAINDO..", symbol=attention, end="\n")
        sys.exit(0)
    # Caso o usuário digite um numero invalido
    else:
        gradient_text(" OPÇÃO INVÁLIDA!", symbol=attention, end="\n")
        sleep(1)
        menu()
if __name__ == "__main__":
    login()