def factoriel(x):

    """Bu fonksiyon girilen sayının faktöriyel degerini döndürür"""

    sonuc = 1
    for i in range(1, x + 1):
        sonuc *= i

    return sonuc    


def my_pow(x,y):

    return float(x ** y)

my_pi = 3,14


def mean(* sayı):

    return sum([i for i in sayı]) / len(sayı)


   

