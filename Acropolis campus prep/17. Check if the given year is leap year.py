n=int(input())

def check(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(True)
            else:
                print(False)
        else:
            print(True)
    else:
        print(False)
check(n)
