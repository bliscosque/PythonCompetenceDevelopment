import os, sys
from PySide6.QtWidgets import (QApplication,QWidget,QTableView,QMessageBox,QHeaderView,QVBoxLayout)
from PySide6.QtSql import (QSqlDatabase,QSqlRelation,QSqlRelationalTableModel,QSqlRelationalDelegate)

# work with tables with relationship

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(1000,500)
        self.setWindowTitle("Sql Table Model")

        self.createDBConnection()
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

    def setupMainWindow(self):
        model=QSqlRelationalTableModel()
        model.setTable("employee")
        model.setRelation(model.fieldIndex("department_id"),QSqlRelation("department","id","department_name")) # department_name will be shown 
        
        table_view=QTableView()
        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # populate the model
        model.select()

        #instancia o delegate
        delegate=QSqlRelationalDelegate()
        table_view.setItemDelegate(delegate)

        layout=QVBoxLayout()
        layout.addWidget(table_view)
        self.setLayout(layout)


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec())
    