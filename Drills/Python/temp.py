def check_temperature(temp):
    if temp < 18:
        print("Heater ON")
    elif 18 <= temp <= 25:
        print("Temperature Normal")
    else:
        print("Fan ON")

check_temperature(10)  
check_temperature(22)  
check_temperature(30)   
