from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self,parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent,*args,**kwargs)

        self.cw=QWidget()
        self.v_layout=QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        self.setWindowTitle("Thiago's calc")

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(),self.height())

    def addToVLayout(self,widget):
        self.v_layout.addWidget(widget)