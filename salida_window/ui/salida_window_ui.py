# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salida_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_salida_window(object):
    def setupUi(self, salida_window):
        if not salida_window.objectName():
            salida_window.setObjectName(u"salida_window")
        salida_window.resize(504, 452)
        self.gridLayout_3 = QGridLayout(salida_window)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(salida_window)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(u"formLayout")
        self.listWidget = QListWidget(self.groupBox_3)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.listWidget)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout = QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_2 = QLineEdit(self.groupBox_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setTristate(True)

        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 2)

        self.checkBox_2 = QCheckBox(self.groupBox_4)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 2)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_4)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_4 = QCheckBox(self.groupBox_6)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_2.addWidget(self.checkBox_4, 1, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.groupBox_6)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_2.addWidget(self.checkBox_5, 2, 0, 1, 1)

        self.checkBox_11 = QCheckBox(self.groupBox_6)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout_2.addWidget(self.checkBox_11, 4, 0, 1, 1)

        self.checkBox_8 = QCheckBox(self.groupBox_6)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout_2.addWidget(self.checkBox_8, 3, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox_6)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setTabletTracking(False)
        self.checkBox_3.setTristate(True)

        self.gridLayout_2.addWidget(self.checkBox_3, 0, 0, 1, 1)

        self.checkBox_6 = QCheckBox(self.groupBox_6)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_2.addWidget(self.checkBox_6, 2, 1, 1, 1)

        self.checkBox_9 = QCheckBox(self.groupBox_6)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout_2.addWidget(self.checkBox_9, 3, 1, 1, 1)

        self.checkBox_12 = QCheckBox(self.groupBox_6)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.gridLayout_2.addWidget(self.checkBox_12, 4, 1, 1, 1)

        self.checkBox_10 = QCheckBox(self.groupBox_6)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout_2.addWidget(self.checkBox_10, 5, 0, 1, 1)

        self.checkBox_7 = QCheckBox(self.groupBox_6)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout_2.addWidget(self.checkBox_7, 5, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.formLayout_2 = QFormLayout(self.groupBox_7)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_4 = QLineEdit(self.groupBox_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_5 = QLabel(self.groupBox_7)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_5 = QLineEdit(self.groupBox_7)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_5)


        self.horizontalLayout_2.addWidget(self.groupBox_7)


        self.verticalLayout.addWidget(self.groupBox_5)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(salida_window)

        QMetaObject.connectSlotsByName(salida_window)
    # setupUi

    def retranslateUi(self, salida_window):
        salida_window.setWindowTitle(QCoreApplication.translate("salida_window", u"Salida - PrePRODIC3D", None))
        self.groupBox.setTitle(QCoreApplication.translate("salida_window", u"Opciones de salida", None))
        self.groupBox_2.setTitle("")
        self.groupBox_3.setTitle(QCoreApplication.translate("salida_window", u"Variables", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("salida_window", u"Temperatura", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_4.setTitle(QCoreApplication.translate("salida_window", u"Puntos de monitoreo", None))
        self.lineEdit_2.setText(QCoreApplication.translate("salida_window", u"0", None))
        self.lineEdit.setText(QCoreApplication.translate("salida_window", u"0", None))
        self.checkBox.setText(QCoreApplication.translate("salida_window", u"Nodo com\u00fan", None))
        self.checkBox_2.setText(QCoreApplication.translate("salida_window", u"Distintos nodos", None))
        self.label.setText(QCoreApplication.translate("salida_window", u"X", None))
        self.label_2.setText(QCoreApplication.translate("salida_window", u"Y", None))
        self.label_3.setText(QCoreApplication.translate("salida_window", u"Z", None))
        self.lineEdit_3.setText(QCoreApplication.translate("salida_window", u"0", None))
        self.groupBox_5.setTitle("")
        self.groupBox_6.setTitle(QCoreApplication.translate("salida_window", u"Promedio en las esquinas", None))
        self.checkBox_4.setText(QCoreApplication.translate("salida_window", u"Todas las esquinas", None))
        self.checkBox_5.setText(QCoreApplication.translate("salida_window", u"(1, N1, L1)", None))
        self.checkBox_11.setText(QCoreApplication.translate("salida_window", u"(M1, N1, 1)", None))
        self.checkBox_8.setText(QCoreApplication.translate("salida_window", u"(M1, 1. L1)", None))
        self.checkBox_3.setText(QCoreApplication.translate("salida_window", u"Seleccionar esquinas", None))
        self.checkBox_6.setText(QCoreApplication.translate("salida_window", u"(1, 1, L1)", None))
        self.checkBox_9.setText(QCoreApplication.translate("salida_window", u"(M1, 1, 1)", None))
        self.checkBox_12.setText(QCoreApplication.translate("salida_window", u"(1, N1, 1)", None))
        self.checkBox_10.setText(QCoreApplication.translate("salida_window", u"(M1, N1, L1)", None))
        self.checkBox_7.setText(QCoreApplication.translate("salida_window", u"(1, 1, 1)", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("salida_window", u"Otras opciones", None))
        self.label_4.setText(QCoreApplication.translate("salida_window", u"Numero de iteraciones", None))
        self.lineEdit_4.setText(QCoreApplication.translate("salida_window", u"5", None))
        self.label_5.setText(QCoreApplication.translate("salida_window", u"\u00cdndice gr\u00e1fico", None))
    # retranslateUi

