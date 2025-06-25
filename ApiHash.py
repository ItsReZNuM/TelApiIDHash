import requests
from bs4 import BeautifulSoup
from colorama import Fore, init
from time import sleep
import random
import sys

init(autoreset=True)

CONTACTS = 'Telegram: @ItsReZNuM | Instagram: ReZ.NuM | GitHub: https://github.com/ItsReZNuM'

def unscramble_effect(text, delay=0.05):
    """Display text with an unscramble effect."""
    chars = list(text)
    displayed = [' ' for _ in chars]
    indices = list(range(len(chars)))
    random.shuffle(indices)
    
    for i in indices:
        displayed[i] = chars[i]
        sys.stdout.write('\r' + Fore.LIGHTGREEN_EX + ''.join(displayed))
        sys.stdout.flush()
        sleep(delay)
    print()

print(f"""{Fore.CYAN}


$$$$$$$\            $$$$$$$$\ $$\   $$\           $$\      $$\ 
$$  __$$\           \____$$  |$$$\  $$ |          $$$\    $$$ |
$$ |  $$ | $$$$$$\      $$  / $$$$\ $$ |$$\   $$\ $$$$\  $$$$ |
$$$$$$$  |$$  __$$\    $$  /  $$ $$\$$ |$$ |  $$ |$$\$$\$$ $$ |
$$  __$$< $$$$$$$$ |  $$  /   $$ \$$$$ |$$ |  $$ |$$ \$$$  $$ |
$$ |  $$ |$$   ____| $$  /    $$ |\$$$ |$$ |  $$ |$$ |\$  /$$ |
$$ |  $$ |\$$$$$$$\ $$$$$$$$\ $$ | \$$ |\$$$$$$  |$$ | \_/ $$ |
\__|  \__| \_______|\________|\__|  \__| \______/ \__|     \__|
                                                                                                            
                                                               
                                                                   
                                                                      
                                                                      
    {Fore.YELLOW}ReZNuM's Tool to get API Hash and API ID of Telegram account 
""")
unscramble_effect(CONTACTS)

Phone = input(f"{Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Enter your number along with the country code [Ex : +98XXXXXX]: {Fore.RED}")
with requests.Session() as req:
    phone_number = Phone

    login0 = req.post('https://my.telegram.org/auth/send_password', data={'phone': phone_number})

    if 'Sorry, too many tries. Please try again later.' in login0.text:
        print(f'{Fore.RED}Your account has been banned!\n Please try again in 8 hours ')
        exit()

    login_data = login0.json()
    random_hash = login_data['random_hash']

    code = input(f'{Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Send the code sent in the Telegram account: {Fore.RED}')

    login_data = {
        'phone': phone_number,
        'random_hash': random_hash,
        'password': code
    }

    login = req.post('https://my.telegram.org/auth/login', data=login_data)

    apps_page = req.get('https://my.telegram.org/apps')
    soup = BeautifulSoup(apps_page.text, 'html.parser')
    try:
        api_id = soup.find('label', string='App api_id:').find_next_sibling('div').select_one('span').get_text()
        api_hash = soup.find('label', string='App api_hash:').find_next_sibling('div').select_one('span').get_text()
        key = soup.find('label', string='Public keys:').find_next_sibling('div').select_one('code').get_text()
        Pc = soup.find('label', string='Production configuration:').find_next_sibling('div').select_one('strong').get_text()
        sleep(3)
        print(f"""{Fore.GREEN}

$$$$$$$\   $$$$$$\   $$$$$$\  $$\      $$\ $$\ 
$$  __$$\ $$  __$$\ $$  __$$\ $$$\    $$$ |$$ |
$$ |  $$ |$$ /  $$ |$$ /  $$ |$$$$\  $$$$ |$$ |
$$$$$$$\ |$$ |  $$ |$$ |  $$ |$$\$$\$$ $$ |$$ |
$$  __$$\ $$ |  $$ |$$ |  $$ |$$ \$$$  $$ |\__|
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$  /$$ |    
$$$$$$$  | $$$$$$  | $$$$$$  |$$ | \_/ $$ |$$\ 
\_______/  \______/  \______/ \__|     \__|\__|
                                               
                                               
                                               


    {Fore.CYAN}APIs successfully received:

        {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Api ID: {Fore.YELLOW}{api_id}
        {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Api HASH: {Fore.YELLOW}{api_hash}
        
        {Fore.RED}[{Fore.GREEN}~{Fore.RED}] {Fore.GREEN}Public Key: {Fore.YELLOW}{key}
        {Fore.RED}[{Fore.GREEN}~{Fore.RED}] {Fore.GREEN}Production configuration: {Fore.YELLOW}{Pc}
        
    """)
    except:
        print(f'''{Fore.RED}
              
              
 $$$$$$\   $$$$$$\  $$$$$$$\  $$$$$$$\ $$\     $$\       $$\ 
$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\\$$\   $$  |      $$ |
$$ /  \__|$$ /  $$ |$$ |  $$ |$$ |  $$ |\$$\ $$  /       $$ |
\$$$$$$\  $$ |  $$ |$$$$$$$  |$$$$$$$  | \$$$$  /        $$ |
 \____$$\ $$ |  $$ |$$  __$$< $$  __$$<   \$$  /         \__|
$$\   $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |   $$ |              
\$$$$$$  | $$$$$$  |$$ |  $$ |$$ |  $$ |   $$ |          $$\ 
 \______/  \______/ \__|  \__|\__|  \__|   \__|          \__|
                                                             
                                                             
                                                             

              
              
              It is not possible to get APIs for you!\nIn the next update, this bug will be fixed!''')