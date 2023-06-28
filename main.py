# This Python file uses the following encoding: utf-8
# uic -g python mainwindow.ui -o mainwindow.py
import sys
import winreg
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtCore import Slot
from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_Exit.clicked.connect(self.onExitClick)
        self.ui.button_Start.clicked.connect(self.onStartClick)
        self.ui.textEdit_2.append(f"크롬 브라우저 ({self.get_chrome_version()})")

    def get_chrome_version(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon")
            value, _ = winreg.QueryValueEx(key, "version")
            self.ui.button_Start.setDisabled(False)
            return value
        except Exception as e:
            self.ui.button_Start.setDisabled(True)            
            return "크롬 브라우저 정보를 가져오는 도중 오류가 발생하였습니다. 크롬 브라우저 설치 여부를 확인해 주세요"


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
