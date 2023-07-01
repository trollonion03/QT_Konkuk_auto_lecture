# This Python file uses the following encoding: utf-8
# uic -g python mainwindow.ui -o mainwindow.py
import sys, threading, winreg
from selenium import webdriver
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot, QObject, Signal
from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
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
        self.get_chrome_version()

        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless') #동작 확인 위해 비활성화
            driver = webdriver.Chrome(options=chrome_options)
            capabilities = driver.capabilities
            version = capabilities['chrome']['chromedriverVersion'].split(' ')[0]
            self.ui.textEdit_2.append(f'ChromeDriver({version}) 확인됨')
        except Exception as e:
            self.ui.textEdit_2.append("ChromeDriver 버전을 가져오는 도중 오류가 발생하였습니다.")
            version = '-1'
        finally:
            driver.quit()

        driver.quit()

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
    
    t1 = threading.Thread(target=window.checkWebDriver)
    t1.start()

    sys.exit(app.exec())


