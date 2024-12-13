from main import *
from teaching import *
from interface import *

class TestPythonApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None: