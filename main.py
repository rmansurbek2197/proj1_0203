#1
oy = int(input("Oy raqamini kiriting (1-12): "))

match oy:
    case 12 | 1 | 2:
        print("Qish")
    case 3 | 4 | 5:
        print("Bahor")
    case 6 | 7 | 8:
        print("Yoz")
    case 9 | 10 | 11:
        print("Kuz")
    case _:
        print("Noto'g'ri oy raqami")

#2
a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))
amal = input("Amalni kiriting (+, -, *, /, //, %, **): ")

match amal:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b if b != 0 else "0 ga bo‘lib bo‘lmaydi")
    case "//":
        print(a // b if b != 0 else "0 ga bo‘lib bo‘lmaydi")
    case "%":
        print(a % b if b != 0 else "0 ga bo‘lib bo‘lmaydi")
    case "**":
        print(a ** b)
    case _:
        print("Noto‘g‘ri amal")

#3
ball = int(input("Balingizni kiriting (0-100): "))

match ball:
    case b if 90 <= b <= 100:
        print("A")
    case b if 80 <= b <= 89:
        print("B")
    case b if 70 <= b <= 79:
        print("C")
    case b if 60 <= b <= 69:
        print("D")
    case b if 0 <= b <= 59:
        print("F")
    case _:
        print("Noto‘g‘ri ball")
