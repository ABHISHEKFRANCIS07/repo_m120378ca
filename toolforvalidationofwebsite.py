


from Tkinter import *
import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize
from PyQt4 import QtCore, QtGui
import sys
import requests
import re
import os
import lxml
import enchant
from enchant.checker import SpellChecker






try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(391, 402)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 110, 81, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(70, 40, 171, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 40, 61, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 190, 141, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 131, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 110, 171, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 260, 101, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 300, 111, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 260, 131, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 40, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Get url (Depth)", None))
        self.label.setText(_translate("Form", "ENTER URL", None))
        self.pushButton_2.setText(_translate("Form", "Spell Check ", None))
        self.label_2.setText(_translate("Form", "CHECK SPELLING ERROR", None))
        self.label_3.setText(_translate("Form", "DEPTH", None))
        self.label_4.setText(_translate("Form", "SPELL CHECK A PAGE", None))
        self.pushButton_3.setText(_translate("Form", "Page Check", None))
        self.pushButton_4.setText(_translate("Form", "Get url", None))

        self.pushButton_4.clicked.connect(self.GetUrl)
        self.pushButton.clicked.connect(self.GetUrlDepth)
        self.pushButton_2.clicked.connect(self.Extraction)
        self.pushButton.clicked.connect(self.DepthSearch)
        self.pushButton_3.clicked.connect(self.PageCheck)





    def GetUrl(self,Form):


        
        a=self.lineEdit.text()
        b=str(a)
        #print b
        url = b
        
        br = mechanize.Browser()
        m = open('C:\Ptext\surl.txt','w')
        c=open('C:\Ptext\url.txt','w')
                    # create lists for the urls in que and visited urls
        urls = [url]
        visited = [url]
        level = [str(0)]
        # level[0]=0
        # Since the amount of urls in the list is dynamic
        # we just let the spider go until some last url didn't
        # have new ones on the webpage
        c1=0
        j=1
        level_no=0
        temp=0
        c.write("level 0 \n")
        l=level[0]+"->"+url
        print "level 0"
        print l
        c.write(l + "\n")
        
        while len(urls)>0:
            try:
                br.open(urls[0])
                urls.pop(0)
                k=0
                
                    
                z=level[c1]
                c1=c1+1
                #print (c1)
            

                

                for link in br.links():
                    newurl = urlparse.urljoin(link.base_url,link.url)
                     #print newurl
                    if newurl not in visited and url in newurl:
                        k=k+1
                        visited.append(newurl)
                        y = str(z)+'.'+str(k)
                        print y
                        level.append(y)
                        urls.append(newurl)
                        count=str(level[j]).count('.')
                        
                        
                            
                            
                            
                        
                        
                        if count>temp :
                            print "level "+str(count)
                            c.write("level "+str(count)+"\n")
                            temp = count
                        l=level[j]+"->"+newurl
                        
                        
                        print l
                        j=j+1
                        #print newurl
                        m.write(newurl + "\n")
                        c.write(l + "\n")
                        #c.write(str(newurl) + "\n")

            except:
                print "error"
                urls.pop(0)
                
                

        c.close()
        m.close()
        #f.close()







       


    def PageCheck(self,Form):
        chkr = SpellChecker("en_US")
        d = enchant.Dict("en_US")
        
        k=self.lineEdit_3.text()
        er=[]
        br=[]
        a=requests.get(str(k))
        soup=BeautifulSoup(a.content)

        htmlfile=urllib.urlopen(str(k))
        htmltext=htmlfile.read()
        type(soup)

        ar=[]

        for i in re.findall(r'(?s)<!--(.*?)-->', htmltext):
            br.append(i)

        for j in re.findall(r'(?s)".*?"', htmltext):
            ar.append(i)



        qt=0
        while qt<len(ar):
            htmltext = re.sub('(?s)<!.*?>', '', htmltext)
            qt=qt+1

        st=0
        while st<len(ar):
            htmltext = re.sub('(?s)".*?"', '', htmltext)
            st=st+1
        
        at=0
        while at<len(ar):
            htmltext = re.subn(r'<(script).*?</\1>(?s)', '', htmltext)[0]
            at=at+1

        ct=0
        while ct<len(ar):
            htmltext = re.subn(r'<(style).*?</\1>(?s)', '', htmltext)[0]
            ct=ct+1


        

                        
        soup=BeautifulSoup(htmltext)

        p=soup.get_text()
        spell_check=re.split(r'\W*',p)
        
        #q=q+1
        print "Words Found =>",
        print len(spell_check)
        #print spell_check
        
        a=0
        for spell in spell_check:
            uni=spell_check[a]
            c=uni.encode("ascii","ignore")
            chkr.set_text(c)
            try:
                for err in chkr:
                    t=err.word
                    if err.word[0].islower()==True:
                        if t not in er:
                            print err.word
                            print d.suggest(err.word)
                    
                            er.append(t)
                            #print er
                       
                       #print "False",err.word
                       #print d.suggest(err.word)
                    

            except:
                print ""
    
            a=a+1


    def Close(self,Form):
        app = QtGui.QApplication(sys.argv)
        sys.exit(app.exec_())
        


    def DepthSearch():
        c=self.lineEdit.text()
        a=self.lineEdit.text()
        m=str(c)
        n=str(a)

        
       
        
        
        




    


    


    def Extraction(self,Form):
        chkr = SpellChecker("en_US")
        d = enchant.Dict("en_US")
        fob = open('C:\Ptext\surl.txt','r+')
        nm =open('C:/Ptext/report.txt','w') 
        qwe=re.split(r'\s*',fob.read())
        #r=requests.get("http://nitc.ac.in/cec/index.html")
        #soup=BeautifulSoup(r.content)
        q=0
        m=0
        er=[]
        ar=[]
        n=len(qwe)
        for link in qwe:
            a=0
            #print qwe[n-1]
            print qwe[q]
            #print len(qwe)

            if q<=len(qwe)-2:
                #print "o"
                try:
                    if str(qwe[q]).split(".")[-1].lower()\
                       not in ["pdf", "ppt", "doc", "jpg", "img","png", "gif"]:
                        #print q
                        a=requests.get(str(qwe[q]))
                        soup=BeautifulSoup(a.content)
                        htmlfile=urllib.urlopen(str(qwe[q]))
                        htmltext=htmlfile.read()
                        #type(soup)
                        
                        ar=[]

                        for i in re.findall(r'(?s)<!--(.*?)-->', htmltext):
                            ar.append(i)



                        qt=0
                        while qt<len(ar):
                            htmltext = re.sub('(?s)<!.*?>', '', htmltext)
                            qt=qt+1

                        for j in re.findall(r'(?s)".*?"', htmltext):
                            ar.append(i)



                        qt=0
                        while qt<len(ar):
                            htmltext = re.sub('(?s)<!.*?>', '', htmltext)
                            qt=qt+1

                            st=0
                        while st<len(ar):
                            htmltext = re.sub('(?s)".*?"', '', htmltext)
                            st=st+1
        
                        at=0
                        while at<len(ar):
                            htmltext = re.subn(r'<(script).*?</\1>(?s)', '', htmltext)[0]
                            at=at+1

                        ct=0
                        while ct<len(ar):
                            htmltext = re.subn(r'<(style).*?</\1>(?s)', '', htmltext)[0]
                            ct=ct+1                    

                        
                        soup=BeautifulSoup(htmltext)
                        
                          
                        p=soup.get_text()
                        spell_check=re.split(r'\W*',p)
                        #print "qrt"
                        #print spell_check
                        #print spell_check[3]
                        q=q+1
                        nm.write("\n"+ qwe[q] + "\n")
                        print "Words Found =>",
                        print len(spell_check)
                        #print type(soup)
                        #print spell_check
                        '''
                        while a<=len(spell_check)-1:
                        a=a+1
                        print "mmmmmmmm"'''


                        a=0

                        for spell in spell_check:
                            
                            uni=spell_check[a]
                            c=uni.encode("ascii","ignore")
                            chkr.set_text(c)
                            try:
                                for err in chkr:
                                    t=err.word
                                    if err.word[0].islower()==True:
                                        sa=d.suggest(err.word)
                                        if t not in er:
                                            print err.word
                                            print d.suggest(err.word)
                                            nm.write("\n" + err.word  + "=> SuggestedWords =")
                                            for w in sa:
                                                nm.write(" "+ w + ":")
                                            
                    
                                            er.append(t)
                

                                        

                                    
                                        #print "False",err.word
                        
                                    

                            except:
                                print ""
    
                            a=a+1
                            

                            '''
                            if d.check(str(spell_check[a]))==False:
                            print spell_check[a]
                            a=a+1
                            '''
    
                        
                            

                        
                            
                    
                    else :
                        q=q+1
                    
                    

                    
                except IndexError:
                    print ""
                    q=q+1


        fob.close()
                
            
            
        
        




    def GetUrlDepth(self,Form):



        sd = open('C:\Ptext\surl.txt','w')
        xc = open('C:\Ptext\url.txt','w')
        c=self.lineEdit_2.text()   #depth
        m=str(c)
        a=self.lineEdit.text()      #url
        b=str(a)
        #print b
        url = b
        br = mechanize.Browser()
        c=open('C:\Python27\SAM\in.txt','w')
                    # create lists for the urls in que and visited urls
        urls = [url]
        visited = [url]
        level = [str(0)]
        # level[0]=0
        # Since the amount of urls in the list is dynamic
        # we just let the spider go until some last url didn't
        # have new ones on the webpage
        c1=0
        j=1
        level_no=0
        temp=0
        c.write("level 0 \n")
        l=level[0]+"->"+url
        print "level 0"
        print l
        c.write(l + "\n")
        
        while len(urls)>0:
            try:
                br.open(urls[0])
                urls.pop(0)
                k=0
                
                    
                z=level[c1]
                c1=c1+1
                

                

                for link in br.links():
                    newurl = urlparse.urljoin(link.base_url,link.url)
                     #print newurl
                    if newurl not in visited and url in newurl:
                        k=k+1
                        visited.append(newurl)
                        y = str(z)+'.'+str(k)
                        level.append(y)
                        urls.append(newurl)
                        count=str(level[j]).count('.')
                        #r=int(c)+1
                        #m=int(m)+1
                        #print m
                        if str(count)==str(m):
                            #quit()
                            os._exit(1)
                        
                            
                            
                            
                        
                        
                        if count>temp :
                            print "level "+str(count)
                            c.write("level "+str(count)+"\n")
                            temp = count
                        l=level[j]+"->"+newurl
                        print l
                        j=j+1
                        #print newurl
                        xc.write(l + "\n")
                        sd.write(newurl + "\n")
                        #c.write(str(newurl) + "\n")

            except:
                print "error"
                print l
                urls.pop(0)
                
                

        sd.close()
        xc.close()
        
                    
        
        
  
    
if __name__== '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    
    sys.exit(app.exec_())

