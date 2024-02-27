x =int(input("input the year which you have to check leapyear or not"))
if x%4==0:
    if x%100==0:
        print("not a leap year")
        if x%400==0:
            print("it's a leap year")
        else:
            ("not a #leap year")
    else:
        ("it's a leap year")
else:
    print("not a leap year")