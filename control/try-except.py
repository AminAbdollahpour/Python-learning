try:
    num0 = 10/0
    num = int(input("Enter your number:"))
    print(num)
except ValueError:
    print("invalid number")
except Exception as err:
    print(err)