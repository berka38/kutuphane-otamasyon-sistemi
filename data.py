#############################################
#                                           #
#       kütüphane otomasyon sistemi         #
#                                           #
#           yapımcı bilgileri               #
#           github - gladyotr               #
#           instagram - @gladbey            #
#           gmail - gladyotr123@gmail.com   #
#                                           #
#               berat karaca <3             #
#############################################

data = {'mehmet': ('mehmet', 'ekim'), 'berat': ('berat', 'ekim'), 'yusuf': ('yusuf', 'ekim')}

def ekle(isim,kitap,tarih):
    data[isim]= kitap,tarih

def sil(isim):
    del data[isim]
    