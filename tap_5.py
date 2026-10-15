#Tapşırıq 5. İstifadəçidən bir ədəd al və onun 1-dən 10-a qədər vurma cədvəlini göstər.



def vurma_cedveli():
    while True:
        try:
            eded_al= int(input('Bir tam eded girin zehmet olmasa: '))
            break

        except (ValueError):
            print("Yanlis secim! Tam ededler daxil edin")


    for i in range(1,11):
        print(f'{eded_al} * {i} = {eded_al*i}')


vurma_cedveli()