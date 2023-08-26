import sys
from PySide6.QtWidgets import QDialog,QApplication, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import QTime,QTimer
from datetime import datetime

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.msecs=100
        self.timer=QTimer(self)
        self.timer.setInterval(self.msecs)
        self.timer.start()
        self.timer.timeout.connect(self.timeout)

    def initializeUI(self):
        layout=QVBoxLayout()
        self.lbl=QLabel(datetime.now().strftime("%B %d, %Y %H:%M:%S"))
        btnOk=QPushButton("OK")
        layout.addWidget(self.lbl)
        layout.addWidget(btnOk)
        self.setLayout(layout)

        self.show()

        btnOk.clicked.connect(self.ok)


    def timeout(self):
        self.lbl.setText(datetime.now().strftime("%B %d, %Y %H:%M:%S"))

    def ok(self):
        self.close()

if __name__=='__main__':
    app=QApplication(sys.argv)
    clock=Dialog()
    sys.exit(app.exec())