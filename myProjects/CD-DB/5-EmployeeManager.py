import os,sys
from PySide6.QtWidgets import (QApplication,QWidget,QLabel,QPushButton,QComboBox,QTableView,QHeaderView,
                               QAbstractItemView, QMessageBox, QHBoxLayout, QVBoxLayout, QSizePolicy)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtSql import (QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel, QSqlRelationalDelegate)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(1000,600)
        self.setWindowTitle("Employee Manager GUI")

        self.createDBConnection()
        self.createModel()
        self.setupMainWindow()
        self.show()

    def createDBConnection(self):
        database=QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName(os.path.dirname(os.path.abspath(__file__))+"/emp.db")
        
        if not database.open():
            print("Unable to open DB file")
            sys.exit(1)

        # check tables required for this
        tables_needed={"employee", "department"}
        tables_not_found=tables_needed-set(database.tables())
        if tables_not_found:
            QMessageBox.critical(self,"Error",f"Missing table(s): {tables_not_found}")
            sys.exit(1)
    
    def createModel(self):
        model=QSqlRelationalTableModel()
        model.setTable("employee")
        model.setRelation(model.fieldIndex("department_id"),QSqlRelation("department","id","department_name")) # department_name will be shown 


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec())