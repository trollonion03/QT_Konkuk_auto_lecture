# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(465, 429)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 5, 301, 20))
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.text_id = QTextEdit(self.centralwidget)
        self.text_id.setObjectName(u"text_id")
        self.text_id.setGeometry(QRect(75, 30, 150, 20))
        self.text_id.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_id.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_pw = QTextEdit(self.centralwidget)
        self.text_pw.setObjectName(u"text_pw")
        self.text_pw.setGeometry(QRect(75, 55, 150, 20))
        self.text_pw.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_pw.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 50, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 55, 70, 20))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 30, 100, 20))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 81, 445, 3))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(240, 55, 215, 20))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 80, 70, 20))
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(10, 100, 445, 255))
        self.button_Exit = QPushButton(self.centralwidget)
        self.button_Exit.setObjectName(u"button_Exit")
        self.button_Exit.setGeometry(QRect(375, 360, 80, 24))
        self.button_Start = QPushButton(self.centralwidget)
        self.button_Start.setObjectName(u"button_Start")
        self.button_Start.setGeometry(QRect(290, 360, 80, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 465, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uac74\uad6d\ub300\ud559\uad50 Ecampus \uc790\ub3d9\uc218\uac15", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uc81c\uc678\ud560 \ud56d\ubaa9", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Log:", None))
        self.button_Exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.button_Start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

