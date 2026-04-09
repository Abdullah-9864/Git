while True:
    moisture= int(input("Enter moisture (0-100,-1 to quit):  "))
    if moisture ==-1 :
        break
    elif moisture < 0 or moisture >100:
        print("input is invalid")
        # continue
    elif moisture <= 30 :
        print("DRY")
    elif moisture <= 70:
        print("moderate")
    elif moisture <=100 :
        print ("wet")