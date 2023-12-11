import time
import random
from colorama import init, Fore, Style

init(autoreset=True)

def clear_console():
    print("\033c", end="")

def print_banner():
    banner = f"""
{Fore.MAGENTA}
        ███████╗██████╗ ██╗███████╗███████╗ █████╗ ███████╗███████╗
        ██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝   ~ eDisease ~
        █████╗  ██║  ██║██║███████╗█████╗  ███████║███████╗█████╗  
        ██╔══╝  ██║  ██║██║╚════██║██╔══╝  ██╔══██║╚════██║██╔══╝  
        ███████╗██████╔╝██║███████║███████╗██║  ██║███████║███████╗   ~ https://discord.gg/edisease ~
        ╚══════╝╚═════╝ ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝
{Fore.RESET}
    """
    print(banner)

def generate_code():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    return "https://discord.gift/" + ''.join(random.choice(letters) for _ in range(16))

def main():
    clear_console()
    print_banner()

    first_iteration = True
    for i in range(99999):
        time.sleep(random.uniform(4, 5))

        code = generate_code()
        if first_iteration:
            print(f"{Fore.RED}Invalid  > {Fore.MAGENTA}{code}")
            first_iteration = False
        elif random.random() < 0.0001:  # Adjusted to make "Vaild" even rarer
            print(f"\n{Fore.GREEN}Vaild  > {Fore.MAGENTA}{code}")
        else:
            print(f"{Fore.RED}Invalid  > {Fore.MAGENTA}{code}")

if __name__ == "__main__":
    main()
