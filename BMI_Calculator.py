# Kalkulatror BMI
wzrost = float(input("Jaki masz wzrost (w metrach):" ))
waga = float(input("Ile ważysz (w kg)"))
bmi =  waga/(wzrost ** 2)
print("Twoje BMI wynosi:", round(bmi, 2))