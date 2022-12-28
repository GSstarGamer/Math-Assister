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
╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ╚═╝╚═════╝░\n"""

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

def cls():
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

pi = math.pi

cls()

shape1 = input("What shape to calcuate surface area? \n1 - cubiod\n2 - cylinder\nNumber or name: ")
shape = shape1.lower()



if shape == "cubiod" or shape == "1":
  cls()
  print(f"""What shape to calcuate surface area? 
**1 - cubiod**
2 - cylinder
Number or name: {shape} 
""")

  length1 = input("length (if no value given then type 'none'): ")
  if length1 == "none":
    area1 = input("Surface area: ")
    area = float(area1)
  
  width1 = input("width (if no value given then type 'none'): ")
  if width1 == "none":
    area1 = input("Surface area: ")
    area = float(area1)
  height1 = input("height (if no value given then type 'none'): ")
  if height1 == "none":
    area1 = input("Surface area: ")
    area = float(area1)

  if length1 == "none":
    width = float(width1)
    height = float(height1)
  elif width1 == "none":
    length = float(length1)
    height = float(height1)
  elif height1 == "none":
    length = float(length1)
    width = float(width1)
  else:
    height = float(height1)
    width = float(width1)
    length = float(length1)
  
  if length1 == "none":
    withxheight = height * 2
    withxwidth = width * 2
    perset = 2 * (width * height)

    addofwithx = withxheight + withxwidth
    ans = (area - perset) / addofwithx
  elif width1 == "none":
    withxheight = height * 2
    withxlength = length * 2
    perset = 2 * (height * length)

    addofwithx = withxheight + withxlength
    ans = (area - perset) / addofwithx
  elif height1 == "none":
    withxwidth = width * 2
    withxlength = length * 2
    perset = 2 * (width * length)

    addofwithx = withxwidth + withxlength
    ans = (area - perset) / addofwithx
  else:
    ans = 2 * ((length * height) + (width * height) + (length * width))

  floatans = '{0:.2f}'.format(ans)
  print(f"Answer: {floatans}")

elif shape == "cylinder" or shape == "2":

  cls()
  print(f"""What shape to calcuate surface area? 
1 - cubiod
**2 - cylinder**
Number or name: {shape} 
""")

  radius = float(input("Radius: "))
  height1 = input("Height (if no value given then type 'none'): ")
  if height1 == "none":
    area1 = input("Surface area: ")
    area = float(area1)
  else:
    height = float(height1)

  if height1 == "none":
    ans = (area / (2 * pi * radius)) - radius
  else:
    ans = 2 * pi * radius * (radius + height)
  floatans1 = float(ans)
  floatans = '{0:.2f}'.format(ans)
  print(f"Answer: {floatans}")

else:
  print("bad value")
  exit()

print("Thanks for using :D")

print()

gobac()