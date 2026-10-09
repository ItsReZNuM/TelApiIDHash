import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
from time import sleep
import random
import string
import sys
import os
import re

init(autoreset=True)

# Clear console
os.system('cls' if sys.platform == 'win32' else 'clear')

CONTACTS = 'Telegram: @ItsReZNuM | Instagram: ReZ.NuM | GitHub: https://github.com/ItsReZNuM'

BANNER_START = f"""{Fore.CYAN}
$$$$$$$\\            $$$$$$$$\\ $$\\   $$\\           $$\\      $$\\ 
$$  __$$\\           \\____$$  |$$$\\  $$ |          $$$\\    $$$ |
$$ |  $$ | $$$$$$\\      $$  / $$$$\\ $$ |$$\\   $$\\ $$$$\\  $$$$ |
$$$$$$$  |$$  __$$\\    $$  /  $$ $$\\$$ |$$ |  $$ |$$\\$$\\$$ $$ |
$$  __$$< $$$$$$$$ |  $$  /   $$ \\$$$$ |$$ |  $$ |$$ \\$$$  $$ |
$$ |  $$ |$$   ____| $$  /    $$ |\\$$$ |$$ |  $$ |$$ |\\$  /$$ |
$$ |  $$ |\\$$$$$$$\\ $$$$$$$$\\ $$ | \\$$ |\\$$$$$$  |$$ | \\_/ $$ |
\\__|  \\__| \\_______|\\________|\\__|  \\__| \\______/ \\__|     \\__|

    {Fore.YELLOW}ReZNuM's Tool to get API Hash and API ID of Telegram account 
"""

BANNER_SUCCESS = f"""{Fore.GREEN}
$$$$$$$\\   $$$$$$\\   $$$$$$\\  $$\\      $$\\ $$\\ 
$$  __$$\\ $$  __$$\\ $$  __$$\\ $$$\\    $$$ |$$ |
$$ |  $$ |$$ /  $$ |$$ /  $$ |$$$$\\  $$$$ |$$ |
$$$$$$$\\ |$$ |  $$ |$$ |  $$ |$$\\$$\\$$ $$ |$$ |
$$  __$$\\ $$ |  $$ |$$ |  $$ |$$ \\$$$  $$ |\\__|
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\\$  /$$ |    
$$$$$$$  | $$$$$$  | $$$$$$  |$$ | \\_/ $$ |$$\\ 
\\_______/  \\______/  \\______/ \\__|     \\__|\\__|
"""

BANNER_ERROR = f"""{Fore.RED}
 $$$$$$\\   $$$$$$\\  $$$$$$$\\  $$$$$$$\\ $$\\     $$\\       $$\\ 
$$  __$$\\ $$  __$$\\ $$  __$$\\ $$  __$$\\$$\\   $$  |      $$ |
$$ /  \\__|$$ /  $$ |$$ |  $$ |$$ |  $$ |\\$$\\ $$  /       $$ |
\\$$$$$$\\  $$ |  $$ |$$$$$$$  |$$$$$$$  | \\$$$$  /        $$ |
 \\____$$\\ $$ |  $$ |$$  __$$< $$  __$$<   \\$$  /         \\__|
$$\\   $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |   $$ |              
\\$$$$$$  | $$$$$$  |$$ |  $$ |$$ |  $$ |   $$ |          $$\\ 
 \\______/  \\______/ \\__|  \\__|\\__|  \\__|   \\__|          \\__|
"""

BROWSER_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://my.telegram.org',
    'Referer': 'https://my.telegram.org/auth',
}


def unscramble_effect(text: str, delay: float = 0.03):
    """Display text with an unscramble animation effect."""
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


def print_error(message: str, detail: str = ""):
    """Print standard error message with the ReZNuM error banner."""
    print(BANNER_ERROR)
    print(f"    {Fore.RED}[!] Error: {Fore.YELLOW}{message}")
    if detail:
        print(f"    {Fore.LIGHTBLACK_EX}Details: {detail}")
    print()


def extract_credentials(html: str, soup: BeautifulSoup):
    """
    Robust multi-layered extraction of api_id, api_hash,
    public keys, and production configuration.
    """
    api_id = None
    api_hash = None
    public_key = None
    prod_config = None

    # Layer 1: Flexible DOM search across label tags and form-groups
    labels = soup.find_all(['label', 'span', 'strong', 'td', 'th'])
    for el in labels:
        txt = el.get_text(strip=True).lower()
        parent = el.find_parent(['div', 'tr', 'fieldset']) or el

        if 'api_id' in txt and not api_id:
            val_el = parent.find(['span', 'input', 'strong', 'code'])
            if val_el:
                val = val_el.get_text(strip=True) or val_el.get('value', '')
                m = re.search(r'\b\d{5,12}\b', val)
                if m:
                    api_id = m.group(0)

        elif 'api_hash' in txt and not api_hash:
            val_el = parent.find(['span', 'input', 'strong', 'code'])
            if val_el:
                val = val_el.get_text(strip=True) or val_el.get('value', '')
                m = re.search(r'\b[0-9a-fA-F]{32}\b', val)
                if m:
                    api_hash = m.group(0)

        elif 'public key' in txt and not public_key:
            val_el = parent.find(['code', 'pre', 'span'])
            if val_el:
                public_key = val_el.get_text(strip=True)

        elif 'production configuration' in txt and not prod_config:
            val_el = parent.find(['strong', 'code', 'span'])
            if val_el:
                prod_config = val_el.get_text(strip=True)

    # Layer 2: Search elements with uneditable/selectable classes or attributes
    if not (api_id and api_hash):
        selectable = soup.find_all(lambda tag: (
            tag.name in ['span', 'input'] and (
                'this.select()' in tag.get('onclick', '')
                or 'uneditable-input' in tag.get('class', [])
                or 'form-control' in tag.get('class', [])
            )
        ))
        for item in selectable:
            val = item.get_text(strip=True) or item.get('value', '')
            if not api_id and re.fullmatch(r'\d{5,12}', val):
                api_id = val
            elif not api_hash and re.fullmatch(r'[0-9a-fA-F]{32}', val):
                api_hash = val

    # Layer 3: Direct regex fallbacks on the raw HTML
    if not api_id:
        m_id = re.search(r'api_id.*?(\b\d{5,12}\b)', html, re.I | re.S)
        if m_id:
            api_id = m_id.group(1)

    if not api_hash:
        m_hash = re.search(r'api_hash.*?(\b[0-9a-fA-F]{32}\b)', html, re.I | re.S)
        if m_hash:
            api_hash = m_hash.group(1)

    if not public_key:
        m_key = re.search(r'Public\s*keys?:.*?(-----BEGIN[^-]+-----.*?-----END[^-]+-----|<code[^>]*>(.*?)</code>)', html, re.I | re.S)
        if m_key:
            public_key = (m_key.group(1) or m_key.group(2)).strip()
            public_key = re.sub(r'<[^>]+>', '', public_key)

    if not prod_config:
        m_prod = re.search(r'Production\s*configuration:.*?<strong[^>]*>(.*?)</strong>', html, re.I | re.S)
        if m_prod:
            prod_config = m_prod.group(1).strip()

    return api_id, api_hash, public_key, prod_config


def create_telegram_app(session: requests.Session, soup: BeautifulSoup) -> bool:
    """
    Handle app creation if the account does not currently have any Telegram applications registered.
    """
    print(f"\n{Fore.YELLOW}[*] No existing Telegram App found. Automatically creating a new application...")

    hash_input = soup.find('input', {'name': 'hash'})
    if not hash_input or not hash_input.get('value'):
        print_error("Failed to find application creation CSRF token on my.telegram.org/apps.")
        return False

    csrf_hash = hash_input['value']
    rand_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    app_title = f"MyTelegramApp_{rand_suffix}"
    app_shortname = f"app{rand_suffix}"

    payload = {
        'hash': csrf_hash,
        'app_title': app_title,
        'app_shortname': app_shortname,
        'app_url': 'https://telegram.org',
        'app_platform': 'desktop',
        'app_desc': 'Personal Telegram MTProto Developer Client',
    }

    create_headers = dict(BROWSER_HEADERS)
    create_headers['Content-Type'] = 'application/x-www-form-urlencoded'
    create_headers['Referer'] = 'https://my.telegram.org/apps'

    try:
        resp = session.post('https://my.telegram.org/apps/create', data=payload, headers=create_headers, timeout=15)
        if resp.status_code == 200:
            if 'ERROR' in resp.text:
                print_error(
                    "Telegram rejected creating an application for this account.",
                    "Telegram often limits brand new accounts or flagged IPs from creating apps via automation. "
                    "Try visiting https://my.telegram.org manually in your browser to create the app once."
                )
                return False
            return True
        else:
            print_error(f"HTTP {resp.status_code} while creating application.", resp.text[:200])
            return False
    except Exception as e:
        print_error("Exception during Telegram App creation", str(e))
        return False


def main():
    print(BANNER_START)
    unscramble_effect(CONTACTS)

    phone_input = input(
        f"\n{Fore.RED}[{Fore.GREEN}+{Fore.RED}] "
        f"{Fore.GREEN}Enter your number along with country code [Ex: +98XXXXXXXXX]: {Fore.YELLOW}"
    ).strip()

    # Normalize phone number (strip spaces, ensure + prefix)
    phone_number = re.sub(r'[\s\-()]', '', phone_input)
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    if not re.match(r'^\+\d{7,15}$', phone_number):
        print_error("Invalid phone number format. Please provide a valid international number like +989123456789.")
        return

    with requests.Session() as session:
        session.headers.update(BROWSER_HEADERS)

        # Step 1: Send Password / Login Code
        print(f"\n{Fore.CYAN}[*] Requesting confirmation code from Telegram...")
        try:
            send_resp = session.post(
                'https://my.telegram.org/auth/send_password',
                data={'phone': phone_number},
                headers={'X-Requested-With': 'XMLHttpRequest'},
                timeout=15
            )
        except requests.RequestException as e:
            print_error("Network error while connecting to my.telegram.org", str(e))
            return

        if 'Sorry, too many tries. Please try again later.' in send_resp.text:
            print_error(
                "Your account is temporarily rate-limited by Telegram!",
                "Telegram limits repeated attempts. Please wait 8 to 24 hours before trying again."
            )
            return

        try:
            send_data = send_resp.json()
            random_hash = send_data.get('random_hash')
            if not random_hash:
                print_error("Telegram did not return a valid random_hash.", send_resp.text)
                return
        except Exception:
            print_error("Failed to parse response from Telegram.", send_resp.text)
            return

        print(f"{Fore.GREEN}[+] Confirmation code sent to your Telegram app!")

        # Step 2: Confirmation code input
        code = input(
            f"{Fore.RED}[{Fore.GREEN}+{Fore.RED}] "
            f"{Fore.GREEN}Enter the code sent to your Telegram account: {Fore.YELLOW}"
        ).strip()

        if not code:
            print_error("Confirmation code cannot be empty.")
            return

        login_data = {
            'phone': phone_number,
            'random_hash': random_hash,
            'password': code,
            'remember': '1'
        }

        print(f"\n{Fore.CYAN}[*] Logging in to my.telegram.org...")
        try:
            login_resp = session.post(
                'https://my.telegram.org/auth/login',
                data=login_data,
                headers={'X-Requested-With': 'XMLHttpRequest'},
                timeout=15
            )
        except requests.RequestException as e:
            print_error("Network error during login request", str(e))
            return

        login_text = login_resp.text.strip()
        if login_resp.status_code != 200 or login_text.lower() != 'true':
            # Telegram returns plain text errors on auth/login failure
            err_msg = login_text if login_text else f"HTTP status {login_resp.status_code}"
            print_error(f"Login failed: {err_msg}", "Make sure the code entered is correct and has not expired.")
            return

        print(f"{Fore.GREEN}[+] Login successful!")

        # Step 3: Access /apps page
        print(f"{Fore.CYAN}[*] Fetching API configuration page...")
        try:
            apps_page = session.get(
                'https://my.telegram.org/apps',
                headers={'Referer': 'https://my.telegram.org/'},
                timeout=15
            )
        except requests.RequestException as e:
            print_error("Network error while accessing /apps page", str(e))
            return

        # Check if redirected to login
        if '/auth' in apps_page.url or 'my_login_form' in apps_page.text:
            print_error(
                "Session was not authenticated. Redirected back to login page.",
                "Telegram may have terminated the session or required additional verification."
            )
            return

        soup = BeautifulSoup(apps_page.text, 'html.parser')

        # Check if application needs to be created
        if soup.find('form', action=re.compile(r'/apps/create')):
            created = create_telegram_app(session, soup)
            if not created:
                return
            # Refetch apps page after creation
            apps_page = session.get('https://my.telegram.org/apps', timeout=15)
            soup = BeautifulSoup(apps_page.text, 'html.parser')

        # Step 4: Extract Credentials
        api_id, api_hash, key, pc = extract_credentials(apps_page.text, soup)

        if not api_id or not api_hash:
            print_error(
                "Unable to parse API ID or API Hash from my.telegram.org.",
                "Telegram's page layout may have changed, or your account may have restrictions."
            )
            return

        # Display result
        sleep(1)
        print(BANNER_SUCCESS)
        print(f"    {Fore.CYAN}APIs successfully received:\n")
        print(f"        {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Api ID: {Fore.YELLOW}{api_id}")
        print(f"        {Fore.RED}[{Fore.GREEN}+{Fore.RED}] {Fore.GREEN}Api HASH: {Fore.YELLOW}{api_hash}")

        if key:
            print(f"\n        {Fore.RED}[{Fore.GREEN}~{Fore.RED}] {Fore.GREEN}Public Key: {Fore.YELLOW}{key}")
        if pc:
            print(f"        {Fore.RED}[{Fore.GREEN}~{Fore.RED}] {Fore.GREEN}Production configuration: {Fore.YELLOW}{pc}")

        print(f"\n{Fore.GREEN}[✔] Done! You can now use your Telegram API credentials in your projects.\n")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Process interrupted by user. Exiting...")
        sys.exit(0)
