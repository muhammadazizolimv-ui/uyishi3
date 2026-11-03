
class Mahsulot:
    def __init__(self, nom, miqdor=0):
        self.nom = nom
        self.__miqdor = miqdor

    def miqdorni_korish(self):
        return self.__miqdor

    def qabul_qil(self, son):
        if son > 0:
            self.__miqdor += son
        else:
            print("Qabul qilinadigan son musbat bo‘lishi kerak!")

    def sotish(self, son):
        if son <= 0:
            print("Sotiladigan son musbat bo‘lishi kerak!")
        elif son <= self.__miqdor:
            self.__miqdor -= son
        else:
            print(f"Omborda yetarli {self.nom} yo‘q! Mavjud: {self.__miqdor} dona.")


mahsulot = Mahsulot("Daftar", 20)
mahsulot.sotish(6)
mahsulot.qabul_qil(4)
print(f"Miqdor: {mahsulot.miqdorni_korish()} dona")  # 18 dona

mahsulot.sotish(100)
print(f"Miqdor: {mahsulot.miqdorni_korish()} dona")  # o‘zgarmaydi: 18 dona
