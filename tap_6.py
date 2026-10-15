import random


class ReqemTap:
    def __init__(self, xal=6):
        self.xal = xal
        self.reqem = random.randint(1, 20)
        self.ad = ""

    def start(self):
        while True:
            self.ad = input("Zəhmət olmasa, adınızı daxil edin: ").strip()

            if self.ad.isalpha():
                break

            print("Adı düzgün daxil edin!")

        print(f"Xoş gəlmisiniz, {self.ad}!")
        print("Kompüter 1-20 arasında rəqəm tutub.")
        print(f"Sizin {self.xal} cəhdiniz var.")

        while self.xal > 0:
            daxil = input("Rəqəminiz: ")

            if not daxil.isdigit():
                print("Zəhmət olmasa, tam müsbət rəqəm daxil edin.")
                continue

            texmin = int(daxil)

            if texmin < 1 or texmin > 20:
                print("1 ilə 20 arasında rəqəm daxil edin!")
                continue

            self.xal -= 1

            if texmin == self.reqem:
                print("Təbriklər! Siz qalib gəldiniz!")
                return

            elif texmin < self.reqem:
                print("Tutulan rəqəm daha böyükdür.")

            else:
                print("Tutulan rəqəm daha kiçikdir.")

            print(f"Qalan cəhd sayı: {self.xal}")

        print(f"Cəhdlər bitdi! Tutulan rəqəm {self.reqem} idi.")


oyun = ReqemTap()
oyun.start()