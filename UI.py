# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledlAFcyP.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import QDoubleValidator, QIntValidator
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout,
                               QLabel, QLineEdit, QListView, QListWidget,
                               QPushButton, QSizePolicy,
                               QSpacerItem, QVBoxLayout)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(788, 713)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.layoutV_main = QVBoxLayout()
        self.layoutV_main.setObjectName(u"layoutV_main")
        self.layoutH_select = QHBoxLayout()
        self.layoutH_select.setObjectName(u"layoutH_select")
        self.layoutH_select.setContentsMargins(-1, -1, -1, 10)
        self.btn_sel_train = QPushButton(Dialog)
        self.btn_sel_train.setObjectName(u"btn_sel_train")

        self.layoutH_select.addWidget(self.btn_sel_train)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.layoutH_select.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.layoutH_select.addItem(self.verticalSpacer)

        self.btn_sel_test = QPushButton(Dialog)
        self.btn_sel_test.setObjectName(u"btn_sel_test")

        self.layoutH_select.addWidget(self.btn_sel_test)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.layoutH_select.addWidget(self.label_4)

        self.layoutV_main.addLayout(self.layoutH_select)

        self.layoutV_trainer = QVBoxLayout()
        self.layoutV_trainer.setObjectName(u"layoutV_trainer")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, 0, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_create_trainer = QPushButton(Dialog)
        self.btn_create_trainer.setObjectName(u"btn_create_trainer")
        self.btn_create_trainer.setEnabled(False)

        self.verticalLayout_3.addWidget(self.btn_create_trainer)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        validatorDouble = QDoubleValidator()
        validatorDouble.setNotation(QDoubleValidator.Notation.StandardNotation)
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setValidator(validatorDouble)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setMaximumSize(QSize(50, 50))
        self.lineEdit_2.setBaseSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setValidator(QIntValidator())
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.btn_trainer_train = QPushButton(Dialog)
        self.btn_trainer_train.setObjectName(u"btn_trainer_train")
        self.btn_trainer_train.setEnabled(False)

        self.verticalLayout.addWidget(self.btn_trainer_train)

        self.btn_trainer_test = QPushButton(Dialog)
        self.btn_trainer_test.setObjectName(u"btn_trainer_test")
        self.btn_trainer_test.setEnabled(False)

        self.verticalLayout.addWidget(self.btn_trainer_test)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.layoutV_trainer.addLayout(self.horizontalLayout)

        self.layoutV_main.addLayout(self.layoutV_trainer)

        self.layoutV_predict = QVBoxLayout()
        self.layoutV_predict.setObjectName(u"layoutV_predict")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.layoutV_predict.addWidget(self.label_2)

        self.listWidget = QListWidget(Dialog)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy3)
        self.listWidget.setMaximumSize(QSize(16777215, 50))
        self.listWidget.setViewMode(QListView.ViewMode.IconMode)

        self.layoutV_predict.addWidget(self.listWidget)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)

        self.layoutV_predict.addWidget(self.pushButton)

        self.layoutV_main.addLayout(self.layoutV_predict)

        self.layoutV_result = QVBoxLayout()
        self.layoutV_result.setObjectName(u"layoutV_result")
        self.layoutV_result.setContentsMargins(-1, -1, -1, 10)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.layoutV_result.addWidget(self.label)

        self.listWidget_2 = QListWidget(Dialog)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.layoutV_result.addWidget(self.listWidget_2)

        self.layoutV_main.addLayout(self.layoutV_result)

        self.gridLayout.addLayout(self.layoutV_main, 0, 1, 1, 1)

        # if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.pushButton)
        self.label.setBuddy(self.listWidget_2)
        # endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_sel_train.setText(QCoreApplication.translate("Dialog", u"Select training file", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"File not selected", None))
        self.btn_sel_test.setText(QCoreApplication.translate("Dialog", u"Select test file", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"File not selected", None))
        self.btn_create_trainer.setText(QCoreApplication.translate("Dialog", u"Create trainer", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Trainer does not exist", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Learning rate:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Epochs:", None))
        self.btn_trainer_train.setText(QCoreApplication.translate("Dialog", u"Train", None))
        self.btn_trainer_test.setText(QCoreApplication.translate("Dialog", u"Test", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Make a prediction:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Predict!", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Test results:", None))
    # retranslateUi
