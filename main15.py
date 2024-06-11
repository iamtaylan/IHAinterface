import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtQuickWidgets import *
from PyQt5.QtCore import *
#import folium # pip install folium
import math
import json

from SozDroneTaslak import *
from threadGUI import ThreadGUI
#from qt_material import *


with open('identity.json') as f: #  sürekli veri basıyor. bu veriyi açıp içindeki veriyi enleme kaydet
    KullaniciAdi1 = json.load(f)
with open('password.json') as f: #  sürekli veri basıyor. bu veriyi açıp içindeki veriyi enleme kaydet
    KullaniciParola1 = json.load(f)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #Pencere Boyutlandırma
        QSizeGrip(self.ui.size_grip)

        #Arayüzdeki Map Bölümü
        self.ui.mapQuickWidget.setSource(QUrl("DisplayOverviewMap.qml"))
        self.ui.mapQuickWidget.show()

        self.ui.manuelQmap.setSource(QUrl("DisplayOverviewMap.qml"))
        self.ui.manuelQmap.show()

        #İlk açılışta karşımıza çıkan ekran
        self.ui.ortaSagStackedWidget.setCurrentWidget(self.ui.kullaniciGirisPage)

        #Buton ayarlamaları

        self.ui.ayarlarButon.clicked.connect(lambda: self.ui.ortaSagStackedWidget.setCurrentWidget(self.ui.ayarlarPage))
        self.ui.baslaButon.clicked.connect(lambda: self.ui.ortaSagStackedWidget.setCurrentWidget(self.ui.arayuzPage))
        #self.ui.baslaButon.clicked.connect(self.komutaEnableDisable)
        self.ui.durdurButon.clicked.connect(lambda: self.ui.ortaSagStackedWidget.setCurrentWidget(self.ui.inisPage))

        self.ui.rtlButon.clicked.connect(lambda: self.ui.ortaSagStackedWidget.setCurrentWidget(self.ui.otonomInisPage))
        self.ui.landButon.clicked.connect(lambda: self.ui.ortaSagStackedWidget.setCurrentWidget(self.ui.otonomInisPage))
        self.ui.manuelButon.clicked.connect(lambda: self.ui.ortaSagStackedWidget.setCurrentWidget(self.ui.manuelInisPage))
        self.ui.pushButton.clicked.connect(self.KullaniciGiris)
        #self.ui.manuelRtlButon.clicked.connect(lambda: self.ui.ortaSagStackedWidget.setCurrentWidget(self.ui.otonomInisPage))
        #self.ui.manuelLandButon.clicked.connect(lambda: self.ui.ortaSagStackedWidget.setCurrentWidget(self.ui.otonomInisPage))
        #self.ui.kapatButon.clicked.connect(self.close) 
        #self.ui.kucultButon.clicked.connect(self.minimize)
        #self.ui.buyutButon.clicked.connect(self.maximize)
        #self.ui.comboBox.currentIndexChanged.connect(self.LightThemeChanged) 

        #LineEdit özellikleri
        self.ui.ileriLineEdit.setValidator(QIntValidator(0,99,self))    
        self.ui.yonLineEdit.setValidator(QIntValidator(0,99,self))    
        self.ui.guvenliYukLineEdit.setValidator(QIntValidator(0,1,self))    
        self.ui.lineEdit.setEnabled(False)
        self.ui.bataryaLineEdit.setEnabled(False)
        self.ui.muhimmatLineEdit.setEnabled(False)
        self.ui.ModLineEdit.setEnabled(False)



    #Birbirine bağlılık gösteren butonları aktif inaktif eden fonksiyon
    def komutaEnableDisable(self):
        self.ui.GMDButon.setDisabled(True)
        self.ui.ayarlarButon.setDisabled(True)
        self.ui.durdurButon.setDisabled(False)
        self.ui.pushButton.setDisabled(True)



    #Birbirine bağlılık gösteren butonları aktif inaktif eden fonksiyon 2.
    #def durdurEnableDisable(self):
        #self.ui.durdurButon.setDisabled(True)



    #Kadranları çalıştıran geçici fonksiyon
    def update(self,val):
        self.ui.dikilmeGraphics.setRoll(10*math.cos(val))
        self.ui.dikilmeGraphics.setPitch(10*math.cos(val))
        #self.ui.bataryaGraphics.setSpeed(val/10)
        self.ui.yonelmeGraphics.setHeading(val) 
        self.ui.hizGraphics.setClimbRate(val)
        self.ui.irtifaGraphics.setAltitude(val)
        self.ui.yatisGraphics.setTurnRate(10*math.cos(val))
        self.ui.yatisGraphics.setSlipSkid(10*math.cos(val))
        self.ui.manuelHizGraphics.setClimbRate(val)
        self.ui.manuelrtifaGraphics.setAltitude(val)

        self.ui.dikilmeGraphics.viewUpdate.emit()
        self.ui.irtifaGraphics.viewUpdate.emit()
        #self.ui.bataryaGraphics.viewUpdate.emit()
        self.ui.yonelmeGraphics.viewUpdate.emit()
        self.ui.hizGraphics.viewUpdate.emit()
        self.ui.yatisGraphics.viewUpdate.emit()
        self.ui.manuelHizGraphics.viewUpdate.emit()
        self.ui.manuelrtifaGraphics.viewUpdate.emit()


        self.ui.otonomDikilmeGraphics.setRoll(10*math.cos(val))
        self.ui.otonomDikilmeGraphics.setPitch(10*math.cos(val))
        #self.ui.bataryaGraphics.setSpeed(val/10)
        self.ui.otonomYatisGraphics_2.setHeading(val) 
        self.ui.otonomHizGraphics.setClimbRate(val)
        self.ui.otonomIrtifaGraphics.setAltitude(val)
        self.ui.otonomYatisGraphics.setTurnRate(10*math.cos(val))
        self.ui.otonomYatisGraphics.setSlipSkid(10*math.cos(val))

        self.ui.otonomDikilmeGraphics.viewUpdate.emit()
        self.ui.otonomIrtifaGraphics.viewUpdate.emit()
        #self.ui.bataryaGraphics.viewUpdate.emit()
        self.ui.otonomYatisGraphics_2.viewUpdate.emit()
        self.ui.otonomHizGraphics.viewUpdate.emit()
        self.ui.otonomYatisGraphics.viewUpdate.emit()


        #self.ui.arayuzButon.setDisabled(True)
        self.show()
    

    #Kapatma fonksiyonu
    def close(self):
        quit()

    #Küçültme fonksiyonu
    def minimize(self):
        self.showMinimized()

    #Büyültme fonksiyonu
    def maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


    #Pencereyi hareket ettirme fonksiyonları
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()


    #Kullanıcı giriş fonksiyonu
    def KullaniciGiris(self):
        
        if self.ui.KullaniciALineEdit.text() == KullaniciAdi1 and self.ui.KullaniciPLineEdit.text() != KullaniciParola1:
            pass
        elif self.ui.KullaniciALabel.text() != KullaniciAdi1 and self.ui.KullaniciPLineEdit.text() != KullaniciParola1:
            pass
        elif self.ui.KullaniciALineEdit.text() != KullaniciAdi1 and self.ui.KullaniciPLineEdit.text() == KullaniciParola1:
            pass
        elif self.ui.KullaniciALineEdit.text() == KullaniciAdi1 and self.ui.KullaniciPLineEdit.text() == KullaniciParola1:
            self.ui.pushButton.clicked.connect(lambda: self.ui.ortaSagStackedWidget.setCurrentWidget(self.ui.komutaPage))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    t2 = ThreadGUI(window)
    t2.daemon = True
    t2.start()

    sys.exit(app.exec_())

