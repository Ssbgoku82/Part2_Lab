import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from interface import *
from teaching import *

def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    main_ui = Ui_MainWindow()
    main_ui.setupUi(MainWindow)

    python_app = PythonApp(main_ui)

    main_ui.nextButton.clicked.connect(python_app.next_lesson)
#    main_ui.backButton.clicked.connect(python_app.previous_lesson)
    main_ui.RunCode.clicked.connect(python_app.execute_code)
    main_ui.startLesson.clicked.connect(lambda: python_app.display_lesson(0))

    main_ui.problemButton.clicked.connect(python_app.display_problem)
    main_ui.checkButton.clicked.connect(python_app.check_solution)





    MainWindow.setWindowTitle("Python Application")
    MainWindow.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()




