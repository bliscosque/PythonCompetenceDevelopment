import sys, os
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap, QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100,100,250,250)
        self.setWindowTitle("QLabel Example")
        
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        # Create labels
        hello_label=QLabel(self)
        hello_label.setText("Hello")
        hello_label.setFont(QFont("Arial",20))
        hello_label.setWordWrap(True)
        hello_label.move(85,15)

        curPath=os.path.dirname(os.path.realpath(__file__))
        image = curPath+"/images/world.png"
        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(25, 40)
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec())