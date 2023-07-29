#I described class and saved it. Then I imported it to result.py program.
try:
    class operations():
        print("\nMathematical operations with class")

        a = int(input("First number    : "))
        b = int(input("Second number   : "))
        d = input("\nWhich operation will you do? \n1-Total 2-Extraction 3-Multiplication 4-Division ")

        if d == "1":
            c = (a + b)
        elif d == "2":
            c = (a - b)
        elif d == "3":
            c = (a * b)
        elif d == "4":
            c = (a / b)
except:
    print("Error...")
