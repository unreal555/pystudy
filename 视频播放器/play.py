from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
import sys

class VideoPlayer:

    def __init__(self):
        self.video = QVideoWidget()
        self.video.resize(300, 300)
        self.video.move(0, 0)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video)

        
        self.path=QUrl.fromLocalFile('c://01.mp4')
        print(self.path.path())
        self.movie=QMediaContent(self.path)
        print(self.movie.playlist())
        self.player.setMedia(self.movie)
        print(self.player.duration())
        self.player.durationChanged.connect(self.getDuration)
        
        
        # self.player.setMedia(QMediaContent(QUrl.fromLocalFile("c://01.mp4")))
    def ms2HMS(self,ms):
        playtime =ms/1000
        h = int(playtime // 3600)
        m = int((playtime - h * 3600) // 60)
        s = int(playtime - h * 3600 - m * 60)
        return ms,h,m,s
    
    def getDuration(self):
        '''
        QT中，使用QMediaplayer类可以很方便地实现视频的播放，而在QMediaplayer类中有个duration函数可以直接获取所打开视频的总时间长度。但使用后你会发现duration（）返回的居然是个0。
        在初始回放开始时可能不可用，请连接durationChanged()信号以接收状态通知。
        即我们只需要写个槽函数，在槽函数里面调用duration（）就可以接收到正确的时间
        '''
        ms=self.player.duration()
        ms,h,m,s=self.ms2HMS(ms=ms)
        print(ms,h,m,s)
        return ms,h,m,s


    
    # def callback(self,pos=0):
    #     # self.player.setPosition(10000) # to start at the beginning of the video every time
    #     # self.video.show()
    #     # self.player.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    v = VideoPlayer()
    b = QPushButton('start')
    b.clicked.connect(v.callback)
    b.show()

    sys.exit(app.exec_())
