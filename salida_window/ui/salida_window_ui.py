# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salida_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from Recursos import recursos_rc


class Ui_salida_window(object):
    def setupUi(self, salida_window):
        if not salida_window.objectName():
            salida_window.setObjectName("salida_window")
        salida_window.resize(504, 452)
        icon = QIcon()
        icon.addFile(":/Icon/icon/prodic_icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        salida_window.setWindowIcon(icon)
        self.gridLayout_3 = QGridLayout(salida_window)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QGroupBox(salida_window)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName("formLayout")
        self.lw_variables = QListWidget(self.groupBox_3)
        QListWidgetItem(self.lw_variables)
        self.lw_variables.setObjectName("lw_variables")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lw_variables)

        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.le_y = QLineEdit(self.groupBox_4)
        self.le_y.setObjectName("le_y")

        self.gridLayout.addWidget(self.le_y, 3, 1, 1, 1)

        self.le_x = QLineEdit(self.groupBox_4)
        self.le_x.setObjectName("le_x")

        self.gridLayout.addWidget(self.le_x, 2, 1, 1, 1)

        self.chb_common_node = QCheckBox(self.groupBox_4)
        self.chb_common_node.setObjectName("chb_common_node")
        self.chb_common_node.setTristate(False)

        self.gridLayout.addWidget(self.chb_common_node, 0, 0, 1, 2)

        self.chb_different_nodes = QCheckBox(self.groupBox_4)
        self.chb_different_nodes.setObjectName("chb_different_nodes")

        self.gridLayout.addWidget(self.chb_different_nodes, 1, 0, 1, 2)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName("label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.le_z = QLineEdit(self.groupBox_4)
        self.le_z.setObjectName("le_z")

        self.gridLayout.addWidget(self.le_z, 4, 1, 1, 1)

        self.horizontalLayout.addWidget(self.groupBox_4)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_4 = QCheckBox(self.groupBox_6)
        self.checkBox_4.setObjectName("checkBox_4")

        self.gridLayout_2.addWidget(self.checkBox_4, 1, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.groupBox_6)
        self.checkBox_5.setObjectName("checkBox_5")

        self.gridLayout_2.addWidget(self.checkBox_5, 2, 0, 1, 1)

        self.checkBox_11 = QCheckBox(self.groupBox_6)
        self.checkBox_11.setObjectName("checkBox_11")

        self.gridLayout_2.addWidget(self.checkBox_11, 4, 0, 1, 1)

        self.checkBox_8 = QCheckBox(self.groupBox_6)
        self.checkBox_8.setObjectName("checkBox_8")

        self.gridLayout_2.addWidget(self.checkBox_8, 3, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox_6)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.setTabletTracking(False)
        self.checkBox_3.setTristate(True)

        self.gridLayout_2.addWidget(self.checkBox_3, 0, 0, 1, 1)

        self.checkBox_6 = QCheckBox(self.groupBox_6)
        self.checkBox_6.setObjectName("checkBox_6")

        self.gridLayout_2.addWidget(self.checkBox_6, 2, 1, 1, 1)

        self.checkBox_9 = QCheckBox(self.groupBox_6)
        self.checkBox_9.setObjectName("checkBox_9")

        self.gridLayout_2.addWidget(self.checkBox_9, 3, 1, 1, 1)

        self.checkBox_12 = QCheckBox(self.groupBox_6)
        self.checkBox_12.setObjectName("checkBox_12")

        self.gridLayout_2.addWidget(self.checkBox_12, 4, 1, 1, 1)

        self.checkBox_10 = QCheckBox(self.groupBox_6)
        self.checkBox_10.setObjectName("checkBox_10")

        self.gridLayout_2.addWidget(self.checkBox_10, 5, 0, 1, 1)

        self.checkBox_7 = QCheckBox(self.groupBox_6)
        self.checkBox_7.setObjectName("checkBox_7")

        self.gridLayout_2.addWidget(self.checkBox_7, 5, 1, 1, 1)

        self.horizontalLayout_2.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName("groupBox_7")
        self.formLayout_2 = QFormLayout(self.groupBox_7)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName("label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.le_last = QLineEdit(self.groupBox_7)
        self.le_last.setObjectName("le_last")
        self.le_last.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.le_last)

        self.label_5 = QLabel(self.groupBox_7)
        self.label_5.setObjectName("label_5")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_5 = QLineEdit(self.groupBox_7)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setEnabled(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_5)

        self.horizontalLayout_2.addWidget(self.groupBox_7)

        self.verticalLayout.addWidget(self.groupBox_5)

        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(salida_window)

        QMetaObject.connectSlotsByName(salida_window)

    # setupUi

    def retranslateUi(self, salida_window):
        salida_window.setWindowTitle(QCoreApplication.translate("salida_window", "Salida - PrePRODIC3D", None))
        self.groupBox.setTitle(QCoreApplication.translate("salida_window", "Opciones de salida", None))
        self.groupBox_2.setTitle("")
        self.groupBox_3.setTitle(QCoreApplication.translate("salida_window", "Variables", None))

        __sortingEnabled = self.lw_variables.isSortingEnabled()
        self.lw_variables.setSortingEnabled(False)
        ___qlistwidgetitem = self.lw_variables.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("salida_window", "Temperatura", None))
        self.lw_variables.setSortingEnabled(__sortingEnabled)

        self.groupBox_4.setTitle(QCoreApplication.translate("salida_window", "Puntos de monitoreo", None))
        self.le_y.setText(QCoreApplication.translate("salida_window", "0", None))
        self.le_x.setText(QCoreApplication.translate("salida_window", "0", None))
        self.chb_common_node.setText(QCoreApplication.translate("salida_window", "Nodo com\u00fan", None))
        self.chb_different_nodes.setText(QCoreApplication.translate("salida_window", "Distintos nodos", None))
        self.label.setText(QCoreApplication.translate("salida_window", "X", None))
        self.label_2.setText(QCoreApplication.translate("salida_window", "Y", None))
        self.label_3.setText(QCoreApplication.translate("salida_window", "Z", None))
        self.le_z.setText(QCoreApplication.translate("salida_window", "0", None))
        self.groupBox_5.setTitle("")
        self.groupBox_6.setTitle(QCoreApplication.translate("salida_window", "Promedio en las esquinas", None))
        self.checkBox_4.setText(QCoreApplication.translate("salida_window", "Todas las esquinas", None))
        self.checkBox_5.setText(QCoreApplication.translate("salida_window", "(1, N1, L1)", None))
        self.checkBox_11.setText(QCoreApplication.translate("salida_window", "(M1, N1, 1)", None))
        self.checkBox_8.setText(QCoreApplication.translate("salida_window", "(M1, 1. L1)", None))
        self.checkBox_3.setText(QCoreApplication.translate("salida_window", "Seleccionar esquinas", None))
        self.checkBox_6.setText(QCoreApplication.translate("salida_window", "(1, 1, L1)", None))
        self.checkBox_9.setText(QCoreApplication.translate("salida_window", "(M1, 1, 1)", None))
        self.checkBox_12.setText(QCoreApplication.translate("salida_window", "(1, N1, 1)", None))
        self.checkBox_10.setText(QCoreApplication.translate("salida_window", "(M1, N1, L1)", None))
        self.checkBox_7.setText(QCoreApplication.translate("salida_window", "(1, 1, 1)", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("salida_window", "Otras opciones", None))
        self.label_4.setText(QCoreApplication.translate("salida_window", "Numero de iteraciones", None))
        self.le_last.setText(QCoreApplication.translate("salida_window", "5", None))
        self.label_5.setText(QCoreApplication.translate("salida_window", "\u00cdndice gr\u00e1fico", None))

    # retranslateUi
