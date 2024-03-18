def seperator(* numbers):

    """Girilen sayıları tek ve cift olarak ayıklar."""

    odds = [] 
    evens = []
    for i in numbers:

        if i % 2:
            odds.append(i)
        else:
            evens.append(i)
    # return odds, evens  
    print(f"Tek sayilar listesi: {odds}\n Çift Sayilar listesi: {evens}")
    # return f"Tek sayilar listesi: {odds} Çift Sayilar listesi: {evens}"







