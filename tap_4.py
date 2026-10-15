


def en_boyuk_eded():

    ededler =[]
    for i in range(3):
        eded_al =  int(input(f'{i+1}, ededleri daxil edin: '))
        ededler.append(eded_al)

    print(f'sizin daxil etdiyiniz ededler {ededler}')
    print(f"sizin daxil etdiyiniz ededler arasinda en yuksek eded {max(ededler)}")
    print(f"sizin daxil etdiyiniz ededler arasinda en kicik eded {min(ededler)}")

en_boyuk_eded()