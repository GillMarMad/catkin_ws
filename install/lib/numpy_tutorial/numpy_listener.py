#!/usr/bin/env python3

import numpy
from numpy.core.records import array
import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy

global datas12s4, datas52s8
datas12s4 = numpy.empty(4)
datas52s8 = numpy.empty(4)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 613)
        MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Pictures/motor-boat-emoji-by-google.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 60, 511, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.s8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.s8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.s8.setAlignment(QtCore.Qt.AlignCenter)
        self.s8.setObjectName("s8")
        self.gridLayout.addWidget(self.s8, 6, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 6, 3, 1, 1)
        self.s5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.s5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.s5.setAlignment(QtCore.Qt.AlignCenter)
        self.s5.setObjectName("s5")
        self.gridLayout.addWidget(self.s5, 3, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 4, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 0, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 1, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 4, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 3, 3, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 4, 4, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem13, 5, 3, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 5, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem15, 5, 1, 1, 1)
        self.s1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.s1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.s1.setAlignment(QtCore.Qt.AlignCenter)
        self.s1.setObjectName("s1")
        self.gridLayout.addWidget(self.s1, 0, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 1, 2, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 1, 0, 1, 1)
        self.s4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.s4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.s4.setAlignment(QtCore.Qt.AlignCenter)
        self.s4.setObjectName("s4")
        self.gridLayout.addWidget(self.s4, 3, 0, 1, 1)
        self.s6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.s6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.s6.setAlignment(QtCore.Qt.AlignCenter)
        self.s6.setObjectName("s6")
        self.gridLayout.addWidget(self.s6, 5, 0, 1, 1)
        self.s7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.s7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.s7.setAlignment(QtCore.Qt.AlignCenter)
        self.s7.setObjectName("s7")
        self.gridLayout.addWidget(self.s7, 5, 4, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem18, 6, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem19, 4, 1, 1, 1)
        self.s3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.s3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.s3.setAlignment(QtCore.Qt.AlignCenter)
        self.s3.setObjectName("s3")
        self.gridLayout.addWidget(self.s3, 0, 4, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem20, 1, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem21, 6, 1, 1, 1)
        self.s2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.s2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.s2.setAlignment(QtCore.Qt.AlignCenter)
        self.s2.setObjectName("s2")
        self.gridLayout.addWidget(self.s2, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sensores"))
        self.s8.setText(_translate("MainWindow", "Sensor 8"))
        self.s5.setText(_translate("MainWindow", "Sensor 5"))
        self.s1.setText(_translate("MainWindow", "Sensor 1"))
        self.s4.setText(_translate("MainWindow", "Sensor 4"))
        self.s6.setText(_translate("MainWindow", "Sensor 6"))
        self.s7.setText(_translate("MainWindow", "Sensor 7"))
        self.s3.setText(_translate("MainWindow", "Sensor 3"))
        self.s2.setText(_translate("MainWindow", "Sensor 2"))

        rospy.init_node('SensorsNode_UI', anonymous=True)
        self.listeners1s4()
        self.subCallbacks12s4(datas12s4)
        self.listeners5s8()
        self.subCallbacks52s8(datas52s8)

    def subCallbacks12s4(self,data):
        # print(rospy.get_name(), "I heard %s"%str(data.data[0]))
        self.s1.setText(str(data.data[0]))
        self.s2.setText(str(data.data[1]))
        self.s3.setText(str(data.data[2]))
        self.s4.setText(str(data.data[3]))

    def subCallbacks52s8(self,data):
        self.s5.setText(str(data.data[0]))
        self.s6.setText(str(data.data[1]))
        self.s7.setText(str(data.data[2]))
        self.s8.setText(str(data.data[3]))

    def listeners1s4(self):
        rospy.Subscriber('s12s4', numpy_msg(Floats), self.subCallbacks12s4)

    def listeners5s8(self):
        rospy.Subscriber('s52s8', numpy_msg(Floats), self.subCallbacks52s8)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())







# def callback(data):
#     print(rospy.get_name(), "I heard %s"%str(data.data[0]))

# def listener():
#     rospy.init_node('listener')
#     rospy.Subscriber("floats", numpy_msg(Floats), callback)
#     rospy.spin()