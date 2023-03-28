import random

hiragana_sound_list = ["a","i","u","e","o",
                "ka","ki","ku","ke","ko",
                "sa","si","su","se","so",
                "ta","chi","tsu","te","to",
                "na","ni","nu","ne","no",
                "ha","hi","fu","he","ho",
                "ma","mi","mu","me","mo",
                "ya","yu","yo",
                "ra","ri","ru","re","ro",
                "wa","o","n"]


extra_sound = ["ga","gi",'gu','ge','go','za','ji','zu','ze','zo','da','ji','zu','de','do','ba','bi','bu','be','bo'
               ,'pa','pi','pu','pe','po']

yo_sound = ['kya','kyu','kyo','gya','gyu','gyo','sha','shu','sho','ja','ju','jo','cha','chu','cho','nya','nyu','nyo'
            ,'hya','hyu','hyo','bya','byu','byo','pya','pyu','pyo','mya','myu','myo','rya','ryu','ryo']

total = []
print("add hira?[y/n]")
k = input(">")
if k == "y" or k == "Y":
    total += hiragana_sound_list

print("add 탁음?")
m = input(">")
if m == "y" or m == "Y":
    total += extra_sound

print("add 요음?")
l = input(">")
if l == "y" or l == "Y":
    total += yo_sound


while True:
    idx = random.randint(0, len(total)-1)
    print(total[idx])
    ct = input("continue? [Y/N]")
    if ct == 'Y' or ct == 'y':
        continue
    else:
        print("exit")
        break
