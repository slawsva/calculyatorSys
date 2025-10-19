def Slozhenie(Int1, Int2, SistemaSchis):
    Ostatok = 0
    Result=str()
    while Int1!=0 or Int2!=0:
        if (Int1%10+Int2%10+Ostatok)<SistemaSchis:
            Result+=str(Int1%10+Int2%10+Ostatok)
        else:
            Result+=str(Int1%10+Int2%10+Ostatok-SistemaSchis)
        Ostatok=(Int1%10+Int2%10+Ostatok)//SistemaSchis
        Int1//=10
        Int2//=10
    if Ostatok!=0:
        Result+=str(Ostatok)
    Oconchatelniy=Result[::-1]
    return Oconchatelniy
def Vichitanie(Int1, Int2, SistemaSchis):
    Zanyatoe = 0
    Result=str()
    while Int1 != 0 or Int2 != 0:
        if (Int1 % 10 - Zanyatoe) >= Int2 % 10:
            Result += str(Int1 % 10 - Zanyatoe - Int2 % 10)
            Zanyatoe = 0
        else:
            Result += str(SistemaSchis + Int1 % 10 - Zanyatoe - Int2 % 10)
            Zanyatoe = 1
        Int1 //= 10
        Int2 //= 10
    Oconchatelniy=Result[::-1]
    return Oconchatelniy
def Umnozhenie(Number1, Number2, SistemaSchis):
    Len1, Len2 = len(Number1), len(Number2)
    Result = [0] * (Len1 + Len2)
    for i in range(Len1 - 1, -1, -1):
        Ostatok = 0
        N1dig = int(Number1[i])
        for j in range(Len2 - 1, -1, -1):
            N2dig = int(Number2[j])
            PromZnach = Result[i + j + 1] + N1dig * N2dig + Ostatok
            Result[i + j + 1] = PromZnach % SistemaSchis
            Ostatok = PromZnach // SistemaSchis
        Result[i] += Ostatok
    Oconchatelniy=(''.join(map(str, Result)).lstrip('0'))
    return Oconchatelniy
SistemaSchis=int(input('Введите систему счисления (от 2 до 10) : '))
Number1=str(input('Введите первое число: '))
Number2=str(input('Введите второе число: '))
Operation=str(input('Введите знак проводимой операции: '))
Resultat=str()
Int1, Int2=int(Number1), int(Number2)
if any(int(d)>SistemaSchis for d in Number1+Number2):
    print('Ошибка: число не соответствует системе счисления')
elif Operation not in '+-*':
    print('Данной операции не существует')
else:
    if Operation=='+':
        Resultat = Slozhenie(Int1, Int2, SistemaSchis)
    elif Operation=='-':
        Resultat = Vichitanie(Int1, Int2, SistemaSchis)
    else:
        Resultat = Umnozhenie(Number1, Number2, SistemaSchis)
    print(f"Результат в системе счисления с основанием {SistemaSchis}: {Resultat}")