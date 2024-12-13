from PyQt6.QtWidgets import QVBoxLayout

from main import *
from teaching import *
from interface import *

class TestPythonApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None:
        """
        Setting up the UI test.
        """
        #Main Window
        self.setWindowTitle("Python Code Tester")
        self.setGeometry(100, 100, 600, 400)

        #central Widget
        self.central_widget = QtWidgets()
        self.centralWidget(self.central_widget)

        #Create Layout
        layout = QVBoxLayout()



