
try:
    file = open('document.txt', 'w')
    file.write("""fecha_Especificacion_costo_valor
                    03/03/1997 laptop1 3000000$ 3500001$
                    03/04/1997 laptop2 300002$ 3500200$
                    03/05/1997 laptop3 3000430$ 3500070$
                    03/06/1997 laptop4 300005460$ 3590000$
                    03/07/1997 laptop5 3000067$ 35670000$
                    03/08/1997 laptop6 3000002$ 3508000$

                    """)
    file.close()
except TypeError as err:
    print(err)


def recognyze_file():
    archivo = open('document.txt', 'r')
    ar = []
    for f in archivo:
        nen = f.replace("_", " ")
        nen2 = nen.split()
        if nen2 not in ar:
            ar.append(nen2)

    archivo.close()
    return ar


def characters_analyze(char):
    texts = ""
    count = 0
    for i in char:
        for x in range(len(i*len(char*2))-2):
            print('-', end='')
        print('+')
        print('\n')
        for item in i:
            texts += item + ","
            count += 1
            print('|  {}\t'.format(item), end=' ')
        print('\n')
    for i in char[0]:
        for it in range(len(i*len(char[0]))-13):
            print('-',end='')
    print('+')
    print('\n')

filereg = recognyze_file()

analy = characters_analyze(filereg)
