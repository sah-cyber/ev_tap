"""
📘 Dict — 4 tapşırıq
{"ad": "Ali", "yas": 18} dictionary-si yarat və ad-ı çap et.

Dictionary-yə yeni "seher": "Baki" elementi əlavə et.

Verilmiş dictionary-də neçə element olduğunu tap.

Tələbələrin ad və qiymətlərindən dictionary yarat. Ən yüksək qiyməti alan tələbənin adını tap.
"""


def ad_yarat():
    siyahi = {"ad":"Ali","yas":18}

    print(siyahi['ad'])
    siyahi['seher']='Baki'

    print(siyahi)

    print(len(siyahi))

    telebeler = {
        "Ali": 85,
        "Aysel": 95,
        "Murad": 78,
        "Leyla": 92
    }


    en_yuksek = max(telebeler, key=telebeler.get)
    print(en_yuksek,telebeler[en_yuksek])


ad_yarat()


