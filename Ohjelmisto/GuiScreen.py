import tkinter
from tkinter import font
from tkinter import messagebox
from InputCheck import InputCheck

""" This class implements the GUI.
"""

class GuiScreen(tkinter.Frame):
    def __init__(self, master, backend_logic):
        """ In the constructor we set parameters that are needed in this GUI class.

        Args:
            Master. A tkinter.Tk master class.
            Backend_logic. Instance of backend_logic class.

        Returns: None.
        """
        super().__init__(master)
        self.backend_logic = backend_logic
        self.input_check = InputCheck()
        self.font = font.Font(family="Arial", size=12)
        self.header_font = font.Font(family="Arial", size=16)
        self.top = None
        self.bottom = None
        self.sentence_start = None
        self.firstname = None
        self.lastname = None
        self.sentence_years = None
        self.sentence_months = None
        self.remand_duration_days = None
        self.filename = "asiakkaat.csv"

    def start(self) -> None:
        """ Executes the functions that create the parts of the GUI and the GUI buttons.

        Args:
            None.

        Returns: None.
        """
        self.create_top()
        self.create_bottom()
        self.create_save_button()

    def create_top(self) -> None:
        """ Creates the top part of the GUI. Places entries for customer information.

        Args:
            None.

        Returns: None.
        """
        
        self.top = tkinter.Frame(self, bg="lightgrey", width=960, height=384)
        self.top.place(x=0, y=0)

        label_header = tkinter.Label(self.top, text="Asiakkaan tiedot", font=self.header_font, bg="lightgrey")
        label_header.place(x=350, y=25)        
    
        label_firstname = tkinter.Label(self.top, text="Etunimi:", font=self.font, bg="lightgrey")
        label_firstname.place(x=275,y=175)     
        self.firstname_entry = tkinter.Entry(self.top, width=10)
        self.firstname_entry.insert(0, "")
        self.firstname_entry.place(x=275,y=225)

        label_lastname = tkinter.Label(self.top, text="Sukunimi:", font=self.font, bg="lightgrey")
        label_lastname.place(x=525,y=175)     
        self.lastname_entry = tkinter.Entry(self.top, width=10)
        self.lastname_entry.insert(0, "")
        self.lastname_entry.place(x=525,y=225)

    def create_bottom(self) -> None:
        """ Creates the bottom part of the GUI. Places labels and entries for the sentence length.

        Args:
            None.

        Returns: None.
        """
    
        self.bottom = tkinter.Frame(self, bg="lightgrey", width=960, height=384)
        self.bottom.place(x=0, y=384)

        label_header_bottom = tkinter.Label(self.bottom, text="Asiakkaan tuomion tiedot", font=self.header_font, bg="lightgrey")
        label_header_bottom.place(x=325, y=25)  

        label_sentece_years = tkinter.Label(self.bottom, text="Tuomio vuosina:", font=self.font, bg="lightgrey")
        label_sentece_years.place(x=25,y=150)     
        self.sentece_years_entry = tkinter.Entry(self.bottom, width=10)
        self.sentece_years_entry.insert(0, "")
        self.sentece_years_entry.place(x=25,y=200)

        label_sentece_months = tkinter.Label(self.bottom, text="Tuomio kuukausina:", font=self.font, bg="lightgrey")
        label_sentece_months.place(x=175,y=150) 
        self.sentece_months_entry = tkinter.Entry(self.bottom, width=10)
        self.sentece_months_entry.insert(0, "")
        self.sentece_months_entry.place(x=175,y=200)

        label_remand_duration_days = tkinter.Label(self.bottom, text="Esitutkintavankeusaika päivinä:", font=self.font, bg="lightgrey")
        label_remand_duration_days.place(x=425,y=150) 
        self.remand_duration_days_entry = tkinter.Entry(self.bottom, width=10)
        self.remand_duration_days_entry.insert(0, "")
        self.remand_duration_days_entry.place(x=425,y=200)

        label_sentence_start = tkinter.Label(self.bottom, text="Tuomion alkamisaika:", font=self.font, bg="lightgrey")
        label_sentence_start.place(x=675,y=150) 
        self.sentence_start_entry = tkinter.Entry(self.bottom, width=10)
        self.sentence_start_entry.insert(0, "")
        self.sentence_start_entry.place(x=675,y=200)

    def create_save_button(self) -> None:
        """ Creates the save button.

        Args:
            None.

        Returns: None.
        """
        
        save_button = tkinter.Button(self.bottom, text="Talleta tiedot", font=self.font, command=lambda: self.save_data())
        save_button.place(x=375,y=300)
                

    def save_data(self) -> None:
        """ Check the data and print it to a csv file.

        Args:
            None.

        Returns: None.
        """

        self.firstname = self.firstname_entry.get()
        self.lastname = self.lastname_entry.get()

        self.sentence_years = self.sentece_years_entry.get()
        self.sentence_months = self.sentece_months_entry.get()
        self.remand_duration_days = self.remand_duration_days_entry.get()
        self.sentence_start = self.sentence_start_entry.get()

        e = None

        e = self.input_check.checkInputName(self.firstname)
        
        if e == None:
            e = self.input_check.checkInputName(self.lastname)

        if e == None:
            e = self.input_check.checkInputYears(self.sentence_years)
        
        if e == None:
            e = self.input_check.checkInputMonths(self.sentence_months)
        
        if e == None:
            e = self.input_check.checkInputDays(self.remand_duration_days)
        
        if e == None:
            e = self.input_check.checkInputStart(self.sentence_start)

        if e == None:
            e = self.backend_logic.calculate_date(self.sentence_years, self.sentence_months, self.remand_duration_days, self.sentence_start)
        if e == None:
            e = self.backend_logic.write_file(self.firstname, self.lastname, self.sentence_years, self.sentence_months, self.remand_duration_days, self.sentence_start, self.filename)

        if e == None:
            messagebox.showinfo("Talletus onnistui!", "Asiakastiedot tallennettu onnistuneesti.")
        else:
            messagebox.showerror("Virhe!", f"{e}")


        # Set fields to zero.
        self.firstname_entry.delete(0,"end")
        self.lastname_entry.delete(0,"end")

        self.sentece_years_entry.delete(0,"end")
        self.sentece_months_entry.delete(0,"end")
        self.remand_duration_days_entry.delete(0,"end")
        self.sentence_start_entry.delete(0,"end")
        

