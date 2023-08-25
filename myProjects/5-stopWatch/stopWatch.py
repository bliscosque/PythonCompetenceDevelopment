import sys
from PySide6.QtWidgets import QDialog, QApplication, QDialogButtonBox, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QTimer, QTime

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.timer=QTimer(self)
        self.msecs=100
        self.timer.setInterval(self.msecs)
        self.timer.timeout.connect(self.timeout)
        self.time=QTime(0,0)

    
    def initializeUI(self):
        layout=QVBoxLayout()
        self.lbl=QLabel('00:00:00')
        btnStart=QPushButton('Start')
        btnStop=QPushButton('Stop')
        buttonBox=QDialogButtonBox(QDialogButtonBox.Ok)
        buttonBox.addButton(btnStart,QDialogButtonBox.ActionRole)
        buttonBox.addButton(btnStop,QDialogButtonBox.ActionRole)
        layout.addWidget(self.lbl)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

        # connecting buttons with functions
        btnStart.clicked.connect(self.start)
        btnStop.clicked.connect(self.stop)
        buttonBox.accepted.connect(self.ok)

        self.show()

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def ok(self):
        self.close()

    def timeout(self):
        self.time=self.time.addMSecs(self.msecs)
        self.lbl.setText(self.time.toString())

if __name__=='__main__':
    app=QApplication(sys.argv)
    stopWatch=Dialog()
    sys.exit(app.exec())