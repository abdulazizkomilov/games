import random

def sontop_user(x=10):
    tasodify_son = random.randint(1, x)
    print('Keling o`ylagan sonni topish o`ynaymiz!')
    print(f"1 dan {x} gacha son o`yladim. Topa olasizmi ?")
    i = 0
    while True:
        i+=1
        taxmin = int(input('>> '))
        if taxmin < tasodify_son:
            print(f"Xato, men o`ylagan son {taxmin} kattaroq. Yana harakat qilib kuring.")
        elif taxmin > tasodify_son:
            print(f"Xato, men o`ylagan son {taxmin} kichikroq. Yana harakat qilib kuring.")
        else:
            break
    print(f"TOPDINGIZ! {tasodify_son} sonini o`ylagan edim. {i} ta taxmin bilan topdingiz. Tabriklayman!!")
    return i


def sontop(x=10):
    print(f"1 dan 10 gacha son o`ylang, men topishga harakat qilaman.")
    input(f"Son o`ylagan bo`lsangiz istalgan tugmani bosing. >> ")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            tamin_son = random.randint(quyi, yuqori)
        else:
            quyi = yuqori
        hisob = str(input(f"Siz {tamin_son} sonini o`yladingiz to`g`rimi: to`g`ri (t), o`ylagan son kattaroq (+) yoki kichikroq (-)?? "))
        if hisob == '-':
            yuqori = tamin_son - 1
        elif hisob == '+':
            quyi = tamin_son + 1
        else:
            break
    print(" ")
    print(f"Men {taxminlar} ta taxmin bilan topdim.")
    return taxminlar

def hisob(x=10):
    yana_o = True
    while yana_o:
        tax_user = sontop_user(x)
        tax_pc = sontop(x)
        print(" ")
        if tax_user > tax_pc:
            print(f"Men {tax_user} ta taxmin bilan yutdim! Siz {tax_pc} ta taxmin bilan yutqazdingiz.")
        elif tax_user < tax_pc:
            print(f"Siz {tax_user} ta taxmin bilan yutdingiz! Men {tax_pc} ta taxmin bilan yutqazdim.")
        elif tax_user == tax_pc:
            print('Durrang!!')
            print((f"{tax_user} = {tax_pc}"))
            print(" ")
        yana_o = int(input("Yana o`ynaysizmi, Ha(1) yoki Yo`q(0). >> "))
print(hisob(10))