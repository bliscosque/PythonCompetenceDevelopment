import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QToolBar
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt

m_path=os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.create_actions()
        self.create_toolbar()
        self.listView=QListView()
        self.setCentralWidget(self.listView)

        self.show()
    
    def create_actions(self):
        self.new_action=QAction("New")
        self.new_action.triggered.connect(self.new)
        self.new_action.setIcon(QIcon(os.path.join(m_path,"./images/new.png")))

        self.open_action=QAction("Open")
        self.open_action.triggered.connect(self.open)
        self.open_action.setIcon(QIcon(os.path.join(m_path,"./images/open.png")))

        self.save_action=QAction("Save")
        self.save_action.triggered.connect(self.save)
        self.save_action.setIcon(QIcon(os.path.join(m_path,"./images/save.png")))


        self.save_as_action=QAction("Save As")
        self.save_as_action.triggered.connect(self.save_as)
        self.save_as_action.setIcon(QIcon(os.path.join(m_path,"./images/save_as.png")))


    def create_toolbar(self):
        toolbar=QToolBar("Main Toolbar")
        self.addToolBar(Qt.ToolBarArea.RightToolBarArea,toolbar)

        toolbar.addAction(self.new_action)
        toolbar.addAction(self.open_action)
        toolbar.addAction(self.save_action)
        toolbar.addAction(self.save_as_action)
        toolbar.addSeparator()
        
    def new(self):
        pass

    def open(self):
        pass

    def save(self):
        pass

    def save_as(self):
        pass


if __name__=='__main__':
    app=QApplication(sys.argv)
    clippy=MainWindow()
    sys.exit(app.exec())