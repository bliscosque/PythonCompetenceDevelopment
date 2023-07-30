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
        self.model=QSqlRelationalTableModel()
        self.model.setTable("employee")
        self.model.setRelation(self.model.fieldIndex("department_id"),QSqlRelation("department","id","department_name")) # department_name will be shown 

        self.model.setHeaderData(self.model.fieldIndex("id"),Qt.Orientation.Horizontal,"ID")
        self.model.setHeaderData(self.model.fieldIndex("first_name"),Qt.Orientation.Horizontal,"First Name")
        self.model.setHeaderData(self.model.fieldIndex("last_name"),Qt.Orientation.Horizontal,"Last Name")
        self.model.setHeaderData(self.model.fieldIndex("email"),Qt.Orientation.Horizontal,"Email")
        self.model.setHeaderData(self.model.fieldIndex("department_name"),Qt.Orientation.Horizontal,"Department Name")

        self.model.select()

    def setupMainWindow(self):
        icons_path=os.path.dirname(os.path.abspath(__file__))+"/icons"

        title=QLabel("Employee Manager System")
        title.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        title.setStyleSheet("font: bold 24px")

        btn_add_emp=QPushButton("Add Employee")
        btn_add_emp.setIcon(QIcon(os.path.join(icons_path,"add_user.png")))
        btn_add_emp.setStyleSheet("padding: 10px")
        btn_add_emp.clicked.connect(self.addEmp)

        btn_del_emp=QPushButton("Delete")
        btn_del_emp.setIcon(QIcon(os.path.join(icons_path,"trash_can.png")))
        btn_del_emp.setStyleSheet("padding: 10px")
        btn_del_emp.clicked.connect(self.delEmp)

        sorting_options = ["Sort by ID", "Sort by First Name", "Sort by Last Name", "Sort by Department"]
        cmb_sort=QComboBox()
        cmb_sort.addItems(sorting_options)
        cmb_sort.currentTextChanged.connect(self.setSortingOrder)

        buttons_h_box=QHBoxLayout()
        buttons_h_box.addWidget(btn_add_emp)
        buttons_h_box.addWidget(btn_del_emp)
        buttons_h_box.addStretch()
        buttons_h_box.addWidget(cmb_sort)

        edit_container=QWidget()
        edit_container.setLayout(buttons_h_box)

        self.table_view=QTableView()
        self.table_view.setModel(self.model)

        horizontal=self.table_view.horizontalHeader()
        horizontal.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        vertical=self.table_view.verticalHeader()
        vertical.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.table_view.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        delegate=QSqlRelationalDelegate()
        self.table_view.setItemDelegate(delegate)

        main_v_layout =QVBoxLayout()
        main_v_layout.addWidget(title,Qt.AlignmentFlag.AlignLeft)
        main_v_layout.addWidget(edit_container)
        main_v_layout.addWidget(self.table_view)
        self.setLayout(main_v_layout)
        

    def addEmp(self):
        last_row=self.model.rowCount()
        self.model.insertRow(last_row)

        #if ID is not valid, it will be next available
        query=QSqlQuery()
        query.exec("SELECT MAX(id) from employee")
        if query.next():
            int(query.value(0))

    def delEmp(self):
        current_item=self.table_view.selectedIndexes()
        for idx in current_item:
            self.model.removeRow(idx.row())
        self.model.select()

    def setSortingOrder(self, text):
        if text == "Sort by ID":
            self.model.setSort(self.model.fieldIndex("id"), Qt.SortOrder.AscendingOrder)
        elif text == "Sort by First Name":
            self.model.setSort(self.model.fieldIndex("first_name"), Qt.SortOrder.AscendingOrder)
        elif text == "Sort by Last Name":
            self.model.setSort(self.model.fieldIndex("last_name"), Qt.SortOrder.AscendingOrder)
        elif text == "Sort by Department":
            self.model.setSort(self.model.fieldIndex("department_name"), Qt.SortOrder.AscendingOrder)

        self.model.select()

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec())