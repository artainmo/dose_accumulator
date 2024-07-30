daily_dose = float(input("Daiy dose: "))
half_life = float(input("Half life in hours: "))
print("")

def next_day_dose(dose):
    eliminated_dose = dose / 2 / half_life * 24
    return dose - eliminated_dose

def day_to_day(accumulated_dose, day):
    print("day " + str(day) + ": " + str(accumulated_dose), end="")
    last_accumulated_dose = accumulated_dose
    leftover_dose = next_day_dose(accumulated_dose)
    accumulated_dose = daily_dose + leftover_dose
    return accumulated_dose, last_accumulated_dose

day = 1
accumulated_dose, last_accumulated_dose = day_to_day(daily_dose, day) 
print()
while last_accumulated_dose != accumulated_dose and accumulated_dose > last_accumulated_dose:
    day = day + 1
    accumulated_dose, last_accumulated_dose = day_to_day(accumulated_dose, day) 
    input("")
   

