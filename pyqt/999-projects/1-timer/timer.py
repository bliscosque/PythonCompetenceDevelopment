import sys, json
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QTextEdit, QGridLayout, QPushButton) 
from PySide6.QtCore import Qt, QDate, Qt
from PySide6.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__() 
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(500, 100) 
        self.setWindowTitle("QGridLayout Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        name_label = QLabel("Timer")
        name_label.setFont(QFont("Arial", 20))
        name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Create widgets for timers and buttons
        t15_label = QLabel("15:00")
        t15_label.setFont(QFont("Arial", 14))
        btn_15_start_pause = QPushButton('Start')
        btn_15_reset = QPushButton('Pause')
        btn_15_start_pause.clicked.connect(self.start)

        t25_label = QLabel("25:00")
        t25_label.setFont(QFont("Arial", 14))
        btn_25_start_pause = QPushButton('Start')
        btn_25_reset = QPushButton('Pause')

        # Create widget for date
        today = QDate.currentDate().toString(Qt.DateFormat.ISODate)
        date_label = QLabel(today)
        date_label.setFont(QFont("Arial", 18))
        date_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        

        # Create grid and add components
        self.main_grid = QGridLayout()
        self.main_grid.addWidget(name_label, 0, 0)
        self.main_grid.addWidget(t15_label, 1, 0)
        self.main_grid.addWidget(btn_15_start_pause, 1, 1)
        self.main_grid.addWidget(btn_15_reset, 1, 2)

        self.main_grid.addWidget(t25_label, 2, 0)
        self.main_grid.addWidget(btn_25_start_pause, 2, 1)
        self.main_grid.addWidget(btn_25_reset, 2, 2)


        self.main_grid.addWidget(date_label, 0, 1)

        self.setLayout(self.main_grid)

    def start(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())