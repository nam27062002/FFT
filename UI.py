from PyQt5 import QtGui, QtWidgets, QtCore
import sys, os
import UIStart,UIStatistical
import Training
import ShowSignal,Percent
from ShowEigenvectors import Process as showVector
class UI:
    def __init__(self):
        self.ui = ""
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.URL = ""
        self.training512 = Training.Process(512)
        self.training256 = Training.Process(256)
        self.training128 = Training.Process(128)
        self.statistical512 = Percent.statistical(self.training512)
        self.statistical256 = Percent.statistical(self.training256)
        self.statistical128 = Percent.statistical(self.training128)
    def maxPercent(self):
        arr = [self.statistical512.Percent,self.statistical256.Percent,self.statistical128.Percent]
        max = -1
        index = -1
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]
                index = i
        if index == 0:
            return self.statistical512.ARR
        if index == 1:
            return self.statistical256.ARR
        if index == 2:
            return self.statistical128.ARR
    def __UIStart(self):
        self.ui = UIStart.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.ui.frame.setAcceptDrops(True)
        self.ui.frame.dragEnterEvent = self.DragEnter
        self.ui.frame.dropEvent = self.dropEvent
        self.ui.pushButton.clicked.connect(self.showVector)
        self.ui.pushButton_2.clicked.connect(self.__UIStatistical)
        self.ui.frame.mousePressEvent = self.openFolder
    def openFolder(self,e):
        directory = QtWidgets.QFileDialog.getOpenFileName(filter="Images (*.wav)")
        if directory[0] != "":
            self.showASignal(directory[0])
    def __UIStatistical(self):
        self.ui = UIStatistical.Ui_MainWindow()
        arrPercent = [round(self.statistical128.Percent,2),round(self.statistical256.Percent,2),round(self.statistical512.Percent,2)]
        self.ui.setupUi(self.MainWindow,arrPercent,self.maxPercent())
        self.ui.pushButton.clicked.connect(self.__UIStart)
        self.MainWindow.show()
    def showVector(self):
        showVector(self.training512.getEigenvectors()).show()
    def DragEnter(self, event):
        x = event.mimeData().urls()[0].toLocalFile()
        s = ""
        for i in range(len(x) - 1, -1, -1):
            if x[i] != ".":
                s = x[i] + s
            else:
                break
        if s == "wav":
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        x = event.mimeData().urls()[0].toLocalFile()
        s = ""
        for i in range(len(x) - 1, -1, -1):
            if x[i] != ".":
                s = x[i] + s
            else:
                break
        if s == "wav":
            event.accept()
            self.showASignal(x)
        else:
            event.ignore()
    def showASignal(self,url):
        ShowSignal.Process(url,self.training512.compare(url)[1]).show()
    def loop(self):
        self.__UIStart()
        sys.exit(self.app.exec_())
