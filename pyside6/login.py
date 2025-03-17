# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_Login_UI(object):
    def setupUi(self, Login_UI):
        if not Login_UI.objectName():
            Login_UI.setObjectName(u"Login_UI")
        Login_UI.resize(279, 204)
        self.centralwidget = QWidget(Login_UI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 80, 30))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 80, 30))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.userNameLineEdit = QLineEdit(self.centralwidget)
        self.userNameLineEdit.setObjectName(u"userNameLineEdit")
        self.userNameLineEdit.setGeometry(QRect(120, 30, 113, 21))
        self.passwordLineEdit = QLineEdit(self.centralwidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(120, 80, 113, 21))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 140, 75, 23))
        Login_UI.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Login_UI)
        self.statusbar.setObjectName(u"statusbar")
        Login_UI.setStatusBar(self.statusbar)

        self.retranslateUi(Login_UI)

        QMetaObject.connectSlotsByName(Login_UI)
    # setupUi

    def retranslateUi(self, Login_UI):
        Login_UI.setWindowTitle(QCoreApplication.translate("Login_UI", u"\u767b\u5f55\u754c\u9762", None))
        self.label.setText(QCoreApplication.translate("Login_UI", u"\u7528\u6237\u540d\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Login_UI", u"\u5bc6\u7801\uff1a", None))
        self.userNameLineEdit.setText("")
        self.userNameLineEdit.setPlaceholderText(QCoreApplication.translate("Login_UI", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("Login_UI", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("Login_UI", u"\u767b\u5f55", None))
    # retranslateUi

