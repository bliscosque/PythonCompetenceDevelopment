import sys
import wexpect
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QTextEdit, QPushButton

class PowerShellApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

        # Inicia o processo do PowerShell no início do aplicativo
        self.process = wexpect.spawn("powershell", encoding='utf-8')

    def init_ui(self):
        self.setWindowTitle("PowerShell App")
        self.setGeometry(100, 100, 600, 400)

        # Widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout principal
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Caixa de entrada para inserir comandos
        self.command_input = QLineEdit(self)
        layout.addWidget(self.command_input)

        # Caixa de texto para exibir a saída do comando
        self.output_terminal = QTextEdit(self)
        self.output_terminal.setReadOnly(True)
        layout.addWidget(self.output_terminal)

        # Botão para enviar o comando
        execute_button = QPushButton("Executar", self)
        execute_button.clicked.connect(self.execute_command)
        layout.addWidget(execute_button)

    def execute_command(self):
        try:
            command = self.command_input.text()

            # Envia o comando para o processo do PowerShell
            self.process.sendline(command)

            # Espera a saída do comando
            self.process.expect_exact(">")

            # Obtém a saída do comando
            output = self.process.before.strip()

            # Exibe a saída na caixa de texto
            self.output_terminal.append(f"Saida do comando:\n{output}")

        except Exception as e:
            self.output_terminal.append(f"Erro ao executar o comando: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    powershell_app = PowerShellApp()
    powershell_app.show()
    sys.exit(app.exec())
