import sys
from PyQt5.QtCore import Qt, QEvent, QObject, pyqtSignal
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QGridLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread, QFileInfo
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMessageBox, QVBoxLayout
import numpy as np
import cv2
import os
import time

import threading


class MainScreen( QWidget ):

    def __init__(self):
        super().__init__()

        self.isplaying = True
        self.initUI()
        self.LiveStream()

    def initUI(self):
        grid = QGridLayout()
        x = 0
        y = 0

        self.text = f'x: {x},  y: {y}'
        self.label = QLabel( self.text, self )
        clickable( self.label ).connect( self.FullScreenS )
        grid.addWidget( self.label )

        self.setMouseTracking( True )
        self.label.installEventFilter( self )
        # print(self.label.size())

        self.setLayout( grid )
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        print( x, y )

    def showText(self):

        print( "Label 1 clicked" )

    def LiveStream(self):
        try:
            self.label.setEnabled( True )
            self.streamlink = "CameraFootage/channel0.mp4"
            self.thread = VideoThread( self.streamlink, self.isplaying )
            self.thread.change_pixmap_signal.connect( self.update_image )
            self.thread.start()

        except Exception as e:
            print( e )
            self.onError( "Try Again" )

    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt( cv_img )
        self.label.setScaledContents( True )
        self.label.setPixmap( qt_img )

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

    def LiveStream(self):
        try:
            self.label.setEnabled( True )
            self.streamlink = 'CameraFootage/channel0.mp4'
            self.thread = VideoThread( self.streamlink, self.isplaying )
            self.thread.change_pixmap_signal.connect( self.update_image )
            self.thread.start()

        except Exception as e:
            print( e )
            self.onError( "Try Again" )

    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt( cv_img )
        self.label.setScaledContents( True )
        self.label.setPixmap( qt_img )

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
        f1 = open( "data.txt", "r+" )
        d = f1.read()
        f1.seek( 0 )
        f1.truncate()
        arr = d.split( "-" )
        x = int( arr[0] )
        y = int( arr[1] )

        if (x > 0 and x < 245 and y > 0 and y < 150):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel1.mp4" )
            return
        elif (x > 245 and x < 490 and y > 0 and y < 150):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel2.mp4" )
            return
        elif (x > 490 and x < 735 and y > 0 and y < 150):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel3.mp4" )
            return
        elif (x > 735 and x < 980 and y > 0 and y < 150):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel4.mp4" )
            return
        elif (x > 0 and x < 245 and y > 150 and y < 300):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel5.mp4" )
            return
        elif (x > 245 and x < 490 and y > 150 and y < 300):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel6.mp4" )
            return
        elif (x > 490 and x < 735 and y > 150 and y < 300):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel7.mp4" )
            return

        elif (x > 735 and x < 980 and y > 150 and y < 300):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel8.mp4" )
            return

        elif (x > 0 and x < 245 and y > 300 and y < 450):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel9.mp4" )
            return

        elif (x > 490 and x < 735 and y > 300 and y < 450):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel10.mp4" )
            return

        elif (x > 735 and x < 980 and y > 300 and y < 450):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel11.mp4" )
            return

        elif (x > 245 and x < 490 and y > 300 and y < 450):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel12.mp4" )
            return

        elif (x > 0 and x < 245 and y > 450 and y < 600):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel13.mp4" )
            return

        elif (x > 245 and x < 490 and y > 450 and y < 600):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel14.mp4" )
            return

        elif (x > 490 and x < 735 and y > 450 and y < 600):
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel15.mp4.mp4" )
            return

        else:
            self.w = FullScreen()
            self.w.show()
            self.w.PlayCamStream( "CameraFootage/channel16.mp4" )
            return

    ## aspect ratio = width/height (5,5) and(20,20)
    # def streampath(self, x, y):


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
                        f = open( "data.txt", "a" )
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


### Video play using OPENCV


class VideoThread( QThread ):
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
        self.cap.set( cv2.CAP_PROP_FPS, 10 )
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
            self.onError( str( e ) )


# def checkIfInside(x,y):
#     if (x > 0 and x < 245 and y > 0 and y < 150):   ##1st line   (0,0)
#         return
#     elif (x > 245 and x < 490 and y > 0 and y < 150):
#         return
#     elif (x > 490 and x < 735 and y > 0 and y < 150):
#         return
#     elif (x > 735 and x < 980 and y > 0 and y < 150):
#         return
#     elif (x > 0 and x < 245 and y > 150 and y < 300):        ###2nd line
#         return
#     elif (x > 245 and x < 490 and y > 150 and y < 300):
#         return
#     elif (x > 490 and x < 735 and y > 150 and y < 300):
#         return
#     elif (x > 735 and x < 980 and y > 150 and y < 300):
#         return
#     elif (x > 0 and x < 245 and y > 300 and y < 450):        ###3rd line
#         return
#     elif (x > 490 and x < 735 and y > 300 and y < 450):
#         return
#     elif (x > 735 and x < 980 and y > 300 and y < 450):
#         #FullScreenS("http://166.165.35.32/mjpg/video.mjpg#.X4WV4gWF4pM.link")

#     elif (x > 245 and x < 490 and y > 300 and y < 450):
#         #FullScreenS( "http://166.165.35.32/mjpg/video.mjpg#.X4WV4gWF4pM.link" )

#     elif (x > 0 and x < 245 and y > 450 and y < 600):         ###4th line (980,575)
#        # FullScreenS("http://166.165.35.32/mjpg/video.mjpg#.X4WV4gWF4pM.link")
#     elif (x > 245 and x < 490 and y > 450 and y < 600):
#        # FullScreenS("http://166.165.35.32/mjpg/video.mjpg#.X4WV4gWF4pM.link")
#     elif (x > 490 and x < 735 and y > 450 and y < 600):
#       #  FullScreenS("http://166.165.35.32/mjpg/video.mjpg#.X4WV4gWF4pM.link")
#     else:
#         FullScreenS("http://166.165.35.32/mjpg/video.mjpg#.X4WV4gWF4pM.link")

### Single Cam view###
class FullScreen( QWidget ):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.FScreen = QLabel( "FullScreen" )
        self.FScreen.setWindowTitle( "Preview" )
        self.FScreen.setStyleSheet( "background-color: rgb(0, 0, 0);" )
        self.showMaximized()
        self.FScreen.setEnabled( True )
        layout.addWidget( self.FScreen )
        self.setLayout( layout )
        self.isplaying = True

    def PlayCamStream(self, streamlink):
        self.streamlink = streamlink
        self.thread = VideoThread( self.streamlink, self.isplaying )
        self.thread.change_pixmap_signal.connect( self.update_image2 )
        self.thread.start()

    def update_image2(self, cv_img):
        qt_img = self.convert_cv_qt( cv_img )
        self.FScreen.setScaledContents( True )
        self.FScreen.setPixmap( qt_img )

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor( cv_img, cv2.COLOR_BGR2RGB )
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage( rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888 )
        return QPixmap.fromImage( convert_to_Qt_format )

# def main():
#     app = QApplication(sys.argv)
#     ex = ()
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()
