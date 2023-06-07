import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Temperature Converter')
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.celsius_label = QLabel('Celsius:')
        self.celsius_input = QLineEdit()
        self.fahrenheit_label = QLabel('Fahrenheit:')
        self.fahrenheit_output = QLabel()

        convert_button = QPushButton('Convert')
        convert_button.clicked.connect(self.convert_temperature)

        layout.addWidget(self.celsius_label)
        layout.addWidget(self.celsius_input)
        layout.addWidget(self.fahrenheit_label)
        layout.addWidget(self.fahrenheit_output)
        layout.addWidget(convert_button)

        self.setLayout(layout)

    def convert_temperature(self):
        celsius = float(self.celsius_input.text())
        fahrenheit = (celsius * 9/5) + 32
        self.fahrenheit_output.setText(str(fahrenheit))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = TemperatureConverter()
    converter.show()
    sys.exit(app.exec_())
