question = int(input("introduce un numero: "))


def parImpar(ques):
    if ques %2 == 0:
        print("{} es un numero par".format(ques))
    else:
        print("{} es un  numero impar".format(ques))

parImpar(question)