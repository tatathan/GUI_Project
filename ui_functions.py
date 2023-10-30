

## ==> GUI FILE
import PySide2.QtGui
from main import *

WINDOW_SIZE = 0;

class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):

        if enable:

            # GET WIDTH
            width = self.ui.leftMenuContainer.width()
            maxExtend = maxWidth
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            #self.ui.leftMenuContainer.setMaximumWidth(maxWidth)
            self.animation = QPropertyAnimation(self.ui.leftMenuContainer, b"maximumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def toggleLeftBox(self, enable):
        if enable:
             # GET WIDTH
            width = self.ui.centerMenuContainer.width()
            maxExtend = 200
            standard = 0

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.centerMenuContainer, b"maximumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(maxExtend)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def closeLeftBox(self, enable):
        if enable:
             # GET WIDTH
            width = self.ui.centerMenuContainer.width()
            maxExtend = 200
            standard = 0

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.centerMenuContainer, b"maximumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(standard)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def changePage(self, stackedWidgetName, pageIndex):
            if stackedWidgetName == "stackedWidget_3":
                self.ui.stackedWidget_3.setCurrentIndex(pageIndex)
            elif stackedWidgetName == "stackedWidget":
                self.ui.stackedWidget.setCurrentIndex(pageIndex)
            elif stackedWidgetName == "stackedWidget_2":
                self.ui.stackedWidget_2.setCurrentIndex(pageIndex)

    def toggleRightBox(self, enable):

        if enable:
             # GET WIDTH
            width = self.ui.rightMenuContainer.width()
            maxExtend = 200
            standard = 0
            

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.rightMenuContainer, b"maximumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(maxExtend)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
    #def resize(self, event):
        #self.ui.rightMenuContainer.move(self.window() + (self.ui.rightMenuContainer.width()+10, 10))
        #self.ui.rightMenuContainer.setFla
    #def resizeEvent(self, event: QResizeEvent) -> None:
   
            

    def closeRightBox(self, enable):
        if enable:
             # GET WIDTH
            width = self.ui.rightMenuContainer.width()
            maxExtend = 200
            standard = 0

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.rightMenuContainer, b"maximumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(standard)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def toggleNotiBox(self, enable):
        newW = 600
        newH = 150

        if enable:
            height = self.ui.popupNotificationContainer.height()
            maxExtend = newH
            standard = 0

            if height == 0:
                status = 0
            else:
                status = 1


            if status == 0:
                # ANIMATION
                self.animation = QPropertyAnimation(self.ui.popupNotificationContainer, b"maximumHeight")
                self.animation.setDuration(400)
                self.animation.setStartValue(height)
                self.animation.setEndValue(maxExtend)
                self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.animation.start()
            else :
                self.animation = QPropertyAnimation(self.ui.popupNotificationContainer, b"maximumHeight")
                self.animation.setDuration(400)
                self.animation.setStartValue(height)
                self.animation.setEndValue(standard)
                self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.animation.start()

            

    def closeNotiBox(self, enable):
        if enable:
            height = self.ui.popupNotificationContainer.height()
            maxExtend = 150
            standard = 0

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.popupNotificationContainer, b"maximumHeight")
            self.animation.setDuration(400)
            self.animation.setStartValue(height)
            self.animation.setEndValue(standard)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
    
           



    def maximize_restore(self):
        global WINDOW_SIZE
        winStatus = WINDOW_SIZE
        if winStatus == 0:
            WINDOW_SIZE = 1
            self.showMaximized()
            self.ui.restoreBtn.setIcon(QtGui.QIcon(u":/icons/icons/copy.svg"))
            self.ui.restoreBtn.setToolTip("Restore Window")
        else:
            WINDOW_SIZE = 0
            self.showNormal()
            self.ui.restoreBtn.setIcon(QtGui.QIcon(u":/icons/icons/square.svg"))
            self.ui.restoreBtn.setToolTip("Maximize Window")


    def uiDefinitions(self):

        def moveWindow(event):
            if WINDOW_SIZE == 0:
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
        self.ui.headerContainer.mouseMoveEvent = moveWindow









        

