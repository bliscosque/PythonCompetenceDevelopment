# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# QWidget -> genérico
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

app = QApplication(sys.argv)

botao1 = QPushButton('Botao 1')
botao1.setStyleSheet('font-size: 40px;')

botao2 = QPushButton('Botao 2')
botao2.setStyleSheet('font-size: 40px;')

layout=QVBoxLayout()
layout.addWidget(botao1)
layout.addWidget(botao2)

central=QWidget()
central.setLayout(layout)
central.show()

app.exec()  # O loop da aplicação