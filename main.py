import platform
import shutil
import time
import os
columns = shutil.get_terminal_size().columns


logoe = """

███╗░░░███╗░█████╗░████████╗██╗░░██╗  ██╗██████╗░
████╗░████║██╔══██╗╚══██╔══╝██║░░██║  ╚═╝██╔══██╗
██╔████╔██║███████║░░░██║░░░███████║  ░░░██║░░██║
██║╚██╔╝██║██╔══██║░░░██║░░░██╔══██║  ░░░██║░░██║
██║░╚═╝░██║██║░░██║░░░██║░░░██║░░██║  ██╗██████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ╚═╝╚═════╝░"""

platform = platform.platform().split("-")[0]

def logo():
    print(logoe.center(columns))



def clear():
    if platform == "Windows":
        import os
        os.system("cls")
        logo()
    elif platform == "Linux":
        try:
            import os
            os.system("clear")
            logo()
        except:
            import replit
            replit.clear()
            logo()


def goto(loc):
    if platform == "Windows":
        os.system(f"py {loc}")
    else:
        os.system(f"python {loc}")



clear()

commands = {
    "1": "Surface area solver (Solves surface area of shapes)",
    "2": "Number lister (Lists the type of numbers with given criteria"
}

ui = ""

for num in commands:
    ui = f"{ui}\n{num} - {commands[num]}"

print(ui)

option = input("Please choice a number/name: ").lower()
if option == "1" or option == "surface area solver":
    print("Starting :D")
    time.sleep(.5)
    goto("Modules/surface-area-solver.py")
elif option == "2" or option == "number lister":
    print("Starting :D")
    time.sleep(.5)
    goto("Modules/number-lister.py")
else:
    print("Invalid option")
    exit()