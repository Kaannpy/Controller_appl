import random
import time
from idlelib.pyparse import trans


class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["Fox Tv"],kanal="Fox Tv"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal


    def tv_ac(self):
        if(self.tv_durum=="Açık"):
            print("Televizyon zaten Açık....")
        else:
            print("Televizyon Açılıyor.....")
            self.tv_durum="Açık"

    def tv_kapat(self):
        if (self.tv_durum == "Kapalı"):
            print("Televizyon zaten Kapalı....")
        else:
            print("Televizyon Kapanıyor.....")
            self.tv_durum = "Kapalı"


    def ses_ayarları(self):
        while True:
            cevap=input("Sesi azalt: '<'\n Sesi artırır :'>'\n Çıkıs: exit")

            if(cevap=="<"):

                if(self.tv_ses!=0):

                    self.tv_ses-=1
                    print("Ses",self.tv_ses)
            elif (cevap==">"):

                if(self.tv_ses!=31):

                    self.tv_ses+=1
                    print("Ses:",self.tv_ses)
            else:
                    print("Ses güncellendi:",self.tv_ses)
                    break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi.....")

    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Şu anki Kanal:",self.kanal)

    def __len__(self):
        return  len(self.kanal_listesi)
    def __str__(self):
        return "TV Durumu:{}\nTV Ses:{}\nKanal Listesi:{}\n,Şu anki kanal:{}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda1=Kumanda()


print("""
   Televizyon Uygulaması
   
   1.TV AÇ
   2.TV KAPAT
   3.SES AYARLARI
   4.KANAL EKLE
   5.KANAL SAYISINI ÖĞRENME
   6.RASTGELE KANALA GEÇME
   7.TELEVİZYON BİLGİLERİ
   ÇIKMAK İÇİN "q" BASINIZ


""")
while True:

      işlem=input("İşlemi seçiniz....")
      if(işlem=="q"):
          print("Program sonlandırılıyor....")
          break
      elif(işlem=="1"):
          kumanda1.tv_ac()

      elif(işlem=="2"):
          kumanda1.tv_kapat()

      elif(işlem=="3"):
          kumanda1.ses_ayarları()

      elif(işlem=="4"):
          kanal_isimleri=input("Kanal isimlerini ',' ile ayırarak giriniz:")

          kanal_listesi=kanal_isimleri.split(",")

          for eklencekler in kanal_listesi:
              kumanda1.kanal_ekle(eklencekler)
      elif(işlem=="5"):
          print("Kanal sayisi:",len(kumanda1))

      elif(işlem=="6") :
          kumanda1.rastgele_kanal()

      elif(işlem=="7"):
          print(kumanda1)
      else:
          print("Gecersiz işlem....")