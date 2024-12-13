from collections.abc import ItemsView
from PyQt6.QtGui import QStandardItemModel, QStandardItem

"""
This program was a huge project, I took this project on to challenge myself.
It seems this type of program would take more time to perfect. 
"""

class PythonApp:
    def __init__(self,main_ui) -> None:
        """
        The beginning of the PythonApp
        """

        self.main_ui = main_ui
        self.current_lesson = 0 #Start of the lesson number
        self.current_problem = 0 #Start of the problem currently
        self.hint_shown = False #Show hint when needed
        self.main_ui.RunCode.setEnabled(True) #Disabling the Run Code Button, currently not working properly.


        """
        This is the beginning of Lesson 1: Variables
        """

        self.lessons = [...]  # Lesson content
        self.lesson_1_problems: list[dict] = [...]

        self.lessons = [
            "Lesson 1: Variables\n\n"
            "Creating Variables\n\n"
            "Variables are used to store data for later use.\n"
            "Python has no command for declaring a variable.\n"          
            "A variable is created the moment you assign a value to it\n\n"
            "Click Next\n",
            "Examples:\n\n"
            "1. x = 5\nprint(x)\n\n"
            "2. x = 5\n  y = 'John'\n  print(x)\n  print(y)",
            "Problem 1:\n"
            "Assign the value 10 to variable named 'x'.\n\n",
            "Problem 2:\n"
            "Assign your name to a variable called 'name' and print it.\n\n",
            "Problem 3:\n"
            "Create two variables 'x' and 'y' with values 3 and 4, then print their sum.\n\n",
            "Problem 4:\n"
            "Assign 10 to 'x', 20 to 'y', and swap their values.\n\n",



            #"Lesson 2", still pending development
            #"Lesson 3", still pending development
        ]

        """Lesson 1 solving problems"""
        self.lesson_1_problems = [
            {"problem": "Assign the value 10 to a variable name 'a'.", "solution": "a = 10",
             "hint": "Use the assignment operator '=' to assign a value to 'a'."},

        ]


        self.populate_tree_view() #Populates the QTreeView Widget

    """Populate tree is showing which lessons are available and which lesson your on """
    def populate_tree_view(self) -> None:
        model = QStandardItemModel() #model for QTree
        self.main_ui.treeView.setModel(model) #Assign model to QTree
        for lesson in self.lessons:
            item = QStandardItem(lesson.split(":")[0]) #Extracts the lesson title
            model.appendRow(item) #Adds the lesson title


    def display_lesson(self, index: int) -> None:
        """
        This will display the lesson content.
        Updates the QLabel to show the lesson titles.
        """
        if 0 <= index < len(self.lessons): #Keeps the index within boundaries
            self.main_ui.textBrowser.setPlainText(self.lessons[index])
            self.current_lesson = index

            lesson_title = self.lessons[index].split(":")[0]
            self.main_ui.textLabel.setText(f"{lesson_title}")

    def next_lesson(self, index) -> None:
        if self.current_lesson < len(self.lessons) - 1:
            self.current_lesson += 1
            self.display_lesson(self.current_lesson)

    def previous_lesson(self):
        if self.current_lesson > 0:
            self.current_lesson -= 1
            self.display_lesson(self.current_lesson)


    """Displays the Python problems """

    def display_problem(self) -> None:

        if self.current_problem < len(self.lesson_1_problems): #Checks which problem you're on.
            problem_text = self.lesson_1_problems[self.current_problem]["Problem"] #Get the problem text
            self.main_ui.textBrowser.setPlainText(problem_text) #Display problem
            self.hint_shown = True
            self.main_ui.RunCode.setEnabled(True) #enable Run/Play Button
        else:
            self.main_ui.textBrowser.setPlainText("You have completed all problems for this lesson")
            self.main_ui.RunCode.setEnabled(True)

    """Checks the solution entered by the user"""

    def check_solution(self) -> str:
        if self.current_problem >= len(self.lesson_1_problems):
            self.main_ui.textBrowser.setPlainText("All problems are completed.")
            return "All problems are completed."

        user_code = self.main_ui.textBrowser.toPlainText()
        expected_solution = self.lesson_1_problems[self.current_problem]["solution"]
        hint = self.lesson_1_problems[self.current_problem]["hint"]

        try:
            exec_code = {}
            exec(user_code, exec_code)
            exec(expected_solution, exec_code)

            if exec_code == exec_code:
                self.main_ui.textBrowser.setPlainText("Correct, move to the next problem")
                self.current_problem += 1
                self.display_problem()
                return "Correct"

            else:
                if not self.hint_shown:
                    self.main_ui.textBrowser.setPlainText("Incorrect. Hint: {hint}")
                    self.hint_shown = True

                else:
                    self.main_ui.textBrowser.setPlainText("Incorrect. Try Again")
                return "Incorrect"

        except Exception as e:
            if not self.hint_shown:
                self.main_ui.textBrowser.setPlainText(f"Error: {str(e)}\nHint: {hint}")
                self.hint_shown = True
            else:
                self.main_ui.textBrowser.setPlainText(f"Error: {str(e)}")
            return(f"Error: {str(e)}")

    def execute_code(self) -> str:
        """
        Executes the Python Code
        """
        code = self.main_ui.textEdit.toPlainText()# Gets the code from Qtext
        try:
            exec_code = {}
            exec(code, exec_code) #execute the code
            self.main_ui.textBrowser.setPlainText("Code executed successfully")
            return "Code executed successfully"
        except Exception as e:
            error_msg = f"Error: {str(e)}" #Captures Errors
            self.main_ui.textBrowser.setPlainText(error_msg)
            return error_msg


