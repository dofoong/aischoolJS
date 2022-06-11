from lib2to3.pgen2 import driver
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from threading import Timer
import time
import pyautogui
import pyperclip
import os,subprocess

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

macro = True
macro2 = True 
macroOn = True

class CWidget(QWidget):

    def __init__(self):
        super().__init__()
        # self.year = QLCDNumber(self)
        # self.month = QLCDNumber(self)
        # self.day = QLCDNumber(self)
        self.hour = QLCDNumber(self)
        self.min = QLCDNumber(self)
        self.sec = QLCDNumber(self)


        # LCD 글자색 변경
        pal = QPalette()
        pal.setColor(QPalette.WindowText, QColor(255,0,0))
        self.sec.setPalette(pal)

        self.initUI()

    def initUI(self):
        pb1 = QPushButton('오전', self)
        pb2 = QPushButton('점심', self)
        pb3 = QPushButton('오후', self)
        pb4 = QPushButton('과제제출', self)
        pb1.clicked.connect(self.pb1_clicked)
        pb2.clicked.connect(self.pb2_clicked)
        pb3.clicked.connect(self.pb3_clicked)
        pb4.clicked.connect(self.pb4_clicked)
        hbox1 = QHBoxLayout()
        hbox1.addWidget(pb1)
        hbox1.addWidget(pb2)
        hbox1.addWidget(pb3)
        hbox1.addWidget(pb4)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.hour)
        hbox2.addWidget(self.min)
        hbox2.addWidget(self.sec)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

        self.setWindowTitle('출석 시계')
        self.setGeometry(200, 200, 400, 200)

        self.showtime()

    def pb1_clicked(self):
        os.system("c:/aischool/1.url")
    def pb2_clicked(self):
        os.system("c:/aischool/2.url")
    def pb3_clicked(self):
        os.system("c:/aischool/3.url")
    def pb4_clicked(self):
        os.system("c:/aischool/4.url")

    def showtime(self):
        global macro
        global macro2
        global macroOn
        # 1970년 1월 1일 0시 0분 0초 부터 현재까지 경과시간 (초단위)
        t = time.time()
        # 한국 시간 얻기
        kor = time.localtime(t)
        # LCD 표시
        # self.year.display(kor.tm_year)
        # self.month.display(kor.tm_mon)
        # self.day.display(kor.tm_mday)
        self.hour.display(kor.tm_hour)
        self.min.display(kor.tm_min)
        self.sec.display(kor.tm_sec)
        # 시간세팅
        morning = kor.tm_hour == 9 and kor.tm_min >= 46
        morning2 = kor.tm_hour == 10 and kor.tm_min <= 4
        morningend = kor.tm_hour == 10 and kor.tm_min >= 5
        mef = morningend or kor.tm_hour == 11 or kor.tm_hour == 12
        morningend2 = kor.tm_hour == 13 and kor.tm_min <= 54
        lunch = kor.tm_hour == 13 and kor.tm_min >= 56
        lunch2 = kor.tm_hour == 14 and kor.tm_min <= 4
        lunchend = kor.tm_hour == 14 and kor.tm_min >= 5
        lef = lunchend or kor.tm_hour == 15
        lunchend2 = kor.tm_hour == 16 and kor.tm_min <= 54
        dinner = kor.tm_hour == 16 and kor.tm_min >= 56
        dinner2 = kor.tm_hour == 17 and kor.tm_min <= 14
        # 특정 시간에 매크로 시작
        # if kor.tm_hour == 9 and kor.tm_min == 50:
#아침출석        
        if morning or morning2:
            if macro == True :
                os.system("c:/aischool/1.url")

                
                macro = False
        if mef or morningend2:
            if macroOn == True : 
                macro = True
                macroOn = False

#점심출석
        if lunch or lunch2:
            if macro == True :
                os.system("c:/aischool/2.url")

                macro = False
                macroOn = True
        if lef or lunchend2:
            if macroOn == True:
                macro = True
                macroOn = False

#오후 출석
        if dinner or dinner2:
            if macro == True :
                os.system("c:/aischool/3.url")

                macro = False

#5시 30분 이후 프로그램 종료
        if kor.tm_hour == 17 and kor.tm_min >= 30 or kor.tm_hour >= 18:
            os.system('taskkill /f /im aischool2.exe')
#3시 과제제출
        if kor.tm_hour == 15:
            if macro2 == True :
                os.system("c:/aischool/4.url")
                macro2 = False
#주말종료
        if kor.tm_wday == 5 or kor.tm_wday == 6:
            os.system('taskkill /f /im aischool2.exe')

        # if kor.tm_mday == 12 or kor.tm_mday == 18 or kor.tm_mday == 19 or kor.tm_mday == 11 or kor.tm_mday == 25 or kor.tm_mday == 26:
        #     os.system('taskkill /f /im aischool2.exe')

        # 타이머 설정  (1초마다, 콜백함수)
        timer = Timer(1, self.showtime)
        timer.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    w.show()
    sys.exit(app.exec_())