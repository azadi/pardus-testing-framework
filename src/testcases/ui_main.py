# -*- coding: utf-8 -*-

#
# Created: Thu Aug 12 15:04:59 2010
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(601, 603)
        self.group_box = QtGui.QGroupBox(Dialog)
        self.group_box.setGeometry(QtCore.QRect(10, 10, 581, 391))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.group_box.setPalette(palette)
        self.group_box.setFlat(False)
        self.group_box.setObjectName("group_box")
        self.text_edit = QtGui.QTextEdit(self.group_box)
        self.text_edit.setEnabled(False)
        self.text_edit.setGeometry(QtCore.QRect(10, 70, 561, 321))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.text_edit.setFont(font)
        self.text_edit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.text_edit.setObjectName("text_edit")
        self.package_label = QtGui.QLabel(self.group_box)
        self.package_label.setGeometry(QtCore.QRect(13, 26, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.package_label.setFont(font)
        self.package_label.setObjectName("package_label")
        self.type_label = QtGui.QLabel(self.group_box)
        self.type_label.setGeometry(QtCore.QRect(13, 50, 121, 16))
        self.type_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.type_label.setObjectName("type_label")
        self.text_observation = QtGui.QPlainTextEdit(Dialog)
        self.text_observation.setEnabled(False)
        self.text_observation.setGeometry(QtCore.QRect(40, 480, 531, 70))
        self.text_observation.setObjectName("text_observation")
        self.clear_button = QtGui.QPushButton(Dialog)
        self.clear_button.setEnabled(False)
        self.clear_button.setGeometry(QtCore.QRect(50, 560, 51, 25))
        self.clear_button.setObjectName("clear_button")
        self.next_button = QtGui.QPushButton(Dialog)
        self.next_button.setGeometry(QtCore.QRect(490, 560, 71, 25))
        self.next_button.setObjectName("next_button")
        self.quit_button = QtGui.QPushButton(Dialog)
        self.quit_button.setEnabled(False)
        self.quit_button.setGeometry(QtCore.QRect(350, 560, 71, 25))
        self.quit_button.setObjectName("quit_button")
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(22, 420, 555, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setEnabled(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.yes_button = QtGui.QRadioButton(self.layoutWidget)
        self.yes_button.setEnabled(False)
        self.yes_button.setCheckable(True)
        self.yes_button.setChecked(True)
        self.yes_button.setObjectName("yes_button")
        self.gridLayout.addWidget(self.yes_button, 0, 5, 1, 1)
        self.unable_button = QtGui.QRadioButton(self.layoutWidget)
        self.unable_button.setEnabled(False)
        self.unable_button.setObjectName("unable_button")
        self.gridLayout.addWidget(self.unable_button, 0, 11, 1, 1)
        self.label_observation = QtGui.QLabel(self.layoutWidget)
        self.label_observation.setEnabled(False)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_observation.setFont(font)
        self.label_observation.setObjectName("label_observation")
        self.gridLayout.addWidget(self.label_observation, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 6, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 10, 1, 1)
        self.no_button = QtGui.QRadioButton(self.layoutWidget)
        self.no_button.setEnabled(False)
        self.no_button.setChecked(False)
        self.no_button.setObjectName("no_button")
        self.gridLayout.addWidget(self.no_button, 0, 8, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 4, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 3, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 7, 1, 1)
        self.save_button = QtGui.QPushButton(Dialog)
        self.save_button.setEnabled(False)
        self.save_button.setGeometry(QtCore.QRect(420, 560, 71, 25))
        self.save_button.setObjectName("save_button")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.yes_button, QtCore.SIGNAL("clicked(bool)"), self.text_observation.setDisabled)
        QtCore.QObject.connect(self.clear_button, QtCore.SIGNAL("clicked()"), self.text_observation.clear)
        QtCore.QObject.connect(self.yes_button, QtCore.SIGNAL("clicked(bool)"), self.label_observation.setDisabled)
        QtCore.QObject.connect(self.quit_button, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QObject.connect(self.no_button, QtCore.SIGNAL("clicked(bool)"), self.text_observation.setEnabled)
        QtCore.QObject.connect(self.no_button, QtCore.SIGNAL("clicked(bool)"), self.label_observation.setEnabled)
        QtCore.QObject.connect(self.unable_button, QtCore.SIGNAL("clicked(bool)"), self.text_observation.setEnabled)
        QtCore.QObject.connect(self.unable_button, QtCore.SIGNAL("clicked(bool)"), self.label_observation.setEnabled)
        QtCore.QObject.connect(self.yes_button, QtCore.SIGNAL("clicked(bool)"), self.clear_button.setDisabled)
        QtCore.QObject.connect(self.unable_button, QtCore.SIGNAL("clicked(bool)"), self.clear_button.setEnabled)
        QtCore.QObject.connect(self.no_button, QtCore.SIGNAL("clicked(bool)"), self.clear_button.setEnabled)
        QtCore.QObject.connect(self.unable_button, QtCore.SIGNAL("clicked()"), self.text_observation.setFocus)
        QtCore.QObject.connect(self.no_button, QtCore.SIGNAL("clicked()"), self.text_observation.setFocus)
        QtCore.QObject.connect(self.text_edit, QtCore.SIGNAL("textChanged()"), self.yes_button.click)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.yes_button, self.unable_button)
        Dialog.setTabOrder(self.unable_button, self.text_observation)
        Dialog.setTabOrder(self.text_observation, self.next_button)
        Dialog.setTabOrder(self.next_button, self.clear_button)
        Dialog.setTabOrder(self.clear_button, self.quit_button)
        Dialog.setTabOrder(self.quit_button, self.text_edit)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Pardus Testing Framework", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_button.setText(QtGui.QApplication.translate("Dialog", "&Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.next_button.setText(QtGui.QApplication.translate("Dialog", "&Start", None, QtGui.QApplication.UnicodeUTF8))
        self.quit_button.setText(QtGui.QApplication.translate("Dialog", "&Finish", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Did the above test work as expected?", None, QtGui.QApplication.UnicodeUTF8))
        self.yes_button.setText(QtGui.QApplication.translate("Dialog", "&Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.unable_button.setText(QtGui.QApplication.translate("Dialog", "&Unable to peform this test", None, QtGui.QApplication.UnicodeUTF8))
        self.label_observation.setText(QtGui.QApplication.translate("Dialog", "Enter your observation: ", None, QtGui.QApplication.UnicodeUTF8))
        self.no_button.setText(QtGui.QApplication.translate("Dialog", "&No", None, QtGui.QApplication.UnicodeUTF8))
        self.save_button.setText(QtGui.QApplication.translate("Dialog", "&Save", None, QtGui.QApplication.UnicodeUTF8))

