T = int(input())
for i in range(T):
    a, b = list(input().split())
    try:
        print("{:.0f}".format(int(a)/int(b)))
    except ZeroDivisionError as error:
        print("Error Code:", error)
    except ValueError as error:
        print("Error Code:", error)
