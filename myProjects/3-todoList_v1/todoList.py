import sys
from PySide6.QtWidgets import (QApplication,QMessageBox,QMainWindow,QListWidget,QAbstractItemView, QToolBar)
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.create_actions()
        self.create_menus()
        self.createToolBar()
        self.listWidget=QListWidget()
        self.setCentralWidget(self.listWidget)
        self.listWidget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        
        self.show()

    def create_actions(self):
        #File
        self.new_action=QAction("New")
        self.new_action.triggered.connect(self.new)

        self.open_action=QAction("Open")
        self.open_action.triggered.connect(self.open)

        self.save_action=QAction("Save")
        self.save_action.triggered.connect(self.save)

        self.save_as_action=QAction("Save As")
        self.save_as_action.triggered.connect(self.save_as)

        self.exit_action=QAction("Exit")
        self.exit_action.triggered.connect(self.exit)

        #Items
        self.add_action=QAction("Add")
        self.add_action.triggered.connect(self.add)

        self.remove_action=QAction("Remove")
        self.remove_action.triggered.connect(self.remove)

        self.clear_action=QAction("Clear")
        self.clear_action.triggered.connect(self.clear)

        self.select_all_action=QAction("Select All")
        self.select_all_action.triggered.connect(self.select_all)

        self.select_none_action=QAction("Select None")
        self.select_none_action.triggered.connect(self.select_none)

        #State
        self.checked_action=QAction("Checked")
        self.checked_action.triggered.connect(self.checked)

        self.unchecked_action=QAction("Unchecked")
        self.unchecked_action.triggered.connect(self.unchecked)

        self.partially_action=QAction("Partially")
        self.partially_action.triggered.connect(self.partially)

    def create_menus(self):
        menu_bar=self.menuBar()
        file_menu=menu_bar.addMenu("File")
        file_menu.addAction(self.new_action)
        file_menu.addSeparator()
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.save_as_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        items_menu=menu_bar.addMenu("Items")
        items_menu.addAction(self.add_action)
        items_menu.addAction(self.remove_action)
        items_menu.addSeparator()
        items_menu.addAction(self.clear_action)
        items_menu.addSeparator()
        items_menu.addAction(self.select_all_action)
        items_menu.addAction(self.select_none_action)

        state_menu=menu_bar.addMenu("State")
        state_menu.addAction(self.checked_action)
        state_menu.addAction(self.unchecked_action)
        state_menu.addAction(self.partially_action)

    def createToolBar(self):
        toolbar=QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        toolbar.addAction(self.new_action)
        toolbar.addAction(self.open_action)
        toolbar.addAction(self.save_action)
        toolbar.addAction(self.save_as_action)
        toolbar.addSeparator()
        toolbar.addAction(self.add_action)
        toolbar.addAction(self.remove_action)
        toolbar.addSeparator()
        toolbar.addAction(self.checked_action)
        toolbar.addAction(self.unchecked_action)
        toolbar.addAction(self.partially_action)


    def new(self):
        pass
    def open(self):
        pass
    def save(self):
        pass
    def save_as(self):
        pass
    
    def exit(self):
        self.close()

    def add(self):
        pass
    def remove(self):
        pass
    def clear(self):
        pass
    def select_all(self):
        pass
    def select_none(self):
        pass
    def checked(self):
        pass
    def unchecked(self):
        pass
    def partially(self):
        pass

if __name__=='__main__':
    app=QApplication(sys.argv)
    todoList=MainWindow()
    sys.exit(app.exec())
