import platform
import shutil
import time
import os
import math

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


def goto(loc):
    if platform == "Windows":
        os.system(f"py {loc}")
    else:
        os.system(f"python {loc}")

def gobac():
  input("Press enter to go back\n\n")
  goto("main.py")

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


clear()





askspeed = input("""
Speed
slow - 1 (To list big numbers)
fast - 2 (To list not so big numers)
Choice: """).lower()

speed = 100

if askspeed == "1" or askspeed == "slow":
    speed = 100000
elif askspeed == "2" or askspeed == "fast":
    speed = 100
else:
    print("bad value")
    exit()

clear()
try: 
    fromn = int(input("""
Numbers between:
"""))
    clear()
    ton = int(input(f"""
Numbers between:
{fromn} & """))
except:
    print("bad value")
    exit()




import time



import math

even = []
odd = []
prime = []
comp = []
squarenum = []
trinum = []


def prime_checker(number):
    
    if number == 2 or number == 3 or number==5:
        return True
    if number == 1 or number == 4:
        return False
    num = 2
    a= math.sqrt(number)+4 
    while a > num:
        if number % num == 0:
            return False
        else:
            num = num + 1
    return True

        
def square_checker(number):
    squares = []
    for n in range(0, speed+1):
        squares.append(n*n)
    for num in squares:
        if num == number:
            return True

def triangle_checker(n):
    tranglenums = []
    for num in range(0, speed+1):
        tr = int((num*(num+1))/2)
        tranglenums.append(tr)

    for num in tranglenums:
        if num == n:
            return True

def muliple_maker(num, min, max):
    set = []
    for numbers in range(min, max+1):
        sum = num*numbers
        if sum < max and sum > min:
            set.append(sum)
    return set



overalls = time.process_time()
for number in range(fromn, ton):
    #odd and even
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

    #prime and comp
    if prime_checker(number) == True:
        prime.append(number)
    else:
        comp.append(number)

    #square numbers
    if square_checker(number) == True:
        squarenum.append(number)

    #triangle numbers
    if triangle_checker(number) == True:
        trinum.append(number)



askm = input("Would you like multiples? [yes/no]: ").lower()

if askm == "yes":
    askto = int(input("Multiples of 2 - __ : "))
    clear()
    print()
    for muil in range(2, askto+1):
        print(f"Multiple of {muil}: {muliple_maker(muil, fromn, ton)}")
        print()

print("\n\n")    


ans = f"Even: {even}\nOdd: {odd}\nPrime: {prime}\nComposite: {comp}\nSquare numbers: {squarenum}\nTriangle numbers: {trinum}"
print(ans)

print("\n\n")

overall = time.process_time() - overalls
print(f"Time taken to solve: {overall}")

asksave = input("Whould you like to save the answer? [yes/no]: ").lower()
if asksave == "yes":
    f = open("List.txt", "w")
    f.write(ans)
    if askm == "yes":
        f.write("\n\n")
        for muil in range(2, askto+1):
            f.write(f"Multiple of {muil}: {muliple_maker(muil, fromn, ton)}\n")
    f.close()



print("Thanks for using :D")

print()

gobac()