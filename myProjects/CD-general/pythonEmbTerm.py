# Até agora, a unica maneira que funcionou foi usando QT5 (Pyside2). Quando migro o código para Qt6, não funciona.

import sys
from PySide2 import QtCore, QtWidgets


class EmbTerminal(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(EmbTerminal, self).__init__(parent)
        self.process = QtCore.QProcess(self)
        self.terminal = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.terminal)
        # Works also with urxvt:
        # self.process.start('urxvt',['-embed', str(int(self.winId())),])
        self.process.start('xterm',['-into', str(int(self.winId()))])
        self.setFixedSize(640, 480)


class mainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)

        central_widget = QtWidgets.QWidget()
        lay = QtWidgets.QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        tab_widget = QtWidgets.QTabWidget()
        lay.addWidget(tab_widget)

        tab_widget.addTab(EmbTerminal(), "EmbTerminal")
        tab_widget.addTab(QtWidgets.QTextEdit(), "QTextEdit")
        tab_widget.addTab(QtWidgets.QMdiArea(), "QMdiArea")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = mainWindow()
    main.show()
    sys.exit(app.exec_())