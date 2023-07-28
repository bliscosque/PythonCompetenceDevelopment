import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow, QVBoxLayout
from PySide6.QtCore import Slot

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btn1=QPushButton("Botao 1")
        self.btn2=QPushButton("Botao 2")

        self.layout=QVBoxLayout()
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)

        self.central_widget=QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle("Meu primeiro programa")
        self.central_widget.setLayout(self.layout)
        self.show()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win=MainWindow()
    sys.exit(app.exec())