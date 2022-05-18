import os
import webbrowser
from fpdf import FPDF


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

        # change working directory to files
        os.chdir("files")
        pdf.output(self.filename)

        # open the pdf file after generate the pdf-file, by using the os.system() to pass the shell command to open pdf
        # os.system("open {}".format(self.filename))

        # open the pdf file with webbrowser
        # webbrowser.get('chrome').open("file://"+ os.getcwd()+ "/"+ self.filename)
        webbrowser.get('chrome').open("file://" + os.path.realpath(self.filename))