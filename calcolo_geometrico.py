# utilizzo def per impostare i comandi per il calcolo del perimetro geometrico
def calcoloraggiocerchio(raggio):
    return 2 * raggio
def calcoloperimetrorettangolo(larghezza, lunghezza):
    return 2 * (larghezza + lunghezza)
def calcoloperimetroquadrato(lato):
    return 4 * lato
# con def main() imposto il print per avere ogni risultato di ogni singola figura geometrica
def main():
    print("Scegli una figura Geometrica:")
    print("1. cerchio")
    print("2. rettangolo")
    print("3. quadrato")
# imposto una variabile che mi permette di scegliere la figura geometrica
    figurageometrica = int(input("inserire numero corrispondente alla figura geometrica"))

# utilizzo if ed elif per impostare le scelte numeriche assegnate ad ogni figura geometrica
# operazione di calcolo per il perimetro geometrico del cerchio
    if figurageometrica == 1:
        raggio = float(input("inserire il raggio del cerchio:"))
        raggio = calcoloraggiocerchio(raggio)
        print(f"il raggio del cerchio corrisponde a: {raggio}")
# operazione di calcolo per il perimetro del rettangolo
    elif figurageometrica == 2:
         larghezza = float(input("inserire la larghezza del rettangolo:"))
         lunghezza =float(input("inserire la lunghezza del rettangolo:"))
         perimetro =calcoloperimetrorettangolo(larghezza, lunghezza)
         print(f"il perimetro del rettangolo corrisponde a: {perimetro}")
# operazione di calcolo per il perimetro geometrico del quadrato
    elif figurageometrica == 3:
         lato = float(input("inserire lunghezza lato quadrato"))
         perimetro = calcoloperimetroquadrato(lato) 
         print(f"il perimetro del quadrato corrsiponde a: {perimetro}")
#utilizzo else per rivecere risposta in caso non inserisca un numero corripondente 
    else:
        print("Error: non presente nel database.")

if __name__ == "__main__":
    main()


       









