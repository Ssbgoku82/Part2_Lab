import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from interface import *
from teaching import *

def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Python Lesson")
    MainWindow.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()




