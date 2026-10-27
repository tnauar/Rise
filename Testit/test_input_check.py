from InputCheck import InputCheck

class TestInputCheck:

    def setup_method(self):
        # Bypass tkinter.Frame initialization; the methods under test need no
        # widget state.
        self.input_check = InputCheck.__new__(InputCheck)

    def test_check_input_name(self):
         
        assert self.input_check.checkInputName(" ") == "Nimessä täytyy olla kirjaimia."
        assert self.input_check.checkInputName("Äö-å") is None
        assert self.input_check.checkInputName("aaaaaaaaaa-aaaaaaaaaa-aaaaaaaaaa-aaaaaaaaaa-aaaaaaaaaa-aaaaaaaaaa-aaaaaaaaaa-aaaaaaaaaa-aaaaaaaaaa-aaaaaaaaaa") == "Nimi on liian pitkä. 100 merkkiä on maksimipituus."
        assert self.input_check.checkInputName("?teppo3") == "Virheellisiä merkkejä nimessä. Vain kirjaimet ja väliviiva ovat hyväksyttyjä." 

    def test_check_input_years(self):
        
        assert self.input_check.checkInputYears(1.5) == "Vuosien täytyy olla kokonaisluku."
        assert self.input_check.checkInputYears("Vuosi") == "Vuosien täytyy olla kokonaisluku."
        assert self.input_check.checkInputYears(6) is None
        assert self.input_check.checkInputYears(-1) == "Vuosien täytyy olla välillä 0-100."
        assert self.input_check.checkInputYears(101) == "Vuosien täytyy olla välillä 0-100."
        
    def test_check_input_months(self):
        
        assert self.input_check.checkInputMonths(1.5) == "Kuukausien täytyy olla kokonaisluku."
        assert self.input_check.checkInputMonths("Kuukausi") == "Kuukausien täytyy olla kokonaisluku."
        assert self.input_check.checkInputMonths(4) is None
        assert self.input_check.checkInputMonths(-1) == "Kuukausien täytyy olla välillä 0-11."
        assert self.input_check.checkInputMonths(12) == "Kuukausien täytyy olla välillä 0-11."

    def test_check_input_days(self):
        
        assert self.input_check.checkInputDays(1.5) == "Päivien täytyy olla kokonaisluku."
        assert self.input_check.checkInputDays("päivä") == "Päivien täytyy olla kokonaisluku."
        assert self.input_check.checkInputDays(64) is None
        assert self.input_check.checkInputDays(-1) == "Päivien täytyy olla välillä 0-3650."
        assert self.input_check.checkInputDays(3651) == "Päivien täytyy olla välillä 0-3650."

    def test_check_input_start(self):
        
        assert self.input_check.checkInputStart("0") == "Päivämäärän täytyy olla muotoa VVVV-KK-PP. Esim. 2024-06-29."
        assert self.input_check.checkInputStart("Päivämäärä") == "Päivämäärän täytyy olla muotoa VVVV-KK-PP. Esim. 2024-06-29."
        assert self.input_check.checkInputStart("2024-05-17") is None
        assert self.input_check.checkInputStart("2020-05-32") == "Päivän täytyy olla välillä 0-31."
        #assert self.input_check.checkInputStart("2020--1-17") == "Kuukauden täytyy olla välillä 0-12."
        assert self.input_check.checkInputStart("2020-13-17") == "Kuukauden täytyy olla välillä 0-12."
        assert self.input_check.checkInputStart("1925-05-17") == "Vuoden täytyy olla välillä 1926-3026."
        assert self.input_check.checkInputStart("3027-05-17") == "Vuoden täytyy olla välillä 1926-3026."
     

