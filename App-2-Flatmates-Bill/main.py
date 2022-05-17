import webbrowser
from fpdf import FPDF
import os

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

        pdf = FPDF(orientation='P', unit='pt', format='A4')

        # Create new page
        pdf.add_page()

        # Add icon
        pdf.image(name='files/house.png', w= 30, h= 30)

        # set font
        pdf.set_font(family='Arial', size=24, style='B')
        # Insert title
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Arial', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt= bill.period , border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Arial', size=12)
        pdf.cell(w=100, h=40, txt= flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt= str(flatmate1.pays(bill, flatmate2)) , border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=40, txt= flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt= str(flatmate2.pays(bill, flatmate1)) , border=0, ln=1)

        pdf.output(self.filename)

        # open the pdf file after generate the pdf-file, by using the os.system() to pass the shell command to open pdf
        # os.system("open {}".format(self.filename))

        # open the pdf file with webbrowser
        # webbrowser.get('chrome').open("file://"+ os.getcwd()+ "/"+ self.filename)
        webbrowser.get('chrome').open("file://" + os.path.realpath(self.filename))

# the_bill is an object instance of Bill class
the_bill = Bill(amount= 120, period = "April 2021")
#
john = Flatmate(name = "John", days_in_house = 30)
marry = Flatmate(name = "Mary", days_in_house= 20 )

print("John pays:", john.pays(bill = the_bill, flatmate2= marry))
print("Mary pays:", marry.pays(bill = the_bill, flatmate2 = john))

pdf_report = PdfReport(filename= 'Report1.pdf')
pdf_report.generate(flatmate1= john, flatmate2= marry, bill = the_bill)