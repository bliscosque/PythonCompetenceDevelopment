import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QMessageBox, QFileDialog, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QAction


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.text_edit = QTextEdit(self)

        self.create_actions()
        self.create_menus()
        self.create_buttons()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.text_edit)
        button_widget = QWidget()
        button_widget.setLayout(self.button_layout)
        main_layout.addWidget(button_widget)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("Editor de Textos")
        self.show()

    def create_actions(self):
        self.open_action = QAction("Abrir", self)
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction("Salvar", self)
        self.save_action.triggered.connect(self.save_file)

        self.exit_action = QAction("Sair", self)
        self.exit_action.triggered.connect(self.close)

    def create_menus(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("Arquivo")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.exit_action)

    def create_buttons(self):
        self.button_layout = QVBoxLayout()

        open_button = QPushButton("Abrir", self)
        open_button.clicked.connect(self.open_file)
        self.button_layout.addWidget(open_button)

        save_button = QPushButton("Salvar", self)
        save_button.clicked.connect(self.save_file)
        self.button_layout.addWidget(save_button)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir Arquivo", "", "Arquivos de Texto (*.txt)")
        if file_name:
            try:
                with open(file_name, "r") as file:
                    self.text_edit.setPlainText(file.read())
            except Exception as e:
                self.show_message_box(QMessageBox.Critical, "Erro ao abrir arquivo", str(e))

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", "Arquivos de Texto (*.txt)")
        if file_name:
            try:
                with open(file_name, "w") as file:
                    file.write(self.text_edit.toPlainText())
            except Exception as e:
                self.show_message_box(QMessageBox.Critical, "Erro ao salvar arquivo", str(e))

    def show_message_box(self, icon, title, text):
        msg_box = QMessageBox()
        msg_box.setIcon(icon)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    sys.exit(app.exec())
