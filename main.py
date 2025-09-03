den='[1;90m'
luc='[1;32m'
trang='[1;37m'
red='[1;31m'
vang='[1;33m'
tim='[1;35m'
lamd='[1;34m'
lam='[1;36m'
purple='\331[35m'
hong='[1;95m'
lam = "\033[1;36m"
hong = "\033[1;95m"
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
xnhac = "\033[1;36m"

thanh_xau=trang+'~'+red+'['+vang+'HKT'+red+'] '+trang+'➩ '+luc
thanh_dep=trang+'~'+red+'['+luc+'HKT'+red+'] '+trang+'➩ '+luc

import requests,json,os,sys
from sys import platform
from datetime import datetime        
from time import sleep,strftime
try:from pystyle import Add,Center,Anime,Colors,Colorate,Write,System
except:os.system('pip install pystyle','pip install bs4', 'pip install requests', 'pip install colorama', 'pip install beautifulsoup4', 'pip install Anime', 'pip install webdriver_manager', 'pip install selenium ', 'pip install mechanize'); from pystyle import Add,Center,Anime,Colors,Colorate,Write,System

banners=f"""
                                ╔═══════════════════════════════════════════╗           
                                ███╗  ██╗ █████╗ ██╗  ██╗██╗████████╗ ██████╗ 
                                ██║  ██║██╔══██╗██║ ██╔╝██║╚══██╔══╝██╔═══██╗ 
                                ███████║███████║█████╔╝ ██║   ██║   ██║   ██║ 
                                ██╔══██║██╔══██║██╔═██╗ ██║   ██║   ██║   ██║ 
                                ██║  ██║██║  ██║██║  ██╗██║   ██║   ╚██████╔╝ 
                                ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝    ╚═════╝║
                                ║➢ Admin      : HAKITO                      ║                     
                                ║➢ Telegram   : @HakitoVN                   ║                       
                                ║➣ Youtube    : None                            ║                          
                                ║➣ TIKTOK     : None                        ║                       
                                ╚═══════════════════════════════════════════╝
"""
thongtin=f"""
Vượt Link Để lấy Key Free : key có hiệu lục trong 20h
⚠ trong lúc dùng tool không đổi ip mạng
"""

def lovec25(so):
    a='────'*so
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.003)
    print()

def clear():
    if platform[0:3]=='lin':
        os.system('clear')
    else:
        os.system('cls')

def banner():
    print('[0m',end='')
    clear()
    a=Colorate.Horizontal(Colors.blue_to_green,banners)
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
    print()
    print(thongtin)

banner()

print(f"""{luc}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃   {vang}Tool GOLIKE   {vang}      ┃
{lam}┗━━━━━━━━━━━━━━━━━━━━━━━┛ """)
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}1.1{lam}] {lam}Tool Golike TikTok [ADR]')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}2.1{lam}] {lam}Tool Golike Instagram')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.1{lam}] {lam}Tool Golike Auto Tiktok v1')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}4.1{lam}] {lam}Tool Golike Auto Twitter')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}5.1{lam}] {lam}Tool Golike Auto Threads')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}6.1{lam}] {lam}Tool Golike Auto Snapchat V1')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}7.1{lam}] {lam}Tool Golike Auto Snapchat V2')

print(f'{luc}{lam}────────────────────────────────────────────────────────')
print(f"""{luc}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃  {vang}Tool TRAO DOI SUB    {vang}┃
{lam}┗━━━━━━━━━━━━━━━━━━━━━━━┛""")
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}8.1{lam}] {lam}Tool Cày Xu TDS Tiktok 1')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}9.1{lam}] {lam}Tool Cày Xu TDS tiktok 2')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}10.1{lam}] {lam}Tool Cày Xu TDS Instagram')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}11.1{lam}] {lam}Tool Cày Xu TDS Facebook')
print(f'{luc}{lam}────────────────────────────────────────────────────────')
print(f"""{luc}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃   {vang}Tool TUONG TAC CHEO {vang}┃
{lam}┗━━━━━━━━━━━━━━━━━━━━━━━┛""")
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}12.1{lam}] {lam}Tool Cày Xu TTC Facebook')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}13.1{lam}] {lam}Tool Cày Xu TTC INSTAGRAM')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}14.1{lam}] {lam}Tool Cày Xu TTC Facebook v2')
print(f'───────────────────────────────────────────────────────────────────')
chon = input(
        '\033[1;31m[\033[1;37mHKT\033[1;31m] \033[1;37m=> \033[1;32mNHẬP\033[1;37m =>: \033[1;33m'
    )
if   chon == "1.1":
    exec(requests.get('https://raw.githubusercontent.com/Hakito0909/HAKITO-VN/refs/heads/main/1.1.py').text)
elif chon == "2.1":
    exec(requests.get('https://raw.githubusercontent.com/Hakito0909/HAKITO-VN/refs/heads/main/2.1.py').text)
elif chon == "3.1":
    exec(requests.get('https://raw.githubusercontent.com/Hakito0909/HAKITO-VN/refs/heads/main/3.1.py').text)
elif chon == "4.1":
    exec(requests.get('https://raw.githubusercontent.com/Hakito0909/HAKITO-VN/refs/heads/main/4.1.py').text)
elif chon == "5.1":
    exec(requests.get('https://raw.githubusercontent.com/Hakito0909/HAKITO-VN/refs/heads/main/5.1.py').text)
elif chon == "6.1":
    exec(requests.get('https://raw.githubusercontent.com/Hakito0909/HAKITO-VN/refs/heads/main/6.1.py').text)
elif chon == "7.1":
    exec(requests.get('https://raw.githubusercontent.com/Hakito0909/HAKITO-VN/refs/heads/main/14.1.py').text)
elif chon == "8.1":
    exec(requests.get('https://raw.githubusercontent.com/Hakito0909/HAKITO-VN/refs/heads/main/8.1.py').text)
elif chon == "9.1":
    exec(requests.get('https://raw.githubusercontent.com/Hakito0909/HAKITO-VN/refs/heads/main/9.1.py').text)
elif chon == "10.1":
    exec(requests.get('https://raw.githubusercontent.com/Hakito0909/HAKITO-VN/refs/heads/main/10.1.py').text) 
elif chon == "11.1":
    exec(requests.get('https://raw.githubusercontent.com/Hakito0909/HAKITO-VN/refs/heads/main/11.1.py').text) 
elif chon == "12.1":
    exec(requests.get('https://raw.githubusercontent.com/Hakito0909/HAKITO-VN/refs/heads/main/12.1.py').text) 
elif chon == "13.1":
    exec(requests.get('https://raw.githubusercontent.com/Hakito0909/HAKITO-VN/refs/heads/main/13.1.py').text)
elif chon == "14.1":
    exec(requests.get('https://raw.githubusercontent.com/Hakito0909/HAKITO-VN/refs/heads/main/14.1.py').text)     

exit(print("Lựa chọn sai"))