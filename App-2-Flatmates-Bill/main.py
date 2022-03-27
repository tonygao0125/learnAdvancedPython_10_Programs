class Bill:
    """
    Object that contains data about a bill, such as total amount and period
    of the bill
    """

    def __init__(self, amount, period):  # attributes
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the flat and pays a share of
    the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = bill.amount/(self.days_in_house + flatmate2.days_in_house)
        to_pay = weight * self.days_in_house
        return to_pay


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as their
    names, their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass

# the_bill is an object instance of Bill class
the_bill = Bill(amount= 120, period = "March 2021")
#
john = Flatmate(name = "John", days_in_house = 30)
marry = Flatmate(name = "Mary", days_in_house= 20 )

print(john.pays(bill = the_bill, flatmate2= marry))
print(marry.pays(bill = the_bill, flatmate2 = john))