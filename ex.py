temperatures = []

for i in range(5):
    temp = float(input(f"Enter temperature reading {i + 1}: "))
    temperatures.append(temp)

    if temp > 30:
        print("Pump ON")
    else:
        print("Pump OFF")

    if temp > 40:
        print("ALERT: Temperature exceeds 40°C!")

average_temp = sum(temperatures) / len(temperatures)

print("\nTemperature Readings:", temperatures)
print(f"Average Temperature: {average_temp:.2f}°C")