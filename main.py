# This Python file uses the following encoding: utf-8
# uic -g python mainwindow.ui -o mainwindow.py
# Author: Trollonion03
import sys, threading, winreg, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Slot, QObject, Signal
from mainwindow import Ui_MainWindow

URL = 'http://ecampus.konkuk.ac.kr/ilos/main/main_form.acl'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_Exit.clicked.connect(self.onExitClick)
        self.ui.button_Start.clicked.connect(self.onStartClick)
        self.title = ""
        self.num = 0

    def get_chrome_version(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon")
            value, _ = winreg.QueryValueEx(key, "version")
            self.ui.button_Start.setDisabled(False)
            self.ui.textEdit_2.append(f"Chrome ({value}) 확인됨")
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
            self.ui.textEdit_2.append(f'ChromeDriver ({version}) 확인됨')
            driver.quit()
        except Exception as e:
            self.ui.textEdit_2.append("ChromeDriver 버전을 가져오는 도중 오류가 발생하였습니다.")
            self.ui.button_Start.setDisabled(True)
            driver.quit()
        finally:
            driver.quit()

        driver.quit()
        print("이건 왜 안죽니")

    @Slot()
    def onStartClick(self):
        self.id = self.ui.text_id.toPlainText()
        self.pw = self.ui.text_pw.text()
        self.bypass = self.ui.textEdit.toPlainText().split("\n")

        if self.id != '' and self.id != '':
            m_thread = threading.Thread(target=self.macroHandler)
            m_thread.start()
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("경고")
            msgBox.setText("ID, 비밀번호를 입력해 주세요")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.exec()
                
    @Slot()
    def onExitClick(self):
        QApplication.quit()
        sys.exit()

    def macroHandler(self):
        self.ui.textEdit_2.append("자동수강을 시작합니다.")
        
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless') #for release
        driver = webdriver.Chrome(options=chrome_options)

        driver.get(url = URL)

        test = driver.find_element(By.CLASS_NAME,'login-btn-color')
        test.click()

        driver.find_element(By.ID,"usr_id").send_keys(self.id)
        driver.find_element(By.ID,"usr_pwd").send_keys(self.pw)
        driver.find_element(By.ID,"login_btn").click()

        driver.find_elements(By.CLASS_NAME,"message_item")[1].click()
        element = driver.find_elements(By.CLASS_NAME,"todo_category")[0]
        driver.execute_script("arguments[0].click();", element)
        lists = driver.find_elements(By.CLASS_NAME,"todo_wrap.on")

        lists_s = len(lists) - 1

        for i in range(lists_s+1) :
            list_ss = lists[num].find_element(By.CLASS_NAME,"todo_title")
            title = str(list_ss.get_attribute('textContent').split("\n        ")[1].split("\n")[0].split("[온라인강의] ")[1])
            self.ui.textEdit_2.append(title)
            if(title in self.bypass):
                num += 1
                continue
            else:
                self.ui.textEdit_2.append(f'titles : {title}')
                driver.execute_script("arguments[0].click();", lists[num])
                driver.implicitly_wait(10)
                views = driver.find_elements(By.CLASS_NAME,"site-mouseover-color")
                pers = driver.find_elements(By.ID,"per_text")
                if(len(pers) == 0):
                    views = driver.find_element(By.CLASS_NAME,"site-mouseover-color")
                    pers = driver.find_element(By.ID,"per_text")
                    self.watch(pers, views)
                    self.ui.textEdit_2.append("성공")
                else:
                    for k in range(len(pers)) :
                        self.watch(pers[k],views[k])
                        driver.implicitly_wait(10)
                        # 오류남
                        views = driver.find_elements(By.CLASS_NAME,"site-mouseover-color")
                        pers = driver.find_elements(By.ID,"per_text")
                        ibox2 = driver.find_elements(By.CLASS_NAME,"ibox2")
                time.sleep(5)
            driver.find_elements(By.CLASS_NAME,"message_item")[1].click()
            element = driver.find_elements(By.CLASS_NAME,"todo_category")[0]
            driver.execute_script("arguments[0].click();", element)
            lists = driver.find_elements(By.CLASS_NAME,"todo_wrap.on")
            num = 0
        driver.quit()
        self.ui.textEdit_2.append("자동수강을 완료하였습니다.")


    def watch(self, el1, el2, driver):
        ppppp = el2.find_element(By.XPATH,"..").find_element(By.XPATH,"..").find_element(By.XPATH,"..").find_element(By.XPATH,"..").find_element(By.XPATH,"..").find_element(By.XPATH,"..").find_elements(By.XPATH,".//*")[0]
        try:
            subtitle = ppppp.text.split("차시 ")[1]
        except Exception:
            subtitle = self.title
        
        if el1.text != "100%" and subtitle not in self.bypass:
            driver.implicitly_wait(10)
            parent = el1.find_element(By.XPATH,"..")
            child = parent.find_elements(By.XPATH,".//*")[4]
            t1 = child.text.split(" / ")[2]
            t2 = child.text.split(" / ")[0]
            sec1 = 0
            sec2 = 0

            # 들은 수강 시간 구하기
            tmp = 1
            s = child.text.split(" / ")[0]
            for t in s.split(':')[::-1]:
                sec1 += int(t) * tmp
                tmp *= 60
            
            # 총 수강 시간 구하기
            tmp = 1
            s = child.text.split(" / ")[2]
            for t in s.split(':')[::-1]:
                sec2 += int(t) * tmp
                tmp *= 60

            sec = sec2 - sec1
            # 4분 단위로 끊는게 정확함
            sec = (sec // 60 // 4 + 1) * 4 * 60

            el2.click()
            time.sleep(15)
            self.ui.textEdit_2.append("Time out")
            self.ui.textEdit_2.append(time.ctime(time.time()),",현재 강의:",subtitle,", 강의 시간:",t1,"(",sec2,")"," 현재 수강 시간:",t2,"(",sec1,")")
            self.ui.textEdit_2.append(f'{sec}초 : {sec // 3600}시 {sec % 3600 // 60}분 {sec % 3600 % 60}초 만큼 기다립니다.')
            #수정
            time.sleep(sec)
            # time.sleep(sec+15)
            # time.sleep(3)
            
            self.ui.textEdit_2.append('find closing driver')
            try:
                driver.find_element(By.ID,"close_").click()
                time.sleep(2)
                alert = Alert(driver)
                alert.accept()
                self.ui.textEdit_2.append("alert accepted")
            except:
                self.ui.textEdit_2.append("no alert - error excepted")
            self.ui.textEdit_2.append(f"Closing Lecture - {subtitle}")        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    t1 = threading.Thread(target=window.checkWebDriver)
    t1.start()

    sys.exit(app.exec())