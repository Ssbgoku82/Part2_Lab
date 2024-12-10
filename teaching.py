from collections.abc import ItemsView
from PyQt6.QtGui import QStandardItemModel, QStandardItem


class PythonApp:
    def __init__(self,main_ui):
        self.main_ui = main_ui
        self.current_lesson = 0
        self.current_problem = 0
        self.lessons = [
            "Lesson 1: Variables\n"
            "Variables are used to store data for later use.\n\n"
            "1. Assign the value 10 to variable named 'x'.\n"
            "2. Assign your name to a variable called 'name' and print it.\n"
            "3. Create two variables 'x' and 'y' with values 3 and 4, then print their sum.\n"
            "4. Assign 10 to 'x', 20 to 'y', and swap their values. \n",
            "Example:\n\n"
            "x = 5\nprint(x)\n\n",
            "Problems:\n"

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

            lesson_title = self.lessons[index].split(":")[0]
            self.main_ui.textLabel.setText(f"Displayed: {lesson_title}")

    def next_lesson(self, index):
        if self.current_lesson < len(self.lessons) - 1:
            self.current_lesson += 1
            self.display_lesson(self.current_lesson)

    def display_problem(self) -> None:
        if self.current_problem < len(self.lesson_1_problems):
            problem_text = self.lesson_1_problems[self.current_problem]["problem"]
            self.main_ui.texEdit.setPlainText(problem_text)
        else:
            self.main_ui.textBrowser.setPlainText("You have completed all problems for this lesson")

    def check_solution(self):
        if self.current_problem >= len(self.lesson_1_problems):
            self.main_ui.textBrowser.setPlainText("All problems are completed.")
            return
        user_code = self.main_ui.textEdit.toPlainText()
        expected_solution = self.lesson_1_problems[self.current_problem]["solution"]

        try:
            exec_code = {}
            exec(user_code, exec_code)
            exec(expected_solution, exec_code)

            if exec_code == exec_code:
                self.main_ui.textBrowser.setPlainText("Correct, move to the next problem")
                self.current_problem += 1
                self.display_problem()

            else:
                self.main_ui.textBrowser.setPlainText("Incorrect. Try again.")
        except Exception as e:
            self.main_ui.textBrowser.setPlainText(f"Error: {str(e)}")

    def execute_code(self):
        code = self.main_ui.textEdit.toPlainText()
        try:
            exec_code = {}
            exec(code, exec_code)
            self.main_ui.textBrowser.setPlainText("Code executed successfully")
        except Exception as e:
            self.main_ui.textBrowser.setPlainText("Error: {str(e)}")








