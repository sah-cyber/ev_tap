"""
📋 List — 4 tapşırıq
5 ədəddən ibarət list yarat və bütün elementləri çap et.

Listə yeni bir ədəd əlavə et və sonra listi çap et.

Listdəki ən böyük və ən kiçik ədədi tap.

Listdə neçə cüt ədəd olduğunu hesabla.
"""


def eded_yarat():
     ededler = [1,2,3,4,5]

     print(*ededler)

     ededler.append(6)
     print(*ededler)

     print("siyahida en kicin eded {}, en boyuk eded {}".format(min(ededler),max(ededler)))

     cut = []

     for i in ededler:
         if i % 2 == 0:
             cut.append(i)

     print(f'cut ededler {cut}')




eded_yarat()