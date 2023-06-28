# This Python file uses the following encoding: utf-8
# uic -g python mainwindow.ui -o mainwindow.py
import sys
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
    
    def onStartClick(self):
        self.id = self.ui.text_id.toPlainText()
        self.pw = self.ui.text_pw.toPlainText()
        
    @Slot()
    def onExitClick(self):
        sys.exit(app.exec())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
