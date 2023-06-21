import time

import art
from colorama import init,Fore
import pyautogui as boomer
import argparse

init()
print(Fore.RED + art.text2art("Boom!"))
print(Fore.GREEN + "By : " + Fore.GREEN + "Mbale Prince || Hacker404\n")

parser = argparse.ArgumentParser()
parser.add_argument('--message',type=str,required=True)
parser.add_argument('--limit',type=int,required=True)
parser.add_argument('--time',type=int,required=True)
args = parser.parse_args()
args1 = parser.parse_args()
args2 = parser.parse_args()

print(Fore.RED + "[Warning]" + Fore.GREEN + "You are about to Boom!!!" + Fore.RED + "\nPRESS CTRL + C TO TERMINATE PROCESS")
print(Fore.RED + "[Info]" + Fore.GREEN + "Getting ready to boom!!!")
i = 0
limit = args1.limit
message = args.message
times = args2.time

time.sleep(times)
print(Fore.RED + "[Info]" + Fore.GREEN + "Now booming!!!")
while i < int(limit):
    boomer.typewrite(message)
    boomer.press("enter")
    i+=1
print(Fore.RED + "[Warning]" + Fore.GREEN + "Booming successful!!!")
print(Fore.RED + "[Info]" + Fore.GREEN + "Now exiting!!!")
