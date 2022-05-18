from flat import Bill, Flatmate
from reports import PdfReport

# let user key in the parameters
input_amount = float(input("Hey user, please enter the bill amount: "))
input_period = input("What is the bill period? E.g. December_2020: ")

# the_bill is an object instance of Bill class
the_bill = Bill(amount= input_amount, period = input_period)

# Flatmate object instance
flatmate1_name = input("What is the name of the first flatmate? ")
flatmate1_days = int(input(f"How many days did {flatmate1_name} stay in the house during the bill period? "))
flatmate2_name = input("What is the name of the second flatmate? ")
flatmate2_days = int(input(f"How many days did {flatmate2_name} stay in the house during the bill period? "))

flatmate1 = Flatmate(name = flatmate1_name, days_in_house = flatmate1_days)
flatmate2 = Flatmate(name = flatmate2_name, days_in_house= flatmate2_days)

print(f"{flatmate1_name} pays:", flatmate1.pays(bill = the_bill, flatmate2= flatmate2))
print(f"{flatmate2_name} pays:", flatmate2.pays(bill = the_bill, flatmate2 = flatmate1))

pdf_report = PdfReport(filename=f"{input_period}.pdf")
pdf_report.generate(flatmate1= flatmate1, flatmate2= flatmate2, bill = the_bill)