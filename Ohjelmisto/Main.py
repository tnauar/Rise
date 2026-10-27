import tkinter
from BackendLogic import BackendLogic
from GuiScreen import GuiScreen

"""
This is the main program that starts the functionality and runs the GUI.
"""

class RotiApp(tkinter.Tk):
    def __init__(self):
        super().__init__()

        """
        Constructor of the main program that starts the needed data operations from BackendLogic and invokes the gui. 
        Inherits gui operations from tkinter.

        Args:
            None.

        Returns: None.
        """
        self.backend_logic = BackendLogic()     

        self.title("Roti simulaatio")
        self.geometry("960x768")
        self.team_selection = GuiScreen(self, self.backend_logic)
        self.team_selection.start()
        self.team_selection.pack(fill=tkinter.BOTH, expand=True)

"""
Program loops so that the gui stays active.
"""

if __name__ == "__main__":
    app = RotiApp()
    app.mainloop()