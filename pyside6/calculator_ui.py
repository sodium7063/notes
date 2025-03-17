# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLCDNumber, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if not Calculator.objectName():
            Calculator.setObjectName(u"Calculator")
        Calculator.resize(340, 392)
        self.verticalLayout_2 = QVBoxLayout(Calculator)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Caculator = QLCDNumber(Calculator)
        self.Caculator.setObjectName(u"Caculator")
        self.Caculator.setMinimumSize(QSize(0, 100))

        self.verticalLayout.addWidget(self.Caculator)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_7 = QPushButton(Calculator)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 60))

        self.horizontalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(Calculator)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 60))

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(Calculator)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 60))

        self.horizontalLayout.addWidget(self.pushButton_9)

        self.pushButton_add = QPushButton(Calculator)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setMinimumSize(QSize(0, 60))

        self.horizontalLayout.addWidget(self.pushButton_add)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_4 = QPushButton(Calculator)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(Calculator)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(Calculator)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_reduce = QPushButton(Calculator)
        self.pushButton_reduce.setObjectName(u"pushButton_reduce")
        self.pushButton_reduce.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_2.addWidget(self.pushButton_reduce)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_1 = QPushButton(Calculator)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_3.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(Calculator)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(Calculator)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_multiple = QPushButton(Calculator)
        self.pushButton_multiple.setObjectName(u"pushButton_multiple")
        self.pushButton_multiple.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_3.addWidget(self.pushButton_multiple)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_0 = QPushButton(Calculator)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_4.addWidget(self.pushButton_0)

        self.pushButton__dot = QPushButton(Calculator)
        self.pushButton__dot.setObjectName(u"pushButton__dot")
        self.pushButton__dot.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_4.addWidget(self.pushButton__dot)

        self.pushButton_cal = QPushButton(Calculator)
        self.pushButton_cal.setObjectName(u"pushButton_cal")
        self.pushButton_cal.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_4.addWidget(self.pushButton_cal)

        self.pushButton_device = QPushButton(Calculator)
        self.pushButton_device.setObjectName(u"pushButton_device")
        self.pushButton_device.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_4.addWidget(self.pushButton_device)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Calculator)

        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"\u8ba1\u7b97\u5668", None))
        self.pushButton_7.setText(QCoreApplication.translate("Calculator", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Calculator", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Calculator", u"9", None))
        self.pushButton_add.setText(QCoreApplication.translate("Calculator", u"+", None))
        self.pushButton_4.setText(QCoreApplication.translate("Calculator", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Calculator", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Calculator", u"6", None))
        self.pushButton_reduce.setText(QCoreApplication.translate("Calculator", u"-", None))
        self.pushButton_1.setText(QCoreApplication.translate("Calculator", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Calculator", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Calculator", u"3", None))
        self.pushButton_multiple.setText(QCoreApplication.translate("Calculator", u"x", None))
        self.pushButton_0.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.pushButton__dot.setText(QCoreApplication.translate("Calculator", u".", None))
        self.pushButton_cal.setText(QCoreApplication.translate("Calculator", u"\u8ba1\u7b97", None))
        self.pushButton_device.setText(QCoreApplication.translate("Calculator", u"/", None))
    # retranslateUi

