#CONSEGNA SETTIMANA 3 LEZIONE 3

#importazione delle librerie
import math

#funzione calcolo perimetro quadrato
def perimetroQuadrato():
    latoQ=float(input("Inserisci il lato del quadrato: "))
    perimetroQ=latoQ*4

    print("\n")
    print("Il perimetro del quadrato è:",f'{perimetroQ:.2f}')

#funzione calcolo circonferenza cerchio
def circonferenzaCerchio():
    raggio=float(input("Inserisci il raggio del cerchio: "))
    circonferenza=raggio*2*math.pi
    
    print("\n")
    print("La circonferenza del cerchio è:",f'{circonferenza:.2f}')

#funzione calcolo perimetro rettangolo
def perimetroRettangolo():
    base=float(input("Inserisci la base del rettangolo: "))
    altezza=float(input("Inserisci l'altezza del rettangolo: "))
    perimetroR=(base+altezza)*2

    print("\n")
    print("Il perimetro del rettangolo è:",f'{perimetroR:.2f}')

#funzione scelta dell'operazione tramite match-case
def sceltaOperazione():
    print("-----------------------------------")
    print('1. Calcolo perimetro del quadrato')
    print('2. Calcolo circonferenza del cerchio')
    print('3. Calcolo perimetro del rettangolo')
    print("-----------------------------------\n")

    choice = int(input("Seleziona l'opzione desiderata: "))
    print("\n")

    match choice:
        case 1:
            perimetroQuadrato()
        case 2:
            circonferenzaCerchio()
        case 3: 
            perimetroRettangolo()
        case _:
            print("Non hai inserito un valore valido\n")
            sceltaOperazione()

#funzione "main"
print('--- BENVENUTO NEL PROGRAMMA ---\n')
sceltaOperazione()

