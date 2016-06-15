#-*- coding: euc-kr -*-

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json
import datetime
import os
import sys
import weather_fnc
import spam
from PyQt5 import QtCore, QtGui, QtWidgets


urllib = urllib2
sendMail = weather_fnc.sendMail
getdata_weather = weather_fnc.getdata_weather
getdata_weather2 = weather_fnc.getdata_weather2
getdata_living = weather_fnc.getdata_living
getvalue_weather = weather_fnc.getvalue_weather
getvalue_weather2 = weather_fnc.getvalue_weather2
getvalue_living = weather_fnc.getvalue_living
geticon = weather_fnc.geticon
now = datetime.datetime.now()
year = now.strftime('%Y')
month = now.strftime('%m')
day = now.strftime('%d')
hour = now.strftime('%H')
minutes = now.strftime('%M')
second = now.strftime('%S')
first_weather = getdata_weather('weather', 'current', 'minutely')
first_json = json.loads(first_weather)
first_weather = first_json["weather"]
first_weather = first_weather["minutely"]
first_weather = first_weather["sky"]
first_weather = first_weather["code"]
temp = getvalue_weather(getdata_weather('weather', 'current', 'minutely'), "temperature")["tc"]
tmax = getvalue_weather(getdata_weather('weather', 'current', 'minutely'), "temperature")["tmax"]
tmin = getvalue_weather(getdata_weather('weather', 'current', 'minutely'), "temperature")["tmin"]
humidity = getvalue_weather(getdata_weather('weather', 'current', 'minutely'), "humidity")
wdir = getvalue_weather(getdata_weather('weather', 'current', 'minutely'), "wind")["wdir"]
wspd = getvalue_weather(getdata_weather('weather', 'current', 'minutely'), "wind")["wspd"]
rain = getvalue_weather(getdata_weather('weather', 'current', 'minutely'), "precipitation")["type"]
rainontime = getvalue_weather(getdata_weather('weather', 'current', 'minutely'), "precipitation")["sinceOntime"]
rain_per = getvalue_weather2(getdata_weather2('weather', 'forecast', '3days'), "precipitation")["prob4hour"]
sky = getvalue_weather(getdata_weather('weather', 'current', 'minutely'), "sky")["name"]
pressure = getvalue_weather(getdata_weather('weather', 'current', 'minutely'), "pressure")["surface"]
lightning = getvalue_weather(getdata_weather('weather', 'current', 'minutely'), "lightning")
uvindex = getvalue_living(getdata_living('weather', 'windex', 'uvindex'), "uvindex", "day01")["index"]
uvindex_info = getvalue_living(getdata_living('weather', 'windex', 'uvindex'), "uvindex", "day01")["comment"]
uvindex_image = getvalue_living(getdata_living('weather', 'windex', 'uvindex'), "uvindex", "day01")["imageUrl"]
dust_value = getvalue_living(getdata_living('weather', "null", 'dust'), "dust", "value")
dust_grade = getvalue_living(getdata_living('weather', "null", 'dust'), "dust", "grade")
weather_info = "상대습도 : " + humidity + "\n풍향 : " + wdir + "\n풍속 : " + wspd + "\n강수확률 : " + rain_per + "\n강수상태 : " + rain + "\n강수량 : " + rainontime + "\n하늘상태 : " + sky + "\n현재기압(Ps) : " + pressure + "\n낙뢰유무 : " + lightning + "\n자외선지수 : " + uvindex + "\n<자외선 도움말>\n" + uvindex_info[:15] + "\n" + uvindex_info[15:] + "\n미세먼지농도(㎍/㎥) : " + dust_value + "\n미세먼지등급 : " + dust_grade
if rain == '0':
    rain = "현상없음"
elif rain == '1':
    rain = "비"
elif rain == '2':
    rain = "비/눈"
elif rain == '3':
    rain = "눈"
else:
    rain = "현상없음"
    
if lightning == '0':
    lightning = "없음"
elif lightning == '1':
    lightning = "있음"
else:
    lightning = "현상없음"

        
class Ui_MainWindow(object):    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Weather")
        MainWindow.resize(600, 265)
        MainWindow.setMinimumSize(QtCore.QSize(600, 265))
        MainWindow.setMaximumSize(QtCore.QSize(600, 265))
        MainWindow.setSizeIncrement(QtCore.QSize(600, 265))
        MainWindow.setBaseSize(QtCore.QSize(600, 265))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_icon = QtWidgets.QLabel(self.centralwidget)
        self.label_icon.setGeometry(QtCore.QRect(70, 10, 151, 141))
        self.label_icon.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_icon.setText("")
        self.label_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.label_icon.setObjectName("label_icon")
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(280, 0, 201, 221))
        self.label_info.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_info.setText(weather_info)
        self.label_info.setObjectName("label_info")
        self.email_input = QtWidgets.QTextEdit(self.centralwidget)
        self.email_input.setGeometry(QtCore.QRect(280, 220, 261, 21))
        self.email_input.setAcceptDrops(True)
        self.email_input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.email_input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.email_input.setDocumentTitle("")
        self.email_input.setObjectName("email_input")
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(544, 220, 51, 21))
        self.send_button.setObjectName("send_button")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(10, 160, 261, 31))
        self.label_date.setText(year + "년 " + month + "월 " + day + "일")
        self.label_date.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_date.setObjectName("label_date")
        self.label_tempmax = QtWidgets.QLabel(self.centralwidget)
        self.label_tempmax.setGeometry(QtCore.QRect(490, 10, 101, 61))
        self.label_tempmax.setText("최고기온\n" + tmax + "°C")
        self.label_tempmax.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tempmax.setObjectName("label_tempmax")
        self.label_tempmin = QtWidgets.QLabel(self.centralwidget)
        self.label_tempmin.setGeometry(QtCore.QRect(490, 150, 101, 61))
        self.label_tempmin.setText("최저기온\n" + tmin + "°C")
        self.label_tempmin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tempmin.setObjectName("label_tempmin")
        self.label_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_temp.setGeometry(QtCore.QRect(490, 80, 101, 61))
        self.label_temp.setText("현재기온\n" + temp + "°C")
        self.label_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp.setObjectName("label_temp")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(10, 190, 261, 51))
        self.label_time.setText(datetime.datetime.now().strftime('%H:%M:%S'))
        self.label_time.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_time.setObjectName("label_time")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setToolTip("")
        self.statusbar.setStatusTip("")
        self.statusbar.setWhatsThis("")
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Weather", "날씨"))
        self.email_input.setPlaceholderText(_translate("Weather", "이메일"))
        self.send_button.setText(_translate("Weather", "전송"))
        self.send_button.clicked.connect(self.btn_clicked)
        pixmap = QtGui.QPixmap(os.getcwd() + '/icon/' + geticon(first_weather) + '.png').scaled(self.label_icon.size(), QtCore.Qt.KeepAspectRatio)
        #pixmap = QtGui.QPixmap(os.getcwd() + '/icon/' + weather_icon + '.png').scaled(self.label_icon.size(), QtCore.Qt.KeepAspectRatio)
        self.label_icon.setPixmap(pixmap)
        self.label_icon.show()
        
    def btn_clicked(self):
        email = self.email_input.toPlainText()
        if email:
            text = year + "년 " + month + "월 " + day + "일" + " 현재날씨\n\n" + "최고기온\n" + tmax + "°C\n" + "최저기온\n" + tmin + "°C\n" + "현재기온\n" + temp + "°C\n\n\n" + weather_info
            sendMail(email, text)
        else:
            print("이메일 서버 연결성공")
    
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        self._update_timer = QtCore.QTimer()
        self._update_timer.timeout.connect(self.update_time)
        self._update_timer.start(100) # milliseconds

        self._update_timer1 = QtCore.QTimer()
        self._update_timer1.timeout.connect(self.update_label)
        self._update_timer1.start(10000) # milliseconds

    def update_time(self):
        self.label_date.setText(year + "년 " + month + "월 " + day + "일")
        self.label_time.setText(datetime.datetime.now().strftime('%H:%M:%S'))
        
    def update_label(self):
        self.label_tempmax.setText("최고기온\n" + tmax + "°C")
        self.label_tempmin.setText("최저기온\n" + tmin + "°C")        
        self.label_temp.setText("현재기온\n" + temp + "°C")
        weather_info = "상대습도 : " + humidity + "\n풍향 : " + wdir + "\n풍속 : " + wspd + "\n강수확률 : " + rain_per + "\n강수상태 : " + rain + "\n강수량 : " + rainontime + "\n하늘상태 : " + sky + "\n현재기압(Ps) : " + pressure + "\n낙뢰유무 : " + lightning + "\n자외선지수 : " + uvindex + "\n<자외선 도움말>\n" + uvindex_info[:15] + "\n" + uvindex_info[15:] + "\n미세먼지농도(㎍/㎥) : " + dust_value + "\n미세먼지등급 : " + dust_grade
        self.label_info.setText(weather_info)
        pixmap = QtGui.QPixmap(os.getcwd() + '/icon/' + geticon(first_weather) + '.png').scaled(self.label_icon.size(), QtCore.Qt.KeepAspectRatio)
        self.label_icon.setPixmap(pixmap)
        self.label_icon.show()


#json_data = json.loads(getdata('weather', 'current', 'minutely'))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
