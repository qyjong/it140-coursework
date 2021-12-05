input_month = input()
input_day = int(input())

if not (input_month in ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]) or  not (0 < input_day < 32):
        print("Invalid")
else:
    if input_month == "March":
        if input_day < 20:
            print("Winter")
        else:
            print("Invalid")
    elif input_month in ["April", "May"]:
        print("Spring")
    elif input_month == "June":
        if input_day < 21:
            print("Spring")
        elif input_day < 31:
            print("Summer")
        else:
            print("Invalid")
    elif input_month in ["July", "August"]:
        print("Summer")
    elif input_month == "September":
        if input_day < 22:
            print("Summer")
        elif input_day < 31:
            print("Autumn")
        else:
            print("Invalid")
    elif input_month in ["October", "November"]:
        print("Autumn")
    elif input_month == "December":
        if input_day < 21:
            print("Autumn")
        else:
            print("Winter")
    elif input_month in ["January", "February"]:
        print("Winter")
        