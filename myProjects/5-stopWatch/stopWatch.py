import sys
from PySide6.QtWidgets import QDialog, QApplication, QDialogButtonBox, QVBoxLayout, QLabel, QPushButton

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        layout=QVBoxLayout()
        lbl=QLabel('00:00:00')
        btnStart=QPushButton('Start')
        btnStop=QPushButton('Stop')
        buttonBox=QDialogButtonBox(QDialogButtonBox.Ok)
        buttonBox.addButton(btnStart,QDialogButtonBox.ActionRole)
        buttonBox.addButton(btnStop,QDialogButtonBox.ActionRole)
        layout.addWidget(lbl)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

        self.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    stopWatch=Dialog()
    sys.exit(app.exec())