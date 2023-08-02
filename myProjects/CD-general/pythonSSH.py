import sys
import paramiko
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget

class SSHClientApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("SSH Client")
        self.setGeometry(100, 100, 600, 400)

        # Widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout principal
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Terminal de saída
        self.output_terminal = QTextEdit(self)
        self.output_terminal.setReadOnly(True)
        layout.addWidget(self.output_terminal)

        # Botão para conectar ao servidor
        connect_button = QPushButton("Conectar", self)
        connect_button.clicked.connect(self.connect_to_server)
        layout.addWidget(connect_button)

    def connect_to_server(self):
        try:
            # Configuração da conexão SSH (ajuste os valores conforme necessário)
            hostname = "example.com"
            port = 22
            username = "your_username"
            password = "your_password"

            # Cria um cliente SSH usando o módulo paramiko
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Conecta ao servidor
            ssh_client.connect(hostname, port, username, password)

            # Executa um comando de exemplo (substitua-o pelo que desejar)
            stdin, stdout, stderr = ssh_client.exec_command("ls -l")

            # Obtém a saída do comando
            output = stdout.read().decode("utf-8")

            # Exibe a saída no terminal do aplicativo
            self.output_terminal.append(output)

            # Fecha a conexão SSH
            ssh_client.close()

        except paramiko.AuthenticationException:
            self.output_terminal.append("Falha na autenticação. Verifique suas credenciais.")
        except paramiko.SSHException as e:
            self.output_terminal.append(f"Erro na conexão SSH: {str(e)}")
        except Exception as e:
            self.output_terminal.append(f"Erro: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ssh_client_app = SSHClientApp()
    ssh_client_app.show()
    sys.exit(app.exec())
