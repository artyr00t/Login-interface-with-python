import sys
import os
from PyQt5 import QtWidgets
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.ad = QtWidgets.QLabel("Kullanıcı adı :")
        self.sifre = QtWidgets.QLabel("Şifre :")
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.cikis = QtWidgets.QPushButton("Cikis Yap")
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.ad)
        v_box.addWidget(self.kullanici_adi)
        v_box.addStretch()
        v_box.addWidget(self.sifre)
        v_box.addWidget(self.parola)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        v_box.addWidget(self.cikis)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Giriş proje")

        self.giris.clicked.connect(self.click)
        self.cikis.clicked.connect(self.clicked)
        self.show()
    def click(self):
        yokla = self.kullanici_adi.text()
        yoklama = self.parola.text()
        if yokla == "":
            print("Kullanıcı Adı Boş")
        elif yoklama == "":
            print("Şifre Boş")
        elif yokla == "" and yoklama == "":
            print("Kullanıcı Adı Ve Şifre Boş")
        else:
            os.system("clear")
            print("Giriş Başarılı!\n****************************************")
            print("Kullanıcı adı : ",yokla)
            print("Şifre : ",yoklama)
            print("****************************************")
            self.kullanici_adi.clear()
            self.parola.clear()
    def clicked(self):
        os.system("clear")
        print("Bye...")
        sys.exit()
        

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
