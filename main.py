# This Python file uses the following encoding: utf-8
# uic -g python mainwindow.ui -o mainwindow.py
import sys
import winreg
import requests
import xml.etree.ElementTree as ET
from selenium import webdriver
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtCore import Slot
from mainwindow import Ui_MainWindow

def fetch_xml_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"XML 데이터를 가져오는 중 오류가 발생했습니다: {e}")
        return None

def parse_chromedriver_info(xml_data, search):
    root = ET.fromstring(xml_data)
    ns = {"ns": "http://doc.s3.amazonaws.com/2006-03-01"}
    sParse = search.split('.')
    patch = []
    print("Dfa")
    chromedriver_info = []
    for contents in root.findall("ns:Contents", ns):
        key = contents.find("ns:Key", ns).text
        if key.endswith("chromedriver_win32.zip"):
            version = key.split("/")[0]
            parse = version.split('.')
            if parse[0] == sParse[0] and parse[1] == sParse[1] and parse[2] == sParse[2]:
                patch.append(int(parse[3]))

    patch.sort()
    chromedriver_info.append(f'{search}.{patch[-1]}')
    chromedriver_info.append(f'https://chromedriver.storage.googleapis.com/{search}.{patch[-1]}/chromedriver_win32.zip')

    return chromedriver_info

def downloadDriver():
    xml_url = "https://chromedriver.storage.googleapis.com/"
    xml_data = fetch_xml_data(xml_url)
    if xml_data:
        chromedriver_info = parse_chromedriver_info(xml_data , "114.0.5735")
        if chromedriver_info:
            print(chromedriver_info)
        else:
            print("Chromedriver 정보를 찾을 수 없습니다.")
    else:
        print("ChromeDriver 버전 데이터를 가져올 수 없습니다.")    






class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.chromeVer = self.get_chrome_version()

        self.ui.button_Exit.clicked.connect(self.onExitClick)
        self.ui.button_Start.clicked.connect(self.onStartClick)
        
    def get_chrome_version(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon")
            value, _ = winreg.QueryValueEx(key, "version")
            self.ui.button_Start.setDisabled(False)
            self.ui.textEdit_2.append(f"크롬 브라우저 ({value})")
            return value
        except Exception as e:
            self.ui.button_Start.setDisabled(True)            
            self.ui.textEdit_2.append("크롬 브라우저 정보를 가져오는 도중 오류가 발생하였습니다. 크롬 브라우저 설치 여부를 확인해 주세요")
            return "-1"

    def checkWebDriver(self):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(options=chrome_options)
            capabilities = driver.capabilities
            version = capabilities['chrome']['chromedriverVersion'].split(' ')[0]
        except Exception as e:
            self.ui.textEdit_2.append("ChromeDriver 버전을 가져오는 도중 오류가 발생하였습니다.")
            version = '-1'
        finally:
            driver.quit()

        if self.chromeVer != "-1" and version != "-1":
            verC = self.chromeVer.split('.')
            verD = version.split('.')

            if verC[0] != verD[0] and verC[1] != verD[1] and verC[2] != verD[2]:
                

    
            


    @Slot()
    def onStartClick(self):
        self.id = self.ui.text_id.toPlainText()
        self.pw = self.ui.text_pw.text()
        self.bypass = self.ui.textEdit.toPlainText().split("\n")

        self.macroHandler()
        
    @Slot()
    def onExitClick(self):
        sys.exit(app.exec())

    def macroHandler(self):
        self.ui.textEdit_2.append("running...")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


