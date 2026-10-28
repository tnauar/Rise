from BackendLogic import BackendLogic

class TestBackendLogic:

    def setup_method(self):
        self.backend_logic = BackendLogic()

    def test_calculate_date(self):
         
        assert self.backend_logic.calculate_date(10, 10, 10, "2017-05-16") == None
        assert self.backend_logic.sentence_end_date == "2028-03-06"

        assert self.backend_logic.calculate_date(10, 11, 365, "2017-05-16") == None
        assert self.backend_logic.sentence_end_date == "2027-04-17"

        assert self.backend_logic.calculate_date(1, 0, 1, "2025-05-01") == None
        assert self.backend_logic.sentence_end_date == "2026-04-30"

        assert self.backend_logic.calculate_date(0, 11, 0, "2017-05-16") == None
        assert self.backend_logic.sentence_end_date == "2018-04-16"

        assert self.backend_logic.calculate_date(0, 1, 20, "2024-11-26") == None
        assert self.backend_logic.sentence_end_date == "2024-12-06"

        assert self.backend_logic.calculate_date(2, 7, 12, "2024-10-14") == None
        assert self.backend_logic.sentence_end_date == "2027-05-02"

    def test_write_file(self):
         
        assert self.backend_logic.write_file("Jari", "Virtanen", 16, 2, 116, "2019-01-16", "testi_asiakkaat.csv") == None