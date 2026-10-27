import tkinter as tk
from tkinter import messagebox
import re

class InputCheck(tk.Frame):
    def __init__(self):
        pass

    def checkInputName(self, name:str) -> str:
        """ This function will check that the names given in GUI are valid.

        Args:
            name. A String indicating a firstname or lastname.

        Returns: A string "None" if everything went OK. Returns a string containing error information if something went wrong. 
        """
        e = None
        NAME_REGEX = re.compile(r"^[A-Za-zÅÄÖåäö]+(?:[ -][A-Za-zÅÄÖåäö]+)*$")

        if not name or not name.strip():
            return "Nimessä täytyy olla kirjaimia."
        if not NAME_REGEX.fullmatch(name.strip()):
            return "Virheellisiä merkkejä nimessä. Vain kirjaimet ja väliviiva ovat hyväksyttyjä."
        if len(name) > 100:
            return "Nimi on liian pitkä. 100 merkkiä on maksimipituus."

        return e


    def checkInputYears(self, years:int) -> str:
        """ This function will check that the sentence years given in GUI is valid.

        Args:
            years. A integer indicating sentence years.

        Returns: A string "None" if everything went OK. Returns a string containing error information if something went wrong.
        """
        e = None
        try:
            if isinstance(years, float) and not years.is_integer():
                return "Vuosien täytyy olla kokonaisluku."
            years_value = int(years)
        except ValueError:
            return "Vuosien täytyy olla kokonaisluku."

        if years_value < 0 or years_value > 100:
            return "Vuosien täytyy olla välillä 0-100."

        return e

    def checkInputMonths(self, months:int) -> str:
        """ This function will check that the sentence months given in GUI is valid.

        Args:
            months. A integer indicating sentence months.

        Returns: A string "None" if everything went OK. Returns a string containing error information if something went wrong.
        """
        e = None
        try:
            if isinstance(months, float) and not months.is_integer():
                return "Kuukausien täytyy olla kokonaisluku."
            months_value = int(months)
        except ValueError:
            return "Kuukausien täytyy olla kokonaisluku."

        if months_value < 0 or months_value > 11:
            return "Kuukausien täytyy olla välillä 0-11."

        return e

    def checkInputDays(self, days:int) -> str:
        """ This function will check that the remand days given in GUI is valid.

        Args:
            days. An integer indicating remand days.

        Returns: A string "None" if everything went OK. Returns a string containing error information if something went wrong. 
        """
        e = None
        try:
            if isinstance(days, float) and not days.is_integer():
                return "Päivien täytyy olla kokonaisluku."
            days_value = int(days)
        except ValueError:
            return "Päivien täytyy olla kokonaisluku."

        if days_value < 0 or days_value > 3650:
            return "Päivien täytyy olla välillä 0-3650."

        return e 

    def checkInputStart(self, start:str) -> str:
        """ This function will check that the sentence start date given in GUI is valid.

        Args:
            start. Sentence start date in the format of YYYY-MM-DD.

        Returns: A string "None" if everything went OK. Returns a string containing error information if something went wrong. 
        """
        e = None

        try:
            year, month, day = map(int, start.split("-"))
        except ValueError:
            return "Päivämäärän täytyy olla muotoa VVVV-KK-PP. Esim. 2024-06-29."

        if day < 0 or day > 31:
            return "Päivän täytyy olla välillä 0-31."
        if month < 0 or month > 12:
            return "Kuukauden täytyy olla välillä 0-12."
        if year < 1926 or year > 3000:
            return "Vuoden täytyy olla välillä 1926-3026."
        
        return e 