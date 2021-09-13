Kaas = input("is de kaas geel? :")
if Kaas == "ja":
    vraag1 = input("zitten er gaten in? :")
    if vraag1 == "ja":
        vraag2 = input("is de kaas belachelijk duur? :")
        if vraag2 == "ja":
            print("Emmenthaler")
        elif vraag2 == "nee":
            print("leerdammer")
    elif vraag1 == "nee":
        vraag3 = input("is de kaas hard als steen? :")
        if vraag3 == "ja":
            print("parmigiano reggiano")
        elif vraag3 == "nee":
            print("goudse kaas")
elif Kaas == "nee":
    vraag4 = input("heeft de kaas blauwe schimmel? :")
    if vraag4 == "ja":
        vraag5 = input("heeft de kaas een korst? :")
        if vraag5 == "ja":
            print("bleu de rochbaron")
        elif vraag5 == "nee":
            print("foume d'ambert")
    elif vraag4 == "nee":
        vraag6 = input("heeft de kaas een korst")
        if vraag6 == "ja":
            print("camembert")
        elif vraag6 == "nee":
            print("mozzarella")
                
