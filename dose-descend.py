daily_dose = float(input("Daily dose: "))
days_of_use = float(input("Days of use: "))
half_life = float(input("Half life in hours: "))
print("")
if daily_dose <= 0 or days_of_use <= 0 or half_life <= 0:
    exit()

def next_day_dose(dose):
    eliminated_dose = dose / 2 / half_life * 24
    return dose - eliminated_dose

def day_to_day(accumulated_dose):
    leftover_dose = next_day_dose(accumulated_dose)
    accumulated_dose = daily_dose + leftover_dose
    return accumulated_dose

accumulated_dose = daily_dose
while days_of_use - 1 > 0:
    days_of_use = days_of_use - 1
    accumulated_dose = day_to_day(accumulated_dose) 
    input("")
   
day = 1
while accumulated_dose > daily_dose/100:
    print("Day " + str(day) + ": " + str(accumulated_dose))
    day = day + 1
    accumulated_dose = next_day_dose(accumulated_dose)
