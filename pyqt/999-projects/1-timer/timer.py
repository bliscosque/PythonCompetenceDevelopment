import sys, json, os
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QTextEdit, QGridLayout, QPushButton) 
from PySide6.QtCore import Qt, QDate, QTimer, QUrl
from PySide6.QtGui import QFont
#from PySide6.QtMultimedia import QSoundEffect, QAudioOutput, QMediaPlayer
from playsound import playsound

class MainWindow(QWidget):
    def __init__(self):
        super().__init__() 
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(500, 100) 
        self.setWindowTitle("QGridLayout Example")

        self.timer=QTimer(self)
        self.timer.timeout.connect(self.updateTime)

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        name_label = QLabel("Timer")
        name_label.setFont(QFont("Arial", 20))
        name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Create widgets for timers and buttons
        self.t15_label = QLabel("15:00")
        self.t15_label.setFont(QFont("Arial", 14))
        self.btn_15_start_pause = QPushButton('Start')
        btn_15_reset = QPushButton('Reset')
        self.btn_15_start_pause.clicked.connect(self.start)
        btn_15_reset.clicked.connect(self.reset)

        t25_label = QLabel("25:00")
        t25_label.setFont(QFont("Arial", 14))
        btn_25_start_pause = QPushButton('Start')
        btn_25_reset = QPushButton('Reset')

        # Create widget for date
        today = QDate.currentDate().toString(Qt.DateFormat.ISODate)
        date_label = QLabel(today)
        date_label.setFont(QFont("Arial", 18))
        date_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        

        # Create grid and add components
        self.main_grid = QGridLayout()
        self.main_grid.addWidget(name_label, 0, 0)
        self.main_grid.addWidget(self.t15_label, 1, 0)
        self.main_grid.addWidget(self.btn_15_start_pause, 1, 1)
        self.main_grid.addWidget(btn_15_reset, 1, 2)

        self.main_grid.addWidget(t25_label, 2, 0)
        self.main_grid.addWidget(btn_25_start_pause, 2, 1)
        self.main_grid.addWidget(btn_25_reset, 2, 2)


        self.main_grid.addWidget(date_label, 0, 1)

        self.setLayout(self.main_grid)

    def start(self):
        self.btn_15_start_pause.setText('Pause')
        self.timer.start(1000)

    def updateTime(self):
        self.t15_label.setText(self.convert_decrement(self.t15_label.text()))
        print('updated')

    def reset(self):
        self.timer.stop()
        self.t15_label.setText('15:00')
    
    def convert_decrement(self,mmss):
        print(mmss)
        mm,ss=map(int,mmss.split(':'))
        tot_sec=mm*60+ss-1
        if tot_sec<=0: 
            self.playSound()
            self.timer.stop()
            return "00:00"
        nm,ns=divmod(tot_sec,60)
        return f"{nm:02d}:{ns:02d}"

    def playSound(self):
        print('on playSound')
        soundPath=os.path.dirname(os.path.realpath(__file__))+"\\sound.mp3"
        #print(soundPath)
        #sound_effect=QSoundEffect()
        #sound_effect.setSource(QUrl.fromLocalFile(Path(__file__).parent / "sound.wav"))
        #sound_effect.setVolume(100)
        #sound_effect.play()
        
        #player = QMediaPlayer()
        #audio_output=QAudioOutput()
        #player.setAudioOutput(audio_output)
        #player.errorOccurred.connect(self.playerError)
        #player.setSource(QUrl.fromLocalFile(soundPath))
        #audio_output.setVolume(1.0)
        #player.play()

        playsound(soundPath)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())