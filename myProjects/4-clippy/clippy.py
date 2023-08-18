import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QToolBar, QFileDialog, QMessageBox
from PySide6.QtGui import QAction, QIcon, QClipboard
from PySide6.QtCore import Qt, QStringListModel, QTimer

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
        
        # Attrs
        self.m_changed=False
        self.m_path=""
        self.m_last=""
        self.m_list=[]
        self.m_model=QStringListModel()
        self.m_timer=QTimer()

        self.m_model.setStringList(self.m_list)
        self.listView.setModel(self.m_model)
        self.m_timer.timeout.connect(self.timeout)
        self.m_timer.setInterval(500)
        self.m_timer.start()
        

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

        self.start_action=QAction("Start")
        self.start_action.triggered.connect(self.start)
        self.start_action.setIcon(QIcon(os.path.join(m_path,"./images/start.png")))

        self.stop_action=QAction("Stop")
        self.stop_action.triggered.connect(self.stop)
        self.stop_action.setIcon(QIcon(os.path.join(m_path,"./images/stop.png")))

        self.copy_action=QAction("Copy")
        self.copy_action.triggered.connect(self.copy)
        self.copy_action.setIcon(QIcon(os.path.join(m_path,"./images/copy.png")))

        self.cut_action=QAction("Cut")
        self.cut_action.triggered.connect(self.cut)
        self.cut_action.setIcon(QIcon(os.path.join(m_path,"./images/cut.png")))

        self.paste_action=QAction("Paste")
        self.paste_action.triggered.connect(self.paste)
        self.paste_action.setIcon(QIcon(os.path.join(m_path,"./images/paste.png")))

        self.delete_action=QAction("Delete")
        self.delete_action.triggered.connect(self.delete)
        self.delete_action.setIcon(QIcon(os.path.join(m_path,"./images/delete.png")))


    def create_toolbar(self):
        toolbar=QToolBar("Main Toolbar")
        self.addToolBar(Qt.ToolBarArea.RightToolBarArea,toolbar)

        toolbar.addAction(self.new_action)
        toolbar.addAction(self.open_action)
        toolbar.addAction(self.save_action)
        toolbar.addAction(self.save_as_action)
        toolbar.addSeparator()
        toolbar.addAction(self.start_action)
        toolbar.addAction(self.stop_action)
        toolbar.addSeparator()
        toolbar.addAction(self.copy_action)
        toolbar.addAction(self.cut_action)
        toolbar.addAction(self.paste_action)
        toolbar.addAction(self.delete_action)

        
    def new(self):
        self.check_saved()
        self.m_list.clear()
        self.m_path=""
        self.m_changed=False
        self.m_model.setStringList(self.m_list)

    def open(self):
        self.check_saved()
        tmp=QFileDialog.getOpenFileName(self,"Open File")
        if tmp=="":
            return
        
        self.m_list.clear()

        try:
            with open(self.m_path,"r") as file:
                lines=file.readlines()
                for line in lines:
                    self.m_list.append(line)
                    
        except Exception as e:
             QMessageBox.critical(self, "Error Opening File", str(e))
        self.m_path=tmp
        self.m_changed=False
        self.m_model.setStringList(self.m_list)
        self.statusBar().showMessage("Opened",2000)

    def save(self):
        pass

    def save_as(self):
        pass

    def start(self):
        self.m_timer.start()
        self.statusBar().showMessage("Listening to the clipboard",2000)

    def stop(self):
        self.m_timer.stop()
        self.statusBar().showMessage("Manual mode",2000)

    def cut(self):
        pass
    def copy(self):
        pass

    def paste(self):
        self.timeout()

    def delete(self):
        pass

    def timeout(self):
        clipboard=QClipboard()
        data=clipboard.text()
        if data==self.m_last:
            self.m_last=data
            print(self.m_last)
            if self.m_last not in self.m_list:
                self.m_list.append(self.m_last)
                self.m_model.setStringList(self.m_list)
                self.statusBar.showMessage("Added to the clipboard", 2000)

    def check_saved(self):
        if not self.m_changed:
            return
        ans=QMessageBox.question(self,"Save Changes?","Would you like to save your changes?")
        if ans==QMessageBox.standardButton.Yes:
            self.save()

if __name__=='__main__':
    app=QApplication(sys.argv)
    clippy=MainWindow()
    sys.exit(app.exec())