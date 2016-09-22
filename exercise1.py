name = raw_input('What is your name? ')
print "Hello, " + name + "!"

name = raw_input('WHAT IS YOUR NAME? ')
name = name.upper()
print "HELLO, " + name + "!"

numLetters = len(name)

numStr = str(numLetters)

print "YOUR NAME HAS " + numStr + " LETTERS IN IT! AWESOME!"


print "__name___ would love to be crusing in a ___car___ right now!"

name = (raw_input("What's your name? "))
car = (raw_input("Whats your favorite car? "))

print name + " would love to be crusing in a " + car + " right now!"

day = int(raw_input("What day is it in a number? 0 equals Sunday: "))

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

today = week[day]
print today

if today == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
    print "Its " + today + ". Go to work!"

else:
    print "Yay! It's the weekend!"

celsius= int(raw_input("What is the temperature in Celsius? "))
fahrenheit = str(float(celsius * 9 / 5 + 32))
print fahrenheit + " F"

bill = float(raw_input("Total bill amount?: "))

serviceLvl = raw_input("How was the service? Good, bad or fair: ")

serviceLvl = serviceLvl.lower()

badFloat = (bill / 10)
goodFloat = (bill / 5)
fairFloat = (bill * .15)


if serviceLvl == "good":
    print "Tip amount: %.2f" % goodFloat
elif serviceLvl == "fair":
    print "Tip amount: %.2f" % fairFloat
else:
    print "Tip amount: %.2f" % badFloat


def tip():
    if serviceLvl == "good":
        return goodFloat
    elif serviceLvl == "fair":
        return fairFloat
    else:
        return badFloat


total = bill + tip()

print "Total bill amount: $%.2f" % total

splitHow = int((raw_input("Split how many ways?: ")))

amountPerPerson = total / splitHow

print "Amount per person: $%.2f" % amountPerPerson
