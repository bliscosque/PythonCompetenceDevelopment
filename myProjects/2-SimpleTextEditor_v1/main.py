import sys
from PySide6.QtWidgets import (QApplication, QWidget, QMessageBox, QMainWindow, QPlainTextEdit, QFileDialog)
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.file_name=""

    def initializeUI(self):
        self.create_actions()
        self.create_menus()
        self.plainTextEdit=QPlainTextEdit()
        self.setCentralWidget(self.plainTextEdit)

        self.show()

    def create_actions(self):
        self.new_action=QAction("New")
        self.new_action.triggered.connect(self.new)

        self.open_action=QAction("Open")
        self.open_action.triggered.connect(self.open)

        self.save_action=QAction("Save")
        self.save_action.triggered.connect(self.save)

        self.save_as_action=QAction("Save as")
        self.save_as_action.triggered.connect(self.save_as)

        self.exit_action=QAction("Exit")
        self.exit_action.triggered.connect(self.exit)

    def create_menus(self):
        menu_bar=self.menuBar()
        file_menu=menu_bar.addMenu("File")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.save_as_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

    def open(self):
        file_name,_=QFileDialog.getOpenFileName(self, "Open File", "","Text Files (*.txt);;All Files (*.*)")
        if file_name:
            try:
                with open(file_name,"r") as file:
                    self.plainTextEdit.setPlainText(file.read())
            except Exception as e:
                QMessageBox.critical(self, "Error Opening File", str(e))
        self.file_name=file_name

    def new(self):
        self.plainTextEdit.clear()
        self.file_name=""

    def save(self):
        if self.file_name=="":
            self.save_as()
        else:
            try:
                with open(self.file_name, "w") as file:
                    file.write(self.plainTextEdit.toPlainText())
            except Exception as e:
                QMessageBox.critical(self, "Error Saving File", str(e))

    def save_as(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*.*)")
        if file_name:
            try:
                with open(file_name, "w") as file:
                    file.write(self.plainTextEdit.toPlainText())
            except Exception as e:
                QMessageBox.critical(self, "Error Saving File", str(e))
        self.file_name=file_name

    def exit(self):
        self.close()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    sEditor=MainWindow()
    sys.exit(app.exec())

