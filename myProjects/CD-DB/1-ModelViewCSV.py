import sys, csv, os
from PySide6.QtWidgets import (QApplication, QWidget, QTableView, QAbstractItemView, QVBoxLayout)
from PySide6.QtGui import (QStandardItemModel, QStandardItem)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setWindowTitle("Primeiro exemplo de model/view")
        self.setupMainWindow()
        self.loadCSVFile()
        self.show()

    def setupMainWindow(self):
        self.model=QStandardItemModel()
        table_view=QTableView()
        #table_view.setSelectionMode(QAbstractItemView.selectionMode.ExtendedSelection)
        table_view.setModel(self.model)

        #self.model.setRowCount(3)
        self.model.setColumnCount(4)

        layout=QVBoxLayout()
        layout.addWidget(table_view)
        self.setLayout(layout)

    def loadCSVFile(self):
        file_name=os.path.dirname(os.path.abspath(__file__))+'/sample.csv'
        print(file_name)
        with open(file_name,"r") as csv_f:
            reader=csv.reader(csv_f)
            header_labels=next(reader)
            self.model.setHorizontalHeaderLabels(header_labels)
            for i,row in enumerate(csv.reader(csv_f)):
                items=[QStandardItem(item) for item in row]
                self.model.insertRow(i,items)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec())