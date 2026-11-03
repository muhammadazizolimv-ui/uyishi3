
class BankHisobi:
    def __init__(self, balans=0):
        self.__balans = balans

    def balansni_korish(self):
        return self.__balans

    def pul_qosh(self, miqdor):
        if miqdor > 0:
            self.__balans += miqdor
        else:
            print("Qo‘shiladigan miqdor musbat bo‘lishi kerak!")

    def pul_yech(self, miqdor):
        if miqdor <= 0:
            print("Yechiladigan miqdor musbat bo‘lishi kerak!")
        elif miqdor <= self.__balans:
            self.__balans -= miqdor
        else:
            print("Balans yetarli emas!")


hisob = BankHisobi(100000)
hisob.pul_qosh(25000)
hisob.pul_yech(30000)
print("Balans:", hisob.balansni_korish())  # 95000

hisob.pul_yech(500000)   # balans yetarli emas
hisob.pul_qosh(-100)     # manfiy miqdor
print("Balans:", hisob.balansni_korish())  # o‘zgarmaydi: 95000


