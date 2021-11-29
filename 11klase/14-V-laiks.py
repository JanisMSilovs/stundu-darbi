from datetime import datetime

laiks = datetime.now()

stundas = 9
minutes = 18

# rīts no 4 līdz 12
# diena no 12 līdz 18
# vakars 18 līdz 00
if 0<=stundas <= 23 and 0 <= minutes <= 59:
    if stundas >=4 and stundas <12 :
        print("Labrīt!")
    elif stundas >=12 and stundas <18 :
        print("Labdien!")
    else:
        print("Labvakar!")
else:
    print("Nekorekts laiks!")