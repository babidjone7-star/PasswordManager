# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Des.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 381, 280))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.writeSite = QLineEdit(self.widget)
        self.writeSite.setObjectName(u"writeSite")

        self.verticalLayout.addWidget(self.writeSite)

        self.writePasswordbu = QLineEdit(self.widget)
        self.writePasswordbu.setObjectName(u"writePasswordbu")
        self.writePasswordbu.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.writePasswordbu)

        self.AddPasswordQt = QPushButton(self.widget)
        self.AddPasswordQt.setObjectName(u"AddPasswordQt")
        self.AddPasswordQt.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"font: 9pt \"Segoe Script\";")

        self.verticalLayout.addWidget(self.AddPasswordQt)

        self.TheListOfPasswords = QTableWidget(self.widget)
        self.TheListOfPasswords.setObjectName(u"TheListOfPasswords")

        self.verticalLayout.addWidget(self.TheListOfPasswords)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.AddPasswordQt.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c....", None))
    # retranslateUi

