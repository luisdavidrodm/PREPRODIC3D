# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'densidad_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_densidad_window(object):
    def setupUi(self, densidad_window):
        if not densidad_window.objectName():
            densidad_window.setObjectName(u"densidad_window")
        densidad_window.resize(501, 497)
        self.gridLayout_2 = QGridLayout(densidad_window)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_2 = QGroupBox(densidad_window)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(self.groupBox_2)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout.addWidget(self.lineEdit_4)


        self.verticalLayout.addWidget(self.groupBox_5)


        self.gridLayout_2.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.groupBox_3 = QGroupBox(densidad_window)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget_2 = QListWidget(self.groupBox_3)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout_2.addWidget(self.listWidget_2)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout = QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 0, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 1, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 1, 2, 1, 1)

        self.lineEdit_10 = QLineEdit(self.groupBox_4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout.addWidget(self.lineEdit_10, 1, 3, 1, 1)

        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 2, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.groupBox_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 2, 2, 1, 1)

        self.lineEdit_9 = QLineEdit(self.groupBox_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout.addWidget(self.lineEdit_9, 2, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_4)


        self.gridLayout_2.addWidget(self.groupBox_3, 2, 1, 1, 1)

        self.groupBox = QGroupBox(densidad_window)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_3)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)

        self.checkBox = QCheckBox(densidad_window)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setContextMenuPolicy(Qt.CustomContextMenu)
        self.checkBox.setLayoutDirection(Qt.LeftToRight)
        self.checkBox.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox, 1, 0, 1, 2)


        self.retranslateUi(densidad_window)

        QMetaObject.connectSlotsByName(densidad_window)
    # setupUi

    def retranslateUi(self, densidad_window):
        densidad_window.setWindowTitle(QCoreApplication.translate("densidad_window", u"Densidad - PrePRODIC3D", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("densidad_window", u"Regiones", None))
        self.pushButton.setText(QCoreApplication.translate("densidad_window", u"Agregar una regi\u00f3n", None))
        self.pushButton_3.setText(QCoreApplication.translate("densidad_window", u"Eliminar \u00faltima regi\u00f3n", None))
        self.groupBox_5.setTitle("")
        self.label_5.setText(QCoreApplication.translate("densidad_window", u"Densidad local", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("densidad_window", u"Conformaci\u00f3n de la regi\u00f3n", None))
        self.pushButton_2.setText(QCoreApplication.translate("densidad_window", u"Agregar un \u00e1rea", None))
        self.pushButton_4.setText(QCoreApplication.translate("densidad_window", u"Eliminar \u00faltima \u00e1rea", None))
        self.groupBox_4.setTitle("")
        self.label_8.setText(QCoreApplication.translate("densidad_window", u"X", None))
        self.label_9.setText(QCoreApplication.translate("densidad_window", u"Y", None))
        self.label_10.setText(QCoreApplication.translate("densidad_window", u"Z", None))
        self.label_6.setText(QCoreApplication.translate("densidad_window", u"Inicio", None))
        self.label_7.setText(QCoreApplication.translate("densidad_window", u"Longitud", None))
        self.groupBox.setTitle(QCoreApplication.translate("densidad_window", u"Densidad general del dominio", None))
        self.label_2.setText(QCoreApplication.translate("densidad_window", u"Valor de densidad", None))
        self.label_3.setText(QCoreApplication.translate("densidad_window", u"Densidad de referencia", None))
        self.label_4.setText(QCoreApplication.translate("densidad_window", u"Temperatura de referencia", None))
        self.label.setText(QCoreApplication.translate("densidad_window", u"Condici\u00f3n", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("densidad_window", u"Valor constante", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("densidad_window", u"Dependiente de la temperatura", None))

        self.checkBox.setText(QCoreApplication.translate("densidad_window", u"Activar variables locales:", None))
    # retranslateUi

