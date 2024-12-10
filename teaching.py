from collections.abc import ItemsView
from PyQt6.QtGui import QStandardItemModel, QStandardItem


class PythonApp:
    def __init__(self,main_ui):
        self.main_ui = main_ui
        self.current_lesson = 0
        self.current_problem = 0
        self.lessons = [
            "Lesson 1: Variables\nVariables are used to store data for later use.\n\n",
            "Example:\n"
            "x = 5\nprint(x)\n\n"
            "Problems:\n:"
            "1. Assign the value 10 to variable named'a'./n"
            "2. Assign your name to a variable called 'name' and print it."
            "3. Create two variables 'x' and 'y' with vaules 3 and 4, then print their sum.\n "
            "4. Assign 10' to 'x', 20 to 'y', and swap their values. \n",
            #"Lesson 2",
            #"Lesson 3",
        ]

        self.lesson_1_problems = [
            {"problem": "Assign the value 10 to a variable name 'a'.", "solution": "a = 10"}
        ]

        self.populate_tree_view()

    def populate_tree_view(self) -> None:

        model = QStandardItemModel()
        self.main_ui.treeView.setModel(model)

        for lesson in self.lessons:
            item = QStandardItem(lesson.split(":")[0])
            model.appendRow(item)


    def display_lesson(self, index) -> None:
        if 0 <= index < len(self.lessons):
            self.main_ui.textEdit.setPlainText(self.lessons[index])
            self.current_lesson = index

    def next_lesson(self, index):
        if 0 <= index < len(self.lessons):
            self.main.ui.textEdit.setPlainText(self.lessons[index])
            self.current_lesson = index
            self.main_ui.textBrowser.setPlainText(f"Displayed: {self.lessons [index].split(':')[0]}")



    def display_problem(self) -> None:
        if self.current_problem < len(self.lesson_1_problems):
            problem_text = self.lesson_1_problems[self.current_problem]["problem"]
            self.main_ui.texEdit.setPlainText(problem_text)








