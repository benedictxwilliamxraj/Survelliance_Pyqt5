# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import Qt, QEvent,QObject,pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget,QLabel, QMessageBox, QVBoxLayout
import qtmodern.styles
import qtmodern.windows
import numpy as np
import  cv2
import os
import time
import  json
import image_rc
import adddvr
import Inferform

class Ui_MainWindow(QWidget):
    # settings = QSettings( "gui.ini", QSettings.IniFormat )
    
    def __init__(self):
        super().__init__()

        self.filename = None
        self.isplaying = True
        # self.restore(self.settings)



    def setupUi(self, MainWindow):
        self.setMouseTracking(True)





        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Screenframe = QtWidgets.QFrame(self.centralwidget)
        self.Screenframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Screenframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Screenframe.setObjectName("Screenframe")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Screenframe)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Screenlabel = QtWidgets.QLabel(self.Screenframe)
        self.Screenlabel.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Screenlabel.setObjectName("Screenlabel")
        self.gridLayout_2.addWidget(self.Screenlabel, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.Screenframe, 0, 0, 1, 1)
        self.Screenframe.hide()
        MainWindow.setCentralWidget(self.centralwidget)

        ####Login Frame
        self.Loginframe = QtWidgets.QFrame( self.centralwidget )
        self.Loginframe.setStyleSheet( "background-image: url(:/wallpaper/wallpaper-1.jpg);" )
        self.Loginframe.setFrameShape( QtWidgets.QFrame.StyledPanel )
        self.Loginframe.setFrameShadow( QtWidgets.QFrame.Raised )
        self.Loginframe.setObjectName( "Loginframe" )
        self.LoginLabel = QtWidgets.QLabel( self.Loginframe )
        self.LoginLabel.setStyleSheet( "color: rgb(0, 0, 0);" )
        self.LoginLabel.setGeometry( QtCore.QRect( 280, 160, 151, 71 ) )
        font = QtGui.QFont()
        font.setFamily( "MS Serif" )
        font.setPointSize( 30 )
        self.LoginLabel.setFont( font )
        self.LoginLabel.setObjectName( "LoginLabel" )
        self.UsernameLabel = QtWidgets.QLabel( self.Loginframe )
        self.UsernameLabel.setGeometry( QtCore.QRect( 280, 250, 81, 21 ) )
        font = QtGui.QFont()
        font.setFamily( "Arial" )
        font.setPointSize( 10 )
        self.UsernameLabel.setFont( font )
        self.UsernameLabel.setObjectName( "UsernameLabel" )
        self.UsernameLabel.setStyleSheet( "color: rgb(0, 0, 0);" )
        self.PasswordLabel = QtWidgets.QLabel( self.Loginframe )
        self.PasswordLabel.setGeometry( QtCore.QRect( 280, 310, 81, 21 ) )
        font = QtGui.QFont()
        font.setFamily( "Arial" )
        font.setPointSize( 10 )
        self.PasswordLabel.setFont( font )
        self.PasswordLabel.setObjectName( "PasswordLabel" )
        self.PasswordLabel.setStyleSheet( "color: rgb(0, 0, 0);" )
        self.UsernameInput = QtWidgets.QLineEdit( self.Loginframe )
        self.UsernameInput.setGeometry( QtCore.QRect( 400, 250, 113, 22 ) )
        self.UsernameInput.setObjectName( "UsernameInput" )
        self.PasswordInput = QtWidgets.QLineEdit( self.Loginframe )
        self.PasswordInput.setGeometry( QtCore.QRect( 400, 310, 113, 22 ) )
        self.PasswordInput.setObjectName( "PasswordInput" )
        self.LoginButton = QtWidgets.QPushButton( self.Loginframe )
        self.LoginButton.setGeometry( QtCore.QRect( 400, 360, 93, 28 ) )
        self.LoginButton.setStyleSheet( "color: rgb(0, 0, 0);" )
        self.LoginButton.setObjectName( "LoginButton" )
        self.label = QtWidgets.QLabel( self.Loginframe )
        self.label.setGeometry( QtCore.QRect( 430, 160, 61, 71 ) )
        self.label.setText( "" )
        self.label.setPixmap( QtGui.QPixmap( ":/logo/fcritlogo.png" ) )
        self.label.setObjectName( "label" )
        self.label_2 = QtWidgets.QLabel( self.Loginframe )
        self.label_2.setGeometry( QtCore.QRect( 660, 430, 151, 91 ) )
        self.label_2.setText( "" )
        self.label_2.setPixmap( QtGui.QPixmap( ":/logo/tifr-logo.png" ) )
        self.label_2.setObjectName( "label_2" )
        self.LoginLabel_2 = QtWidgets.QLabel( self.Loginframe )
        self.LoginLabel_2.setGeometry( QtCore.QRect( 210, 70, 391, 71 ) )
        font = QtGui.QFont()
        font.setFamily( "MS Serif" )
        font.setPointSize( 30 )
        self.LoginLabel_2.setFont( font )
        self.LoginLabel_2.setObjectName( "LoginLabel_2" )
        self.LoginLabel_2.setStyleSheet( "color: rgb(0, 0, 0);" )
        self.gridLayout.addWidget( self.Loginframe, 0, 0, 1, 1 )
        # self.Loginframe.hide()

        ###Menu Bar###
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuDVR = QtWidgets.QMenu(self.menubar)
        self.menuDVR.setObjectName("menuDVR")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_DVR = QtWidgets.QAction(MainWindow)
        self.actionAdd_DVR.setObjectName("actionAdd_DVR")
        self.actionInfertime = QtWidgets.QAction( MainWindow )
        self.actionInfertime.setObjectName( "actionInfertime" )
        self.actionCentral_Library = QtWidgets.QAction(MainWindow)
        self.actionCentral_Library.setObjectName("actionCentral_Library")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        self.menuMenu.addAction(self.actionAdd_DVR)
        self.menuMenu.addAction(self.actionInfertime)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionLogout)
        self.menuDVR.addAction(self.actionCentral_Library)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuDVR.menuAction())
        self.menubar.hide()

        self.f = open( 'data/Channellink.json' )
        self.dict_dump = json.load( self.f )
        self.f.close()
        self.key_hold = list( self.dict_dump[0].keys() )

        for i in range( 1, len( self.key_hold ) ):
            self.dvrdropdown = self.menuDVR.addAction(self.key_hold[i])
            self.handletrigger(self.key_hold[i], self.dvrdropdown)



        ##  All Connections
        clickable( self.Screenlabel ).connect( self.FullScreenS )
        self.LoginButton.clicked.connect( lambda: self.onLogin() )
        self.actionLogout.triggered.connect( lambda: self.onLogout() )
        self.actionCentral_Library.triggered.connect(lambda : self.LiveStream("CentralLibrary"))
        self.actionAdd_DVR.triggered.connect(lambda : self.addDVRForm())
        self.actionInfertime.triggered.connect(lambda : self.Infertime())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AISS"))
        self.Screenlabel.setText(_translate("MainWindow", ""))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuDVR.setTitle(_translate("MainWindow", "DVR"))
        self.actionAdd_DVR.setText(_translate("MainWindow", "Add DVR"))
        self.actionCentral_Library.setText(_translate("MainWindow", "Central Library"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))
        self.actionInfertime.setText(_translate("MainWindow","Inference Time"))

        ##LOGIN PANEL
        self.LoginLabel.setText( _translate( "MainWindow", "LOGIN" ) )
        self.UsernameLabel.setText( _translate( "MainWindow", "Username" ) )
        self.PasswordLabel.setText( _translate( "MainWindow", "Password" ) )
        self.LoginButton.setText( _translate( "MainWindow", "Submit" ) )
        self.LoginLabel_2.setText( _translate("MainWindow", "AI Surveillance System" ))


    def handletrigger(self,key,action):
        action.triggered.connect(lambda: self.LiveStream(key) )


    def showtext(self):
        print("done")


    def addDVRMenu(self):

        self.f3 = open("data/Channellink.json")
        self.dict_dump = json.load(self.f3)
        self.f3.close()


        self.last_key = list(self.dict_dump[0].keys())[-1]
        self.newdvr = self.menuDVR.addAction(self.last_key)
        self.newdvr.triggered.connect(lambda : self.LiveStream(self.last_key))


    def addDVRForm(self):
        Dialog = QtWidgets.QDialog()
        ui = adddvr.Ui_Dialog()
        ui.setupUi(Dialog)
        mw = qtmodern.windows.ModernWindow(Dialog)
        mw.show()
        # Dialog.show()
        res = Dialog.exec_()
        if res == QtWidgets.QDialog.Accepted:
            ui.submitform()
            self.addDVRMenu()

    def Infertime(self):
        Dialog = QtWidgets.QDialog()
        ui = Inferform.Infer_Dialog()
        ui.setupUi( Dialog )
        mw = qtmodern.windows.ModernWindow( Dialog )
        mw.show()
        # Dialog.show()
        res = Dialog.exec_()
        if res == QtWidgets.QDialog.Accepted:
            ui.SubmitInfer()



    def onLogin(self):
        # if
        self.Loginframe.hide()
        self.Screenframe.show()
        self.menubar.show()

    def onLogout(self):
        self.Loginframe.show()
        self.Screenframe.hide()
        self.menubar.hide()


    def LiveStream(self,key):
        try:
            self.Screenlabel.setEnabled( True )
            print(key)
            f = open( "data/keystore.txt", "a" )
            f.write(key)
            f.write( "-" )
            f.close()

            self.path = 'data/Channellink.json'
            self.f = open( self.path )
            self.dump = json.load( self.f )
            self.f.close()
            self.streamlink = self.dump[0][key][0]
            self.thread = VideoThread( self.streamlink, self.isplaying )
            self.thread.change_pixmap_signal.connect( self.update_image )
            self.thread.start()

        except Exception as e:
            print( e )
            self.onError( "Try Again" )

    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt( cv_img )
        self.Screenlabel.setScaledContents( True )
        self.Screenlabel.setPixmap( qt_img )

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor( cv_img, cv2.COLOR_BGR2RGB )
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage( rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888 )
        return QPixmap.fromImage( convert_to_Qt_format )

    def onError(self, error):
        msg = QMessageBox()
        msg.setIcon( QMessageBox.Critical )
        msg.setText( "Error Occured" )
        msg.setInformativeText( error )
        msg.setWindowTitle( "Error" )
        msg.exec_()


    def FullScreenS(self):
        f1 = open( "data/coordinates.txt", "r+" )
        d = f1.read()
        f1.seek( 0 )
        f1.truncate()
        arr = d.split( "-" )

        f2 = open( "data/keystore.txt", "r+" )
        d2 = f2.read()


        self.path = 'data/Channellink.json'
        self.f = open( self.path )
        self.dump = json.load( self.f )
        self.f.close()


        arr2 = d2.split("-")
        self.key = arr2[-2]
        x = int( arr[0] )
        y = int( arr[1] )



        if (x > 0 and x < 245 and y > 0 and y < 150):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( self.dump[0][self.key][1] )
            return
        elif (x > 245 and x < 490 and y > 0 and y < 150):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( self.dump[0][self.key][2] )
            return
        elif (x > 490 and x < 735 and y > 0 and y < 150):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( self.dump[0][self.key][3] )
            return
        elif (x > 735 and x < 980 and y > 0 and y < 150):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( self.dump[0][self.key][4] )
            return
        elif (x > 0 and x < 245 and y > 150 and y < 300):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( self.dump[0][self.key][5] )
            return
        elif (x > 245 and x < 490 and y > 150 and y < 300):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( self.dump[0][self.key][6] )
            return
        elif (x > 490 and x < 735 and y > 150 and y < 300):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( self.dump[0][self.key][7] )
            return

        elif (x > 735 and x < 980 and y > 150 and y < 300):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream(self.dump[0][self.key][8])
            return

        elif (x > 0 and x < 245 and y > 300 and y < 450):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( self.dump[0][self.key][9] )
            return

        elif (x > 245 and x < 490 and y > 300 and y < 450):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( self.dump[0][self.key][10] )
            return

        elif (x > 490 and x < 735 and y > 300 and y < 450):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( self.dump[0][self.key][11] )
            return

        elif (x > 735 and x < 980 and y > 300 and y < 450):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( self.dump[0][self.key][12] )
            return

        elif (x > 0 and x < 245 and y > 450 and y < 600):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( self.dump[0][self.key][13] )
            return

        elif (x > 245 and x < 490 and y > 450 and y < 600):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( self.dump[0][self.key][14] )
            return

        elif (x > 490 and x < 735 and y > 450 and y < 600):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( self.dump[0][self.key][15] )
            return

        else:
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( self.dump[0][self.key][16] )
            return

### Clickable Label ###
def clickable(widget):
    class Filter( QObject ):
        clicked = pyqtSignal()

        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains( event.pos() ):
                        x = event.x()
                        y = event.y()
                        f = open( "data/coordinates.txt", "a" )
                        f.write( str( x ) )
                        f.write( "-" )
                        f.write( str( y ) )
                        f.close()

                        self.clicked.emit()

                        return True

            return False

    filter = Filter( widget )
    widget.installEventFilter( filter )

    return filter.clicked

### Create dynamic Signal
class DynamicConnect(QObject):
    trigger = pyqtSignal()

    def connect_and_emit_trigger(self):
        self.trigger.connect(self.handle_trigger)
        self.trigger.emit()

    def handle_trigger(self):
        print('connected')



### Video play using OPENCV
class VideoThread( QThread):
    change_pixmap_signal = pyqtSignal( np.ndarray )

    def __init__(self, filename, isplaying):
        super().__init__()
        self.filename = filename
        self._run_flag = True
        self.duration = 0
        self.isplaying = isplaying
        self.frameId = 0
        self.startFrame = 0
        self.starttiming = 0
        self.isLive = True
        self.out = None

        self.cap = cv2.VideoCapture( self.filename )
        self.fourcc = cv2.VideoWriter_fourcc( *'XVID' )
        self.cap.set(cv2.CAP_PROP_FPS, 10)
        self.fps = self.cap.get( cv2.CAP_PROP_FPS )
        self.frameCount = int( self.cap.get( cv2.CAP_PROP_FRAME_COUNT ) )
        self.endFrame = self.frameCount - 1
        self.secsDuration = self.frameCount / self.fps
        self.framePosUpdated = False
        print( 'fps = ' + str( self.fps ) )
        print( 'Number of frames = ' + str( self.frameCount ) )
        secs = self.secsDuration
        self.duration = time.strftime( '%H:%M:%S', time.gmtime( secs ) )
        print( "Duration (H:M:S) = ", self.duration )
        print( "Wait Key Value", int( 1000 / self.fps ) )



    def stop(self):
        self._run_flag = False
        self.wait()

    def run(self):
        try:
            while self._run_flag and self.isLive:
                ret, cv_img = self.cap.read()
                if ret:
                    self.change_pixmap_signal.emit( cv_img )
                # if self.isRecord:
                #     self.out.write( cv_img )
            self.cap.release()
            if self.out is not None:
                self.out.release()
        except Exception as e:
            self.onError(str(e))

### Single Cam view###
class FullScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.FScreen = QLabel("FullScreen")
        self.FScreen.setWindowTitle("Preview")
        self.FScreen.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.showMaximized()
        self.FScreen.setEnabled(True)
        layout.addWidget(self.FScreen)
        self.setLayout( layout )
        self.isplaying = True

    def PlayCamStream(self,streamlink):
        self.streamlink = streamlink
        self.thread = VideoThread( self.streamlink, self.isplaying )
        self.thread.change_pixmap_signal.connect(self.update_image2)
        self.thread.start()

    def update_image2(self,cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.FScreen.setScaledContents( True )
        self.FScreen.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor( cv_img, cv2.COLOR_BGR2RGB )
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage( rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888 )
        return QPixmap.fromImage( convert_to_Qt_format )





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # qtmodern.styles.dark( app )
    mw = qtmodern.windows.ModernWindow( MainWindow )
    mw.show()
    # MainWindow.show()
    sys.exit(app.exec_())

