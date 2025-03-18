
from pystyle import Colorate, Colors
from groovecpm import GrooveCPM
from time import sleep
from rich.console import Console
import os, signal, sys

console = Console()

__TELEGRAM__ = "Samuca_007"
__CHANNEL__ = "t.me/GrupoCarParking"

def bold_rainbow_text(text):
    text_colored = Colorate.Horizontal(Colors.green_to_yellow, text)
    return f"\033[1m{text_colored}\033[0m"

print(bold_rainbow_text("INSIRA SEU EMAIL:"))


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

def signal_handler(sig, frame):
    print(bold_rainbow_text("[!] Saindo..."))
    sys.exit(0)

def center_text(text):
    width = console.width
    lines = text.splitlines()
    centered_lines = [line.center(width) for line in lines]
    return "\n".join(centered_lines)

centered_banner1 = center_text(banner)
centered_banner2 = center_text(banner2)
    
def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('error'):
        print(bold_rainbow_text("DADOS NÃO FORAM BUSCADOS CORRETAMENTE!"))
        sys.exit(0)
    if 'localid' in response and 'coins' in response and 'moneys' and 'Name' in response:
        print(bold_rainbow_text("==============[ PLAYER DETALHES ]============="))
        print(bold_rainbow_text(f"  >> EMAIL    : "), end="")
        console.print(f"[bold white]{acc_email}[/bold white]", end="\n")
        print(bold_rainbow_text(f"  >> NOME     : "), end="")
        console.print(f"[bold white]{response.get('Name', 'INDEFINIDO')}[/bold white]", end="\n")
        print(bold_rainbow_text(f"  >> ID       : "), end="")
        console.print(f"[bold white]{response.get('localid', 'INDEFINIDO')}[/bold white]", end="\n")
        print(bold_rainbow_text(f"  >> COINS    : "), end="")
        console.print(f"[bold white]{response.get('coins', 'INDEFINIDO')}[/bold white]", end="\n")
        print(bold_rainbow_text(f"  >> DINHEIRO : "), end="")
        console.print(f"[bold white]{response.get('moneys', 'INDEFINIDO')}[/bold white]", end="\n")
    else:
        print(bold_rainbow_text("ERROR: DADOS AUSENTE NA RESPOSTA DO SERVIDOR!"))
        sys.exit(0)

def load_key_data(cpm):
    response = cpm.get_key_data()
    if response.get('error'):
        print(bold_rainbow_text("ERROR: DADOS NÃO FORAM BUSCADOS CORRETAMENTE!"))
        sys.exit(0)
    print(bold_rainbow_text("===============[ KEY DETALHES ]==============="))
    print(bold_rainbow_text(f"  >> CHAVE    : "), end="")
    console.print(f"[bold white]{response.get('access_key', 'INDEFINIDO')}[/bold white]", end='\n')
    print(bold_rainbow_text(f"  >> VALIDADE : "), end="")
    console.print(f"[bold white]{response.get('expire', 'INDEFINIDO')}[/bold white]", end="\n")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        os.system("cls") if os.name == 'nt' else os.system('clear')
        print(bold_rainbow_text(centered_banner1))
        print(bold_rainbow_text(centered_banner2))
        print("\n")
        print(bold_rainbow_text(" INSIRA SEU EMAIL: "), end="")
        global acc_email
        acc_email = input()
        print(bold_rainbow_text(" INSIRA SUA SENHA: "), end="")
        acc_password = input()
        print(bold_rainbow_text(" CHAVE DE ACESSO : "), end="")
        access_key = input()
        console.print("[bold white] PROCESSANDO: [/bold white]", end="")
        if not acc_email or not acc_password or not access_key:
            sleep(0.5)
            print(bold_rainbow_text("NÃO DEIXE NADA EM BRANCO"), end="\n")
            sleep(1)
            continue
        cpm = GrooveCPM(access_key)
        login = cpm.auth(acc_email, acc_password)
        if not cpm.auth_token:
            print(bold_rainbow_text(f"{login.get('message')}"))
            sleep(1)
            continue
        print(bold_rainbow_text("SUCESSO"))
        sleep(1)
        while True:
            os.system("cls") if os.name == 'nt' else os.system("clear")
            print(bold_rainbow_text("=============================================="))
            print(Colorate.Horizontal(Colors.red_to_yellow, "FERRAMENTA CPM1 || DONO: https://t.me/Samuca77"))
            load_player_data(cpm)
            load_key_data(cpm)
            print(bold_rainbow_text("===================[ MENU ]==================="))
            for i, option in enumerate([
                "CUSTOM COIN", "CUSTOM MONEY", "KING RANK", "CUSTOM ID", "CUSTOM NOME",
                "DELETAR CONTA", "DELETAR AMIGOS", "LIBERAR CARROS PAGOS", "LIBERAR TODOS CARROS",
                "LIBERAR SIRENE EM CARROS", "LIBERAR CARRO POR ID", "LIBERAR SIRENE POR ID",
                "CUSTOM TORQUE EM CARRO POR ID", "REMOVER FRENTE DO CARRO POR ID",
                "REMOVER TRÁS DO CARRO POR ID", "LIBERAR KM MÁXIMO EM TODOS CARROS",
                "LIBERAR KM MÁXIMO EM CARRO POR ID", "LIBERAR W16", "LIBERAR BUZINAS",
                "DESATIVAR DANO NO MOTOR", "LIBERAR GASOLINA ILIMITADA", "LIBERAR CASA PAGA",
                "LIBERAR FUMAÇA", "LIBERAR RODAS", "LIBERAR ANIMAÇÕES", "LIBERAR ROUPAS",
                "CUSTOM CORRIDAS GANHAS", "CUSTOM CORRIDAS PERDIDAS", "COMPLETAR LEVELS",
                "RESETAR LEVELS", "CLONAR CARROS"
            ], start=1):
               console.print(f"  [[bold green]{i:02}[/bold green]] [bold white]{option}[/bold white]")
            console.print("  [[bold green]00[/bold green]] SAIR")
            print(bold_rainbow_text("===================[ CPM✩ ]==================="))
            service = input(bold_rainbow_text("  SELECIONE O SERVIÇO: "))
            
            # Custom Coin
            if service == "1" or service == 1:
                print(bold_rainbow_text("  VALOR: "), end="")
                amount = input()
                console.print("[bold white]  PROCESSANDO: [/bold white]", end="")
                if not amount:
                    sleep(0.5)
                    print(bold_rainbow_text("NÃO DEIXE NADA EM BRANCO"), end="\n")
                    sleep(1)
                    continue
                
                try:
                    amount_int = int(amount)
                except ValueError:
                    sleep(0.5)
                    print(bold_rainbow_text("DIGITE APENAS NÚMEROS!"), end="\n")
                    sleep(1.0)
                    continue
                
                response = cpm.set_player_coin(amount)
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                sleep(1)
                continue
            
            # Custom Money
            elif service == "2" or service == 2:
                print(bold_rainbow_text("  VALOR: "), end="")
                amount = input()
                console.print("[bold white]  PROCESSANDO: [/bold white]", end="")
                if not amount:
                    sleep(0.5)
                    print(bold_rainbow_text("NÃO DEIXE NADA EM BRANCO"), end="\n")
                    sleep(1.0)
                    continue
                
                try:
                    amount_int = int(amount)
                except ValueError:
                    sleep(0.5)
                    print(bold_rainbow_text("DIGITE APENAS NÚMEROS!"), end="\n")
                    sleep(1)
                    continue
                
                response = cpm.set_player_money(amount)
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                sleep(1)
                continue
            
            # King Rank
            elif service == "3" or service == 3:
                console.print("[bold white]  PROCESSANDO: [/bold white]", end="")
                response = cpm.set_player_rank()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                sleep(1)
                continue
                
            # Set ID
            elif service == "4" or service == 4:
                print(bold_rainbow_text("  NOVO ID: "), end="")
                new_id = input()
                console.print("[bold white]  PROCESSANDO: [/bold white]", end="")
                if not new_id:
                    sleep(0.5)
                    print(bold_rainbow_text("NÃO DEIXE NADA EM BRANCO"), end="\n")
                    sleep(1)
                    continue
                
                response = cpm.set_player_id(new_id)
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                sleep(1)
                continue
            
            # Set Name
            elif service == "5" or service == 5:
                print(bold_rainbow_text("  NOVO NOME: "), end="")
                new_name = input()
                console.print("[bold white]  PROCESSANDO: [/bold white]", end="")
                if not new_name:
                    sleep(0.5)
                    print(bold_rainbow_text("NÃO DEIXE NADA EM BRANCO"), end="\n")
                    sleep(1)
                    continue
                
                response = cpm.set_player_name(new_name)
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                sleep(1)
                continue
            
            # Delete Account
            elif service == "6" or service == 6:
                print(bold_rainbow_text("  DIGITE confirmar: "), end="")
                confirm = input()
                console.print("[bold white]  PROCESSANDO: [/bold white]", end="")
                if not confirm:
                    sleep(0.5)
                    print(bold_rainbow_text("NÃO DEIXE NADA EM BRANCO"), end="\n")
                    sleep(1)
                    continue
                
                if str(confirm) == 'confirmar':
                    response = cpm.delete_account()
                    print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                    sleep(1)
                    break
                else:
                    sleep(0.5)
                    print(bold_rainbow_text("CANCELANDO OPERAÇÃO"), end="\n")
                    sleep(1)
                    continue
            
            # Delete Friends
            elif service == 7 or service == "7":
                console.print("[bold white]  PROCESSANDO: [/bold white]", end="")
                response = cpm.delete_friends()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                sleep(1)
                continue
            
            # Unlock paid cars
            elif service == 8 or service == "8":
                console.print("[bold white]  PROCESSANDO: [/bold white]", end="")
                response = cpm.unlock_paid_cars()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                sleep(1)
                continue
            
            # Unlock all cars
            elif service == 9 or service == "9":
                console.print("[bold white]  PROCESSANDO: [/bold white]", end="")
                response = cpm.unlock_all_cars()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                sleep(1)
                continue
            
            # Unlock siren in cars
            elif service == 10 or service == "10":
                console.print("[bold white]  PROCESSANDO: [/bold white]", end="")
                response = cpm.unlock_all_cars_sirens()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                sleep(1)
                continue
            
            # Unlock car id
            elif service == 11 or service == "11":
                print(bold_rainbow_text("  DIGITE O ID: "), end="")
                car_id = input()
                console.print("[bold white]  PROCESSANDO: [/bold white]", end='')
                if not car_id:
                    sleep(0.5)
                    print(bold_rainbow_text("NÃO DEIXE NADA EM BRANCO"), end="\n")
                    sleep(1)
                    continue
                
                try:
                    car_id_int = int(car_id)
                except ValueError:
                    sleep(0.5)
                    print(bold_rainbow_text("DIGITE APENAS NÚMEROS"), end="\n")
                    sleep(1)
                    continue
                
                response = cpm.unlock_car_id(car_id_int)
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                sleep(1)
                continue

            # Unlock siren id
            elif service == 12 or service == "12":
                print(bold_rainbow_text("  DIGITE O ID: "), end="")
                car_id = input()
                console.print("[bold white]  PROCESSANDO: [/bold white]", end='')
                if not car_id:
                    sleep(0.5)
                    print(bold_rainbow_text("NÃO DEIXE NADA EM BRANCO"), end="\n")
                    sleep(1)
                    continue
                
                try:
                    car_id_int = int(car_id)
                except ValueError:
                    sleep(0.5)
                    print(bold_rainbow_text("DIGITE APENAS NÚMEROS"), end="\n")
                    sleep(1)
                    continue
                
                response = cpm.unlock_siren_id(car_id_int)
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                sleep(1)
                continue
            
            # Custom torque
            elif service == 13 or service == "13":
                print(bold_rainbow_text("  DIGITE O ID: "), end="")
                car_id = input()
                print(bold_rainbow_text("  DIGITE O NOVO TORQUE: "), end="")
                new_torque = input()
                console.print("[bold white]  PROCESSANDO: [/bold white]", end='')
                if not car_id or not new_torque:
                    sleep(0.5)
                    print(bold_rainbow_text("NÃO DEIXE NADA EM BRANCO"), end="\n")
                    sleep(1)
                    continue
                
                try:
                    car_id_int = int(car_id)
                    new_torque_int = int(new_torque)
                except ValueError:
                    sleep(0.5)
                    print(bold_rainbow_text("DIGITE APENAS NÚMEROS"))
                    sleep(1)
                    continue
                
                response = cpm.set_torque(car_id_int, new_torque_int)
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                sleep(1)
                continue
            
            # Remove front parts
            elif service == 14 or service == "14":
                print(bold_rainbow_text("  DIGITE O ID: "), end='')
                car_id = input()
                console.print('[bold white]  PROCESSANDO: [/bold white]', end="")
                if not car_id:
                    sleep(0.5)
                    print(bold_rainbow_text("NÃO DEIXE NADA EM BRANCO"), end="\n")
                    sleep(1)
                    continue
                
                try:
                    car_id_int = int(car_id)
                except ValueError:
                    sleep(0.5)
                    print(bold_rainbow_text("DIGITE APENAS NÚMEROS"))
                    sleep(1)
                    continue
                
                response = cpm.remove_front_part(car_id_int)
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                sleep(1)
                continue
                
            # Remove back parts
            elif service == 15 or service == "15":
                print(bold_rainbow_text("[?] DIGITE O ID: "), end='')
                car_id = input()
                console.print('[bold white][%] PROCESSANDO: [/bold white]', end="")
                if not car_id:
                    sleep(0.5)
                    print(bold_rainbow_text("NÃO DEIXE NADA EM BRANCO"), end="\n")
                    sleep(1)
                    continue
                
                try:
                    car_id_int = int(car_id)
                except ValueError:
                    sleep(0.5)
                    print(bold_rainbow_text("DIGITE APENAS NÚMEROS"))
                    sleep(1)
                    continue
                
                response = cpm.remove_back_part(car_id_int)
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                sleep(1)
                continue
            
            # Unlock all cars max milleage
            elif service == 16 or service == "16":
                console.print("[bold white]  PROCESSANDO: [/bold white]", end="")
                response = cpm.unlock_all_cars_max_milleage()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end="\n")
                sleep(1)
                continue
            
            # Unlock car id max milleage 
            elif service == 17 or service == '17':
                print(bold_rainbow_text("  DIGITE O ID: "), end='')
                car_id = input()
                console.print('[bold white]  PROCESSANDO: [/bold white]', end='')
                if not car_id:
                    sleep(0.5)
                    print(bold_rainbow_text('NÃO DEIXE NADA EM BRANCO'), end='\n')
                    sleep(1)
                    continue
                
                try:
                    car_id_int = int(car_id)
                except ValueError:
                    sleep(0.5)
                    print(bold_rainbow_text('DIGITE APENAS NÚMEROS'), end="\n")
                    sleep(1)
                    continue
                
                response = cpm.unlock_car_id_max_milleage(car_id_int)
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end='\n')
                sleep(1)
                continue
            
            # Unlock W16
            elif service == 18 or service == '18':
                console.print('[bold white]  PROCESSANDO: [/bold white]', end='')
                response = cpm.unlock_w16()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end='\n')
                sleep(1)
                continue
            
            # Unlock horns
            elif service == 19 or service == '19':
                console.print('[bold white]  PROCESSANDO: [/bold white]', end='')
                response = cpm.unlock_horns()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end='\n')
                sleep(1)
                continue
            
            # Disable Engine Damage
            elif service == 20 or service == '20':
                console.print('[bold white]  PROCESSANDO: [/bold white]', end='')
                response = cpm.disable_engine_damage()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end='\n')
                sleep(1)
                continue
            
            # Unlimited Fuel
            elif service == 21 or service == '21':
                console.print('[bold white]  PROCESSANDO: [/bold white]', end='')
                response = cpm.unlimited_fuel()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end='\n')
                sleep(1)
                continue
            
            # Unlock House
            elif service == 22 or service == '22':
                console.print('[bold white]  PROCESSANDO: [/bold white]', end='')
                response = cpm.unlock_house()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end='\n')
                sleep(1)
                continue
                
            # Unlock Smoke
            elif service == 23 or service == '23':
                console.print('[bold white]  PROCESSANDO: [/bold white]', end='')
                response = cpm.unlock_smoke()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end='\n')
                sleep(1)
                continue
            
            # Unlock Wheels
            elif service == 24 or service == '24':
                console.print('[bold white]  PROCESSANDO: [/bold white]', end='')
                response = cpm.unlock_wheels()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end='\n')
                sleep(1)
                continue
                
            # Unlock Animations
            elif service == 25 or service == '25':
                console.print('[bold white]  PROCESSANDO: [/bold white]', end='')
                response = cpm.unlock_animations()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end='\n')
                sleep(1)
                continue
            
            # Unlock Cosmetics
            elif service == 26 or service == '26':
                console.print('[bold white]  PROCESSANDO: [/bold white]', end='')
                response = cpm.unlock_cosmetics()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end='\n')
                sleep(1)
                continue
            
            # Set Races Wins
            elif service == 27 or service == '27':
                print(bold_rainbow_text('  QUANTIDADE: '), end='')
                amount = input()
                console.print('[bold white]  PROCESSANDO: ', end='')
                if not amount:
                    sleep(0.5)
                    print(bold_rainbow_text("NÃO DEIXE NADA EM BRANCO"), end="\n")
                    sleep(1)
                    continue
                
                try:
                    amount_int = int(amount)
                except ValueError:
                    sleep(0.5)
                    print(bold_rainbow_text('DIGITE APENAS NÚMEROS'), end="\n")
                    sleep(1)
                    continue
                
                response = cpm.set_races_wins(amount_int)
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end='\n')
                sleep(1)
                continue
            
            # Set Races Loses
            elif service == 28 or service == '28':
                print(bold_rainbow_text('  QUANTIDADE: '), end='')
                amount = input()
                console.print('[bold white]  PROCESSANDO: [/bold white]', end='')
                if not amount:
                    sleep(0.5)
                    print(bold_rainbow_text("NÃO DEIXE NADA EM BRANCO"), end="\n")
                    sleep(1)
                    continue
                
                try:
                    amount_int = int(amount)
                except ValueError:
                    sleep(0.5)
                    print(bold_rainbow_text('DIGITE APENAS NÚMEROS'), end="\n")
                    sleep(1)
                    continue
                
                response = cpm.set_races_loses(amount_int)
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end='\n')
                sleep(1)
                continue
            
            # Complete All Levels
            elif service == 29 or service == '29':
                console.print("[bold white]  PROCESSANDO: ", end='')
                response = cpm.complete_all_levels()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end='\n')
                sleep(1)
                continue
            
            # Reset All Levels
            elif service == 30 or service == '30':
                console.print("[bold white]  PROCESSANDO: ", end='')
                response = cpm.reset_all_levels()
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end='\n')
                sleep(1)
                continue
            
            # Clone Cars
            elif service == 31 or service == '31':
                print(bold_rainbow_text('  EMAIL RECEBEDOR: '), end='')
                clon_email = input()
                print(bold_rainbow_text('  SENHA: '), end='')
                clon_password = input()
                console.print('[bold white]  PROCESSANDO: [/bold white]', end='')
                
                if not clon_email or not clon_password:
                    sleep(0.5)
                    print(bold_rainbow_text('NÃO DEIXE NADA EM BRANCO'), end='\n')
                    sleep(1)
                    continue
                
                response = cpm.clone_cars(clon_email, clon_password)
                print(bold_rainbow_text(response.get('message', 'INDEFINIDO')), end='\n')
                sleep(1)
                continue
            
            elif service == 00 or service == '00' or service == 0 or service == '0':
                print(bold_rainbow_text('  Saindo...'))
                sys.exit(0)
            
            else:
                print(bold_rainbow_text('  OPCÃO INVÁLIDA'))
                sleep(1)
                continue