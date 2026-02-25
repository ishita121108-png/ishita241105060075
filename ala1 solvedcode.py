print("Weather Report")
cities = ["Delhi", "Mumbai", "Pune"]
temps = [30, 32, 28]
city = input("Enter city: ")
if city in cities:
    index = cities.index(city)
    if temps[index] > 25:
        status = "Hot"
    else:
        status = "Cool"
    print("City:", city)
    print("Temperature:", temps[index])
    print("Status:", status)
    for i in range(3):
        print("Checked")
    print("End")
else:
    print("City not found")