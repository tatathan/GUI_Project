# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(769, 694)
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"#leftMenuSubContainer{\n"
"	background-color: #16191d;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #2c313c;\n"
"	border: none;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #2c313c;\n"
"	border-left: 2px solid #3e3e42;\n"
"	border-bottom: 2px solid #3e3e42;\n"
"}\n"
"\n"
"#frame_6 QPushButton:hover {\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"#frame_4 QPushButton, #frame_8 QPushButton, popupNotificationSubContainer QPushButton{\n"
"	border-radius: 70px;\n"
"}\n"
"#rightMenuContainer{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#centerMenuSubContainer, #rightMenuSubContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"#fr"
                        "ame_4, #frame_8, #popupNotificationSubContainer{\n"
"	background-color: #16191d;\n"
"	border-radius: 10px;\n"
"}\n"
"#headerContainer, #footerContainer{\n"
"	background-color: #2c313c;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy)
        self.leftMenuContainer.setMinimumSize(QSize(0, 0))
        self.leftMenuContainer.setMaximumSize(QSize(60, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuSubContainer.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setFont(font)
        self.homeBtn.setStyleSheet(u"background-color: #2c313c;  border-left: 2px solid #3e3e42; border-bottom: 3px solid #3e3e42;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.dataBtn = QPushButton(self.frame_2)
        self.dataBtn.setObjectName(u"dataBtn")
        self.dataBtn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dataBtn.setIcon(icon2)
        self.dataBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.dataBtn)

        self.reportBtn = QPushButton(self.frame_2)
        self.reportBtn.setObjectName(u"reportBtn")
        self.reportBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reportBtn.setIcon(icon3)
        self.reportBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.reportBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon5)
        self.infoBtn.setIconSize(QSize(30, 30))
        self.infoBtn.setAutoDefault(False)
        self.infoBtn.setFlat(False)

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.leftMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QWidget(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(0, 0))
        self.centerMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.centerMenuSubContainer.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.centerMenuCloseBtn = QPushButton(self.frame_4)
        self.centerMenuCloseBtn.setObjectName(u"centerMenuCloseBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.centerMenuCloseBtn.sizePolicy().hasHeightForWidth())
        self.centerMenuCloseBtn.setSizePolicy(sizePolicy3)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.centerMenuCloseBtn.setIcon(icon7)
        self.centerMenuCloseBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.centerMenuCloseBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.centerMenuSubContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Noto Sans")
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_2.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamily(u"Noto Sans")
        font2.setPointSize(13)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setMinimumSize(QSize(0, 45))
        self.headerContainer.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(30, 30))
        self.label_5.setPixmap(QPixmap(u":/images/crown.svg"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5, 0, Qt.AlignVCenter)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setFamily(u"Noto Sans")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_6.setFont(font3)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(135, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.NotiBtn = QPushButton(self.frame_6)
        self.NotiBtn.setObjectName(u"NotiBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.NotiBtn.sizePolicy().hasHeightForWidth())
        self.NotiBtn.setSizePolicy(sizePolicy4)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.NotiBtn.setIcon(icon8)
        self.NotiBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.NotiBtn)

        self.moreBtn = QPushButton(self.frame_6)
        self.moreBtn.setObjectName(u"moreBtn")
        sizePolicy4.setHeightForWidth(self.moreBtn.sizePolicy().hasHeightForWidth())
        self.moreBtn.setSizePolicy(sizePolicy4)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreBtn.setIcon(icon9)
        self.moreBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.moreBtn)

        self.profileBtn = QPushButton(self.frame_6)
        self.profileBtn.setObjectName(u"profileBtn")
        sizePolicy4.setHeightForWidth(self.profileBtn.sizePolicy().hasHeightForWidth())
        self.profileBtn.setSizePolicy(sizePolicy4)
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn.setIcon(icon10)
        self.profileBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.profileBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(130, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        sizePolicy4.setHeightForWidth(self.minimizeBtn.sizePolicy().hasHeightForWidth())
        self.minimizeBtn.setSizePolicy(sizePolicy4)
        self.minimizeBtn.setStyleSheet(u":hover {\n"
"	background-color: #16191d;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon11)
        self.minimizeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        sizePolicy4.setHeightForWidth(self.restoreBtn.sizePolicy().hasHeightForWidth())
        self.restoreBtn.setSizePolicy(sizePolicy4)
        self.restoreBtn.setStyleSheet(u":hover {\n"
"	background-color: #16191d;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon12)
        self.restoreBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy2.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy2)
        self.closeBtn.setMouseTracking(False)
        self.closeBtn.setStyleSheet(u":hover {\n"
"  ;\n"
"	background-color: red;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon13)
        self.closeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy)
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        sizePolicy.setHeightForWidth(self.mainContentsContainer.sizePolicy().hasHeightForWidth())
        self.mainContentsContainer.setSizePolicy(sizePolicy)
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.stackedWidget_3 = QStackedWidget(self.mainContentsContainer)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.verticalLayout_16 = QVBoxLayout(self.pageHome)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_10 = QLabel(self.pageHome)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setFrameShadow(QFrame.Plain)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setMargin(11)

        self.verticalLayout_16.addWidget(self.label_10)

        self.stackedWidget_3.addWidget(self.pageHome)
        self.pageDataAnalysis = QWidget()
        self.pageDataAnalysis.setObjectName(u"pageDataAnalysis")
        self.verticalLayout_17 = QVBoxLayout(self.pageDataAnalysis)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_11 = QLabel(self.pageDataAnalysis)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)

        self.stackedWidget_3.addWidget(self.pageDataAnalysis)
        self.pageReports = QWidget()
        self.pageReports.setObjectName(u"pageReports")
        self.verticalLayout_18 = QVBoxLayout(self.pageReports)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_12 = QLabel(self.pageReports)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_12)

        self.stackedWidget_3.addWidget(self.pageReports)

        self.verticalLayout_15.addWidget(self.stackedWidget_3)


        self.horizontalLayout_8.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QWidget(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(0, 0))
        self.rightMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.rightMenuContainer.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.rightMenuCloseBtn = QPushButton(self.frame_8)
        self.rightMenuCloseBtn.setObjectName(u"rightMenuCloseBtn")
        self.rightMenuCloseBtn.setIcon(icon7)
        self.rightMenuCloseBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.rightMenuCloseBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.stackedWidget_2 = QStackedWidget(self.rightMenuSubContainer)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_8)

        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_14 = QVBoxLayout(self.page_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.page_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)

        self.stackedWidget_2.addWidget(self.page_5)

        self.verticalLayout_12.addWidget(self.stackedWidget_2)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QWidget(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        sizePolicy5 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.popupNotificationContainer.sizePolicy().hasHeightForWidth())
        self.popupNotificationContainer.setSizePolicy(sizePolicy5)
        self.popupNotificationContainer.setMinimumSize(QSize(0, 0))
        self.popupNotificationContainer.setMaximumSize(QSize(0, 0))
        self.verticalLayout_19 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.popupNotificationSubContainer.setMinimumSize(QSize(0, 0))
        self.popupNotificationSubContainer.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.popupNotificationSubContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_14 = QLabel(self.popupNotificationSubContainer)
        self.label_14.setObjectName(u"label_14")
        font4 = QFont()
        font4.setFamily(u"Noto Sans")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_14.setFont(font4)

        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)

        self.notiCloseBtn = QPushButton(self.popupNotificationSubContainer)
        self.notiCloseBtn.setObjectName(u"notiCloseBtn")
        self.notiCloseBtn.setMinimumSize(QSize(45, 45))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notiCloseBtn.setIcon(icon14)
        self.notiCloseBtn.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.notiCloseBtn, 0, 1, 1, 1)

        self.frame_9 = QFrame(self.popupNotificationSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy6)
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_13, 0, Qt.AlignVCenter)


        self.gridLayout.addWidget(self.frame_9, 1, 0, 1, 1)


        self.verticalLayout_19.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_10.addWidget(self.popupNotificationContainer, 0, Qt.AlignHCenter)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.footerContainer.setMinimumSize(QSize(0, 43))
        self.footerContainer.setMaximumSize(QSize(16777215, 43))
        self.horizontalLayout_11 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.footerContainer)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy7)
        self.frame_10.setMaximumSize(QSize(16777215, 43))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_15)


        self.horizontalLayout_11.addWidget(self.frame_10)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(10, 10))
        self.sizeGrip.setMaximumSize(QSize(40, 40))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.sizeGrip)


        self.verticalLayout_10.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.infoBtn.setDefault(False)
        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.dataBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
#endif // QT_CONFIG(tooltip)
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
#if QT_CONFIG(tooltip)
        self.reportBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Reports", None))
#endif // QT_CONFIG(tooltip)
        self.reportBtn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.centerMenuCloseBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.centerMenuCloseBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Program Name", None))
        self.NotiBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
#if QT_CONFIG(tooltip)
        self.rightMenuCloseBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.rightMenuCloseBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"More..", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
#if QT_CONFIG(tooltip)
        self.notiCloseBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close notification", None))
#endif // QT_CONFIG(tooltip)
        self.notiCloseBtn.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Copyright", None))
    # retranslateUi

