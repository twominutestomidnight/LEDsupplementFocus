import requests

from bs4 import BeautifulSoup
import csv

with open('data.csv', newline='') as csvfile:
    data = csv.reader(csvfile)
    i = 1
    for row in data:
        comm = 'http://{}:{}@{}/Image/channels/1/Focus'.format(row[1], row[2], row[0])
        r = requests.get(comm)
        if r.status_code == 200:
            y = BeautifulSoup(r.text, features="xml")
            #print(y.prettify())
            titles = y.find_all('FocusStyle')
            for title in titles:
                if title.get_text() != "AUTO":
                    payload = '<?xml version="1.0" encoding="UTF-8"?> <Focus version="1.0" xmlns="http://www.hikvision.com/ver10/XMLSchema"><FocusStyle>AUTO</FocusStyle> </Focus>'
                    r = requests.put("http://igor_test:233Wedf8!@192.168.40.39/Image/channels/1/Focus", data = payload)
                else:
                    print("focus already  auto mod or focus unavailable on camera, row : ", i)
        else:
            print("wrong ip/login/psw, row : " , i)
        i += 1
