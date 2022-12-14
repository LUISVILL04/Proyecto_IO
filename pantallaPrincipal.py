# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pantallaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(638, 474)
        MainWindow.setMinimumSize(QtCore.QSize(484, 0))
        MainWindow.setMaximumSize(QtCore.QSize(638, 474))
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0         rgba(91, 91, 91, 255), stop:1 rgba(118, 118, 118, 255));\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(180, 40, 271, 31))
        self.titulo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.titulo.setStyleSheet("font: 75 20pt \"Bahnschrift\";\n"
"color: rgb(255, 255, 255);")
        self.titulo.setObjectName("titulo")
        self.boton1 = QtWidgets.QPushButton(self.centralwidget)
        self.boton1.setGeometry(QtCore.QRect(270, 130, 101, 41))
        self.boton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton1.setStyleSheet("color: white;\n"
"font: 12pt \"Bahnschrift Condensed\";\n"
"background-color: #3f3f3f;\n"
"border-radius: 10px;\n"
"border: 2px solid #54fff1;")
        self.boton1.setObjectName("boton1")
        self.boton2 = QtWidgets.QPushButton(self.centralwidget)
        self.boton2.setEnabled(True)
        self.boton2.setGeometry(QtCore.QRect(270, 220, 101, 41))
        self.boton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boton2.setMouseTracking(False)
        self.boton2.setStyleSheet("color: white;\n"
"font: 12pt \"Bahnschrift Condensed\";\n"
"background-color: #3f3f3f;\n"
"border-radius: 10px;\n"
"border: 2px solid #54fff1;")
        self.boton2.setObjectName("boton2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo.setText(_translate("MainWindow", "Optimizaci??n de modelos"))
        self.boton1.setText(_translate("MainWindow", "Maximizar"))
        self.boton2.setText(_translate("MainWindow", "Minimizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
