# -- coding: utf-8 --

# Form implementation generated from reading ui file 'MyDemoUIfile.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess as sp
import cv2 as cv
import pandas as pd
from datetime import datetime
from datetime import date
import face_recognition
import os
from csv import DictWriter
from getpass import getpass
from cvzone.PoseModule import PoseDetector

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1051, 574)
        Dialog.setStyleSheet("#VideoStream{\n"
"    background-color:\"lightblue\";\n"
"}\n"
"#DataSet{\n"
"    background-color:\"lightblue\";\n"
"}\n"
"#Dialog{\n"
"    background-color: \"white\";\n"
"}\n"
"#QPushButton::cliked{\n"
"    background-color:\"blue\";\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-630, -10, 1721, 1041))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/mycctv.jpg"))
        self.label.setObjectName("label")
        
        self.VideoStream = QtWidgets.QPushButton(Dialog)
        self.VideoStream.setGeometry(QtCore.QRect(100, 150, 141, 41))
        self.VideoStream.setObjectName("VideoStream")
        self.VideoStream.clicked.connect(self.myvideo)
        
        self.DataSet = QtWidgets.QPushButton(Dialog)
        self.DataSet.setGeometry(QtCore.QRect(100, 350, 141, 41))
        self.DataSet.setObjectName("DataSet")
        self.DataSet.clicked.connect(self.openMyFile) 

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def myvideo(self):
        cmd=["python3","newtest.py"]
        sp.Popen(cmd)
    
    def openMyFile(self):
         YourCSV=["python3","csvOpener.py"]
         sp.Popen(YourCSV)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.VideoStream.setText(_translate("Dialog", "Video Streamer"))
        self.DataSet.setText(_translate("Dialog", "Data Set"))
        
    


if _name_ == "_main_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
