try:

    n = int(input("how many people you want to invite to a party : "))
    if n < 10:
        for i in range(n):
            print("Enter person name ", str(i + 1), ": ")
            x = input()

            print(x, "has been invited”")

    else:
        print("Too many people ! ")
except:
    print("Error")
