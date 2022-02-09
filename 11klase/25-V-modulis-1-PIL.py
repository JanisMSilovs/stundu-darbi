from PIL import Image

# def bilde():
#     datne = "E:\\viss kopa\\darbi\\stundu-darbi\\11klase\\bilde.png"
#     with Image.open(datne) as im:
#         print(datne, im.format, f"{im.size}x{im.mode}")
#         im.show()
#         izmers = (100, 100)
#         im.thumbnail(izmers)
#         im.save("25-bilde-maza.jpg", im.format)
#         im.show()

# #bilde()

def bilde1():
     datne = "E:\\viss kopa\\darbi\\stundu-darbi\\11klase\\ogre.jpeg"
     with Image.open(datne) as im:
         print(datne, im.format, f"{im.size}x{im.mode}")
         im = im.rotate(90)
         izmers = (250, 100)
         im.thumbnail()
         im.show()
         im.save('E:\\viss kopa\\darbi\ogre1.jpeg')
#bilde1()
#Nezinu vai izdarīju kā vajadzēja, bet pagriež uz 90 grādiem, parāda un noseivo. Katru reizi, kad palaiž programmu, paintā cits nosaukums.

def bilde2():
    datne = "E:\\viss kopa\\darbi\\stundu-darbi\\11klase\\ogre.jpeg"
    with Image.open(datne) as im:
        print(im.size)
        jaunais = (128, 128)
        im = im.resize(jaunais)
        im.show()
        print(im.size)
        im.save('E:\\viss kopa\\darbi\ogre2.jpeg')

bilde2()

#Šeit arī nezinu cik pareizi, bet it kā pārvērš par tumbnail un saglabā citur. Sākumā parāda pirmo izmēru, tad otro, kuru resize.
