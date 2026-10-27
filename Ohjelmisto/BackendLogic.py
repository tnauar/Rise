import csv
from datetime import date, datetime, timedelta
import calendar

class BackendLogic():
    def __init__(self) -> None:
        """ Constructor where the sentence_end_date_defined.

        Args:
            None.

        Returns: None.
        """
        self.sentence_end_date = None
               
    def calculate_date(self, sentence_years:int, sentence_months:int, remand_days:int, sentence_start:str) -> str:
        """ Calculates the sentence end date.

        Args:
            sentence_years. The length of the sentence in years.
            sentence_months. The length of the sentence in months.
            remand_days. The length of the remand in days.
            sentence_start. Sentence start date in the format YYYY-MM-DD

        Returns: A string "None" if everything went OK. Returns a string containing error information if something went wrong.
        """

        e = None
        
        year, month, day = map(int, sentence_start.split("-"))

        sentence_years = int(sentence_years)
        sentence_months = int(sentence_months)
        remand_days = int(remand_days)

        total_months = (year * 12 + (month-1)) + (sentence_years * 12 + sentence_months)
        new_year = total_months // 12
        new_month = total_months % 12 + 1

        last_day = calendar.monthrange(new_year, new_month)[1]
        new_day = min(day, last_day)

        end_date_wo_remand = date(new_year, new_month, new_day).isoformat()
        end_date = datetime.strptime(end_date_wo_remand, "%Y-%m-%d").date()
        self.sentence_end_date = end_date - timedelta(days = remand_days)

        return e

    def write_file(self, firstname:str, lastname:str, sentence_years:int, sentence_months:int, remand_days:int, sentence_start:str) -> str:
        """ Writes the customer data to a csv file. 

        Args:
            firstname. Customer first name.
            lastname. Customer last name.
            sentence_years. The length of the sentence in years.
            sentence_months. The length of the sentence in months.
            remand_days. The length of the remand in days.
            sentence_start. Sentence start date in the format YYYY-MM-DD

        Returns: A string "None" if everything went OK. Returns a string containing error information if something went wrong.
        """
        e = None

        try:

            with open("asiakkaat.csv", mode='a', newline='', encoding='utf-8') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([
                    firstname, lastname, sentence_years, sentence_months, remand_days, sentence_start, self.sentence_end_date])

        except PermissionError as e:
            return e
        
        except Exception as e:
            return e

        return e