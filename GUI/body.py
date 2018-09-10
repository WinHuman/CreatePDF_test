from tkinter import *
from tkinter.ttk import *
from fpdf import FPDF


class Application(Frame):
    def __init__(self, master):
        # initialize frame
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # add Entry
        self.entry_1 = Entry(self, width=30)
        self.entry_1.grid(column=0, row=0)
        # add Entry
        self.entry_2 = Entry(self, width=30)
        self.entry_2.grid(column=0, row=1)
        # add Entry
        self.entry_3 = Entry(self, width=30)
        self.entry_3.grid(column=0, row=2)

        # add button
        self.button = Button(self)
        self.button.grid()
        self.button["text"] = "Create PDF"
        self.button["command"] = self.createPDF
        self.button.grid(column=0, row=20)

    def createPDF(self):
        pdf = FPDF('L', 'mm', 'letter')
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        width_page = 81
        high_page = 37
        num = ''
        for i in range(width_page):
            num += '0'
        for i in range(high_page):
            pdf.multi_cell(0, 5, num)
        pdf.output('createPDF.pdf', 'F')

    # print input
    def print_food(self):
        print(self.entry.get(), var.get())


# for debug
if __name__ == "__main__":
    root = Tk()
    root.title("Lebeller")
    root.geometry("360x640")

    var = StringVar()

    app = Application(root)

    root.mainloop()