#-*- coding: euc-kr -*-

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json
import datetime
import smtplib
from email.mime.text import MIMEText


urllib = urllib2
appkey = "b60cf560-bc58-3d04-8a79-a5993221d22d"
now = datetime.datetime.now()
hour = now.strftime('%H')
if hour >= "18" and hour <= "4":
    time_h = "D"
else:
    time_h = "N"

def sendMail(email, text) :
    HOST = 'smtp.gmail.com'   # smtp 호스트 주소
    PORT = '587'   # smtp 포트 주소
    me = 'axaxax11222@gmail.com'     # 보내는 사람 메일 주소
    passwd = '921209ap!!'
    you = email  # 받는 사람 메일 주소
    contents = text

    msg = MIMEText(contents, _charset='euc-kr')
    msg['Subject'] = '날씨'
    msg['From'] = me
    msg['To'] = you

    s = smtplib.SMTP(HOST, PORT)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(me, passwd)
    s.sendmail(me, [you], msg.as_string())
    s.quit()

def getdata_weather(content, value, option):
    url = "http://apis.skplanetx.com/%s/%s/%s?version=1&lat=37.566826005485716&lon=126.9786567859313&city=1&county=1&village=1&stnid=108" % (content, value, option)
    req = urllib.Request(urllib.quote(url,'/:?=&'))
    req.add_header("appKey", appkey)
    response = urllib.urlopen(req)
    end = response.read().decode().replace("[","").replace("]","")
    return end

def getdata_weather2(content, value, option):
    url = "http://apis.skplanetx.com/%s/%s/%s?version=1&lat=37.566826005485716&lon=126.9786567859313&city=1&county=1&village=1&foretxt=N" % (content, value, option)
    req = urllib.Request(urllib.quote(url,'/:?=&'))
    req.add_header("appKey", appkey)
    response = urllib.urlopen(req)
    end = response.read().decode().replace("[","").replace("]","")
    return end

def getdata_living(content, value, option):
    if value == "null":
        url = "http://apis.skplanetx.com/%s/%s?version=1&lat=37.566826005485716&lon=126.978656785931" % (content, option)
    else:
        url = "http://apis.skplanetx.com/%s/%s/%s?version=1&lat=37.566826005485716&lon=126.978656785931" % (content, value, option)
    req = urllib.Request(urllib.quote(url,'/:?=&'))
    req.add_header("appKey", appkey)
    response = urllib.urlopen(req)
    end = response.read().decode().replace("[","").replace("]","")
    return end

def geticon(weather):
    weather = weather[5:]
    if weather == "00":
        return '38'
    elif weather == "01":
        if time_h == "N":
            return '01'
        else:
            return '08'
    elif weather == "02":
        if time_h == "N":
            return '02'
        else:
            return '09'       
    elif weather == "03":
        if time_h == "N":
            return '03'
        else:
            return '10'
    elif weather == "04":
        if time_h == "N":
            return '12'
        else:
            return '40'
    elif weather == "05":
        if time_h == "N":
            return '13'
        else:
            return '41'
    elif weather == "06":
        if time_h == "N":
            return '14'
        else:
            return '42'
    elif weather == "07":
        return '18'
    elif weather == "08":
        return '21'
    elif weather == "09":
        return '32'
    elif weather == "10":
        return '04'
    elif weather == "11":
        return '29'
    elif weather == "12":
        return '26'
    elif weather == "13":
        return '27'
    elif weather == "14":
        return '28'

def getvalue_weather(dic, value):
    dic = json.loads(dic)
    dic = dic["weather"]
    dic = dic["minutely"]
    if value=="station":
        return dic["station"]
    elif value=="wind":
        return dic["wind"]
    elif value=="precipitation":
        return dic["precipitation"]
    elif value=="sky":
        return dic["sky"]
    elif value=="rain":
        return dic["rain"]
    elif value=="temperature":
        return dic["temperature"]
    elif value=="humidity":
        return dic["humidity"]
    elif value=="pressure":
        return dic["pressure"]
    elif value=="lightning":
        return dic["lightning"]
    elif value=="timeObservation":
        return dic["timeObservation"]
    else:
        return "정보없음"

def getvalue_weather2(dic, value):
    dic = json.loads(dic)
    dic = dic["weather"]
    dic = dic["forecast3days"]
    dic = dic["fcst3hour"]
    if value=="wind":
        return dic["wind"]
    elif value=="precipitation":
        return dic["precipitation"]
    elif value=="sky":
        return dic["sky"]
    elif value=="temperature":
        return dic["temperature"]
    elif value=="humidity":
        return dic["humidity"]
    else:
        return "정보없음"
def getvalue_living(dic, option, value):
    dic = json.loads(dic)
    dic = dic["weather"]
    if option=="uvindex":
        dic = dic["wIndex"]
        dic = dic["uvindex"]
        if value=="grid":
            return dic["grid"]
        elif value=="day00":
            return dic["day00"]
        elif value=="day01":
            return dic["day01"]
        elif value=="day02":
            return dic["day02"]
        else:
            return "정보없음"
    elif option=="dust":
        dic = dic["dust"]
        dic = dic["pm10"]
        if value=="value":
            return dic["value"]
        elif value=="grade":
            return dic["grade"]
        else:
            return "정보없음"
    elif option=="wctIndex":
        dic = dic["wIndex"]
        dic = dic["wctIndex"]
        if value=="current":
            return dic["current"]
        elif value=="forecast":
            return dic["forecast"]
        else:
            return "정보없음"
    elif option=="thIndex":
        dic = dic["wIndex"]
        dic = dic["thIndex"]
        if value=="current":
            return dic["current"]
        elif value=="forecast":
            return dic["forecast"]
        else:
            return "정보없음"
