from collections.abc import ItemsView
from PyQt6.QtGui import QStandardItemModel, QStandardItem


class PythonApp:
    def __init__(self,main_ui):
        self.main_ui = main_ui
        self.current_lesson = 0
        self.lessons = [
            "Lesson 1",
            "Lesson 2",
            "Lesson 3",
        ]

        self.tree_view()

    def tree_view(self) -> None:

        model = QStandardItemModel()
        self.main_ui.treeView.setModel(model)
        model.appendRow()

    def display_lesson(self, index) -> None:
        if 0 <= index < len(self.lessons):
            self.main_ui.textEdit.setPlainText(self.lessons[index])
            self.current_lesson = index







