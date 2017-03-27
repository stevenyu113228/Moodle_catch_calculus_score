import requests
import os
from bs4 import BeautifulSoup
from multiprocessing import Queue #包成EXE要多import這個

moodleLoginURL = 'http://moodle.ntust.edu.tw/login/index.php'
moodleCalculusURL = 'http://moodle.ntust.edu.tw/grade/report/user/index.php?id=11795'
moodleLogoutURL = ''
res = requests.session()
payload = {'username':'','password':''}
score = []
title = []
print()
def userdata():
    try:
        f = open('D://pwd.txt','r')
        a = str(f.read())
        payload['username'] = str(a[9:a.find('password:')-1])
        payload['password'] = str(a[a.find('password:')+9:])
        f.close()
    except:
        payload['username'] = input('UserName : ')
        payload['password'] = input('Password : ')

def login():
    res.post(moodleLoginURL,data = payload)

def getscore():
    a = res.get(moodleCalculusURL)
    soup = BeautifulSoup(a.text,"html.parser")
    alltable = soup.findAll('table')[0]
    usertitle = str(soup.find('h2'))
    usertitle = usertitle[4:usertitle.find('</')]
    print(usertitle)
    for n in alltable.findAll('td',{'class':'level2 leveleven item b1b itemcenter column-grade'}):
        n = str(n)
        n = n[n.find('>')+1:n.find('</')]
        score.append(n)
    for c in alltable.findAll('th',{'class':'level2 leveleven item b1b column-itemname'}):
        c = str(c)
        c = c[c.find('"/')+3:c.find('</a></th>')]
        title.append(c)
        
def printScore():
    for a in range(len(title)):
        print(title[a]+ " : "+score[a])
        

userdata()
login()
getscore()
printScore()
os.system("pause")