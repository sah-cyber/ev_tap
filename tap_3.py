"""
🔹 Set — 4 tapşırıq
5 ədəddən ibarət set yarat və elementlərini çap et.

Setə yeni element əlavə et.

İki set yarat və onların ortaq elementlərini tap.

İki set yarat və birinci setdə olub, ikinci setdə olmayan elementləri tap.

İstəsən, bunları asan → orta → çətin sıralamasında bir az daha çətin formada da hazırlaya bilərəm.

"""


def eded_yarat():

    ededler = {1,2,3,4,5}

    print(*ededler)

    ededler.add(6)
    print(*ededler)

eded_yarat()