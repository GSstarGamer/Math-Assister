def SA():
    shape1 = input("What shape to calcuate surface area? \n1 - cubiod\n2 - cylinder\nNumber or name: ")
    shape = shape1.lower()
    
    pi = 3.1415916535897743

    if shape == "cubiod" or shape == "1":
   
        print("cubiod :D")

        length1 = input("length or n: ")
        if length1 == "n":
            area1 = input("Surface area: ")
            area = float(area1)
        
        width1 = input("width or n: ")
        if width1 == "n":
            area1 = input("Surface area: ")
            area = float(area1)
        height1 = input("height or n: ")
        if height1 == "n":
            area1 = input("Surface area: ")
            area = float(area1)

        if length1 == "n":
            width = float(width1)
            height = float(height1)
        elif width1 == "n":
            length = float(length1)
            height = float(height1)
        elif height1 == "n":
            length = float(length1)
            width = float(width1)
        else:
            height = float(height1)
            width = float(width1)
            length = float(length1)
    
        if length1 == "n":
            withxheight = height * 2
            withxwidth = width * 2
            perset = 2 * (width * height)

            addofwithx = withxheight + withxwidth
            ans = (area - perset) / addofwithx
        elif width1 == "n":
            withxheight = height * 2
            withxlength = length * 2
            perset = 2 * (height * length)

            addofwithx = withxheight + withxlength
            ans = (area - perset) / addofwithx
        elif height1 == "n":
            withxwidth = width * 2
            withxlength = length * 2
            perset = 2 * (width * length)

            addofwithx = withxwidth + withxlength
            ans = (area - perset) / addofwithx
        else:
            ans = 2 * ((length * height) + (width * height) + (length * width))

            floatans = '{0:.2f}'.format(ans)
            print("Answer: "+floatans)

    elif shape == "cylinder" or shape == "2":


        print("cylinder")

        radius = float(input("Radius: "))
        height1 = input("Height or n: ")
        if height1 == "n":
            area1 = input("Surface area: ")
            area = float(area1)
        else:
            height = float(height1)

        if height1 == "n":
            ans = (area / (2 * pi * radius)) - radius
        else:
            ans = 2 * pi * radius * (radius + height)
        floatans1 = float(ans)
        floatans = '{0:.2f}'.format(ans)
        print("Answer: "+floatans)

    else:
        print("bad value")
        exit()

def nlister():

    speed = 100

    try: 
        fromn = int(input("Numbers between:"))
        ton = int(input("To: "))
    except:
        print("bad value")
        exit()



    even = []
    odd = []
    prime = []
    comp = []
    squarenum = []
    trinum = []

    def sqrt(x):
        last_guess= x/2.0
        while True:
            guess= (last_guess + x/last_guess)/2
            if abs(guess - last_guess) < .000001: # example threshold
                return guess
            last_guess= guess

    def prime_checker(number):
        
        if number == 2 or number == 3 or number==5:
            return True
        if number == 1 or number == 4:
            return False
        num = 2
        a= sqrt(number)+4 
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

    print("\n\n")    


    # ans = "Even: "+even+"\nOdd: "+odd+"\nPrime: "+prime+"\nComposite: "+comp+"\nSquare numbers: "+squarenum+"\nTriangle numbers: "+trinum
    print("Even:")
    print(even)
    print("Odd:")
    print(odd)
    print("Prime:")
    print(prime)
    print("Composite:")
    print(comp)
    print("Square Numbers:")
    print(squarenum)
    print("Triangle numbers:")
    print(trinum)
ask = input("Surface area [1]\nNumber lister [2]\n").lower()
if ask == "1":
    SA()
elif ask == "2":
    nlister()
else:
    print("Wrong answer")