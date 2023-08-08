import sys
from PySide6.QtWidgets import (QApplication,QListWidgetItem,QMainWindow,QListWidget,QAbstractItemView, QToolBar,QFileDialog,QMessageBox)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.file_changed=False

    def initializeUI(self):
        self.create_actions()
        self.create_menus()
        self.createToolBar()
        self.listWidget=QListWidget()
        self.setCentralWidget(self.listWidget)
        self.listWidget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        
        self.show()
        self.create()

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
        self.checkSave()
        self.create()

    def open(self):
        self.checkSave()
        path,_=QFileDialog.getOpenFileName(self,"Open","","To-do (*.td)")
        if(path==""): return
        self.open_int(path)
    
    def open_int(self,path):
        try:
            with open(path,"r") as file:
                count=int(file.readline())
                for i in range(count):
                    state=Qt.CheckState(int(file.readline()))
                    name=file.readline()[:-1]
                    self.createItem(state,name)
        except Exception as e:
             QMessageBox.critical(self, "Error Opening File", str(e))
        self.file_name=path
        self.file_changed=False


    def save(self):
        if not self.file_name:
            self.save_as()
            return
        self.save_int(self.file_name)
    
    def save_as(self):
        path,_=QFileDialog.getSaveFileName(self,"Save","","To-do (*.td)")
        if not path: return
        self.save_int(path)

    def save_int(self, path):
        print(path)
        try:
            with open(path,"w") as file:
                count=self.listWidget.count()
                file.write(str(count)+"\n")
                for i in range(count):
                    item=self.listWidget.item(i)
                    state=str(item.checkState())
                    if "Unchecked" in state: 
                        stateInt=0
                    elif "artia" in state:
                        stateInt=1
                    else:
                        stateInt=2
                    file.write(str(stateInt)+"\n")
                    file.write(item.text()+"\n")
        except Exception as e:
             QMessageBox.critical(self, "Error Saving File", str(e))
        self.file_name=path
        self.file_changed=False
    
    def exit(self):
        self.close()

    def add(self):
        self.createItem(Qt.CheckState.Unchecked,"New Item")
        self.file_changed=True

    def remove(self):
        list=self.listWidget.selectedItems()
        for item in list:
            self.listWidget.takeItem(self.listWidget.row(item))
        self.file_changed=True

    def clear(self):
        self.listWidget.clear()
        self.file_changed=True

    def select_all(self):
        self.listWidget.selectAll()

    def select_none(self):
        self.listWidget.clearSelection()

    def checked(self):
        list=self.listWidget.selectedItems()
        for item in list:
            item.setCheckState(Qt.CheckState.Checked)
        self.file_changed=True

    def unchecked(self):
        list=self.listWidget.selectedItems()
        for item in list:
            item.setCheckState(Qt.CheckState.Unchecked)
        self.file_changed=True
    
    def partially(self):
        list=self.listWidget.selectedItems()
        for item in list:
            item.setCheckState(Qt.CheckState.PartiallyChecked)
        self.file_changed=True

    def checkSave(self):
        pass

    def create(self):
        self.file_changed=False
        self.file_name=""
        self.listWidget.clear()

    def createItem(self, state, name):
        item=QListWidgetItem(name,self.listWidget)
        item.setCheckState(state)
        item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsAutoTristate | Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsSelectable)
        self.listWidget.addItem(item)

if __name__=='__main__':
    app=QApplication(sys.argv)
    todoList=MainWindow()
    sys.exit(app.exec())
