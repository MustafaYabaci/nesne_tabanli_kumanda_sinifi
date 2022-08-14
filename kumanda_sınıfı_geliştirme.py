import random
import time
class Kumanda():
    def __init__(self,tv_durum="kapalı",tv_ses=0,kanal_listesi = ["Trt"],kanal="trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_aç(self):
        if(self.tv_durum=="açık"):
            print("tv zaten açık")
        else:
            print("tv açılıyor")
            self.tv_durum="açık"
    def tv_kapat(self):
        if(self.tv_durum=="kapalı"):
            print("tv zaten kapalı")
        else:
            print("tv kapanıyor")
            self.tv_durum="kapalı"
    def ses_ayarları(self):
        while True:
            cevap=input("sesi azaltmak için '<' \n sesi artırmak için '>'\n çıkış :çıkış")
            if(cevap=="<"):
                if(self.tv_ses!=0):
                    self.tv_ses-=1
                    print("ses",self.tv_ses)
            elif(cevap==">"):
                if(self.tv_ses!=31):
                    self.tv_ses+=1
                    print("ses :",self.tv_ses)
            else:
                print("ses güncellendi",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
                print("kanal ekleniyor")
                time.sleep(1)
                self.kanal_listesi.append(kanal_ismi)
                print("kanal eklendi....")
    def rastgele_kanal(self):
                rastgele=random.randint(0,len(self.kanal_listesi)-1)
                self.kanal=self.kanal[rastgele]
                print("şu anki kanal",self.kanal)
    def __len__(self):
                return len(self.kanal_listesi)

    def __str_(self):
                return("tv durum {} \n tv_ses : {}\n kanal_listesi : {} \n şu anki kanal :{} \n").format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
kumanda=Kumanda()

print("""

            Televizyon Uygulaması


            1. Tv Aç

            2. Tv Kapat

            3. Ses Ayarları

            4. Kanal Ekle

            5. Kanal Sayısını Öğrenme

            6. Rastgele Kanala Geçme

            7. Televizyon Bilgileri

            Çıkmak için 'q' ya basın.
""")
while True:
                işlem=input("lütfen işlemi seçiniz")
                if(işlem=="q"):
                    print("program sonlandırılıyor")
                    break
                elif(işlem=="1"):
                    kumanda.tv_aç()
                elif(işlem=="2"):
                    kumanda.tv_kapat()

                elif(işlem=="3"):
                    kumanda.ses_ayarları()
                elif (işlem == "4"):
                    kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")

                    kanal_listesi = kanal_isimleri.split(",")

                    for eklenecekler in kanal_listesi:
                        kumanda.kanal_ekle(eklenecekler)
                elif(işlem=="5"):
                    print("kanal sayısı : ",len(kumanda))
                elif(işlem=="6"):
                    kumanda.rastgele_kanal()
                elif(işlem=="7"):
                    print(kumanda)
                else:
                    print("gecersiz işlem")



