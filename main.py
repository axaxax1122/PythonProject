#-*- coding: euc-kr -*-

import string;
import math;
import urllib2;
import datetime;
import xml.etree.ElementTree as ET;
#from HTMLParser import HTMLParser;
from BeautifulSoup import BeautifulSoup;

SecretKey = "mEAnmdN%2Bf1E5XE8MqgBsfJyEbA1iuef6fvdNK6bksEttkdkaWqrJNE7JlWmnpLOAK0Z9737YqRgpH56F5nSnQQ==";
MainUrl = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?ServiceKey={0}&base_date={1}&base_time={2}&nx={3}&ny={4}";
now = datetime.datetime.now();
count =0;
max = 0;

def parsing(category, fcstValue):
    if category=="POP":
        return "����Ȯ�� : {0}%".format(int(fcstValue));
    elif category=="PTY":
        if fcstValue == 0:
            return "�������� : ����";
        elif fcstValue == 1:
            return "�������� : ��";
        elif fcstValue == 2:
            return "�������� : ��/��";
        else:
            return "�������� : ��";
    elif category=="SKY":
        if fcstValue == 1:
            return "�ϴû��� : ����"
        elif fcstValue == 2:
            return "�ϴû��� : ��������"
        elif fcstValue == 3:
            return "�ϴû��� : ��������"
        else:
            return "�ϴû��� : �帲"
    elif category=="UUU":
        if fcstValue < 4:
            return "(����)�ٶ��� ���ϴ�";
        elif fcstValue < 9:
            return "(����)�ٶ��� �ణ ���ϴ�";
        elif fcstValue < 14:
            return "(����)�ٶ��� ���ϴ�";
        else:
            return "(����)�ٶ��� �ſ� ���ϴ�";
    elif category=="VVV":
        if fcstValue < 4:
            return "(����)�ٶ��� ���ϴ�";
        elif fcstValue < 9:
            return "(����)�ٶ��� �ణ ���ϴ�";
        elif fcstValue < 14:
            return "(����)�ٶ��� ���ϴ�";
        else:
            return "(����)�ٶ��� �ſ� ���ϴ�";
    elif category=="VEC":
        converted = int(((fcstValue + 22.5 * 0.5) / 22.5));
        if converted == 0:
            return "ǳ�� : N";
        elif converted == 1:
            return "ǳ�� : NNE";
        elif converted == 2:
            return "ǳ�� : NE";
        elif converted == 3:
            return "ǳ�� : ENE";
        elif converted == 4:
            return "ǳ�� : E";
        elif converted == 5:
            return "ǳ�� : ESE";
        elif converted == 6:
            return "ǳ�� : SE";
        elif converted == 7:
            return "ǳ�� : SSE";
        elif converted == 8:
            return "ǳ�� : S";
        elif converted == 9:
            return "ǳ�� : SSW";
        elif converted == 10:
            return "ǳ�� : SW";
        elif converted == 11:
            return "ǳ�� : WSW";
        elif converted == 12:
            return "ǳ�� : W";
        elif converted == 13:
            return "ǳ�� : WNW";
        elif converted == 14:
            return "ǳ�� : NW";
        elif converted == 15:
            return "ǳ�� : NNW";
        elif converted == 16:
            return "ǳ�� : N";
    elif category =="WAV":
        return "�İ� : {0}m".format(fcstValue);
    elif category == "REH":
        return "���� : {0}%".format(int(fcstValue));
    elif category == "T3H":
        return "3 �ð� ��� : {0}��".format(int(fcstValue));
    elif category == "R06":
        return "6 �ð� ������ : {0}mm".format(int(fcstValue));
    elif category == "S06":
        return "6 �ð� ������ : {0}cm".format(int(fcstValue));
    elif category == "TMX":
        return "�� �ְ� ��� : {0}��".format(int(fcstValue));
    elif category == "TMN":
        return "�� ���� ��� : {0}��".format(int(fcstValue));
    return "{0} : ���� ����({1})".format(category, fcstValue);
def GetBaseTime():
    time = int('{:%H%M}'.format(now));
    if time < 230:
        return -1;
    elif time < 530:
        return "0200";
    elif time < 830:
        return "0500";
    elif time < 1130:
        return "0800";
    elif time < 1430:
        return "1100";
    elif time < 2030:
        return "1400";
    elif time < 2330:
        return "2000";
    else:
        return "2300";
def grid(v1, v2) :
  
    RE = 6371.00877 
    GRID = 5.0      
    SLAT1 = 30.0    
    SLAT2 = 60.0    
    OLON = 126.0    
    OLAT = 38.0    
    XO = 43
    YO = 136
 
    DEGRAD = math.pi / 180.0
    RADDEG = 180.0 / math.pi
 
    re = RE / GRID;
    slat1 = SLAT1 * DEGRAD
    slat2 = SLAT2 * DEGRAD
    olon = OLON * DEGRAD
    olat = OLAT * DEGRAD
  
    sn = math.tan(math.pi * 0.25 + slat2 * 0.5) / math.tan(math.pi * 0.25 + slat1 * 0.5)
    sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
    sf = math.tan(math.pi * 0.25 + slat1 * 0.5)
    sf = math.pow(sf, sn) * math.cos(slat1) / sn
    ro = math.tan(math.pi * 0.25 + olat * 0.5)
    ro = re * sf / math.pow(ro, sn);
    rs = {};
 
    ra = math.tan(math.pi * 0.25 + (v1) * DEGRAD * 0.5)
    ra = re * sf / math.pow(ra, sn)
 
    theta = v2 * DEGRAD - olon
    if theta > math.pi :
        theta -= 2.0 * math.pi
    if theta < -math.pi :
        theta += 2.0 * math.pi
    theta *= sn
    rs['x'] = math.floor(ra * math.sin(theta) + XO + 0.5)
    rs['y'] = math.floor(ro - ra * math.cos(theta) + YO + 0.5)
    return str(rs["x"]).split('.')[0], str(rs["y"]).split('.')[0];
def elementToString(element):
    s = element.text or ""
    for sub_element in element:
        s += ET.tostring(sub_element)
    s += element.tail
    return s
def GetSubText(elem, str):
    for elem2 in elem.iter(tag=str):
        return elem2.text;
    return "";
def Do(url):
    response = urllib2.urlopen(url);
    html = response.read();
    xmldoc = ET.fromstring(html);
    itemList = xmldoc.iter(tag='item');
    good = "";
    for elem in itemList:
        if good == "":
            print("====================");
            good = GetSubText(elem, 'fcstTime');
        elif good != GetSubText(elem, 'fcstTime'):
            print("====================");
            good = GetSubText(elem, 'fcstTime');

        Category = GetSubText(elem, 'category');
        fcstValue = GetSubText(elem, 'fcstValue');
        print("[{0}]{1} => {2}".format(GetSubText(elem, 'baseDate'), GetSubText(elem, 'fcstTime'), parsing(Category, float(fcstValue))));
    return;
def ConvertToNum(str):
    x = list(str);
    o = list();
    for c in x:
        if c == '.':
            o.append(c);
        else:
            try:
                n = int(c);
                o.append(c);
            except:
                n = 0;
    s = "";
    for c in o:
        s+=c;
    return s;
def main():
    x = 37.566826005485716;
    y = 126.9786567859313;
    #lon, lat = swap1(x, y, map);
    output = grid(x, y);
    x1 = output[0];
    y1 = output[1];
    #print(x1 +" "+y1);
    #print('{:%Y%m%d}'.format(now)); #dateformat
    baseDate = '{:%Y%m%d}'.format(now);
    baseTime = GetBaseTime();
    responsed = urllib2.Request("http://www.findip.kr/where.php", headers={'User-Agent': 'Mozilla/5.0'});
    response = urllib2.urlopen(responsed)
    #print(html);
    html = response.read();
    soup = BeautifulSoup(html);
    itemList = soup.findAll('ul', attrs={'class':'green'});
    for elem in itemList:
            li = elem.findAll('li');
            #print(ConvertToNum(str(li[4])))
            x = float(ConvertToNum(str(li[4]))); #float(str(li[4]).replace("����(Latitude) : ", "").replace("<li>", "").replace("</li>", ""));
            y = float(ConvertToNum(str(li[5]))); #float(str(li[5]).replace("�浵(Longitude) : ", "").replace("<li>", "").replace("</li>", ""));
            #print(str(x) + " " + str(y));
    
    if baseTime == -1:
        yesterday = now - datetime.timedelta(1); 
        baseDate = '{:%Y%m%d}'.format(yesterday);
        baseTime = "2300";
    url = MainUrl.format(SecretKey, baseDate, baseTime, x1, y1);
    response = urllib2.urlopen(url);
    html = response.read();
    xmldoc = ET.fromstring(html);
    itemList = xmldoc.iter(tag='body');
    for elem in itemList:
        max = int(GetSubText(elem, 'totalCount'));
    _url = "{0}&numOfRows={1}".format(url, max);
    #print(_url);
    Do(_url);
    return;
def pMenu():
    print("P : ���� ����");
    i = raw_input();
    return i;

i = pMenu();
if i == "P" or i == "p":
    main();
a = raw_input();