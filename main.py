import sys
sys.path.append('funzioni')
import modulo
import os
def main():
    os.system("cls")
    esci = False
    TERMINATORE = "!!!"

    while not(esci):
        print()
        print("-" * 80)
        scelta_utente = modulo.menu(TERMINATORE)

        if scelta_utente == "1":
            classe_input = input("Inserire classe (esempio: 3gi) ").upper()
            
            docenti = modulo.leggidocenti()[0]
            
            orari = modulo.leggidocenti()[1]
            
            modulo.f1(classe_input, orari, docenti)
            
        elif scelta_utente == "2":
            docente = input("Inserire cognome e nome docente: ").upper()

            # creo una lista con i nomi e i cognomi dei docenti, i docenti con un cognome a due parole hanno solo il cognome 
            docenti = modulo.leggidocenti()[0]
            
            orari = modulo.leggidocenti()[1]
            
            modulo.f2(docenti,orari,docente)  

        elif scelta_utente == "3":
            docente = input("Inserire cognome e nome docente: ").upper()
            
            docenti = modulo.leggidocenti()[0]
            
            orari = modulo.leggidocenti()[1]
            
            modulo.f3(docenti,orari,docente)
            
        elif scelta_utente == "4":
            ora_input = 0
            while ora_input == 0:
                try:
                    ora_input = int(input("Inserire ora (esempio : 1): ").upper())
                    if ora_input <= 0 or ora_input >= 9:
                        print("Digitare un intero compreso tra 1 e 8.")
                        ora_input = 0
                except:
                    print("Digitare un intero compreso tra 1 e 8.")
                    pass
            giorno_input = input("Inserire giorno (esempio : lun) ").upper()
            
            docenti = modulo.leggidocenti()[0]
            
            orari = modulo.leggidocenti()[1]
            
            modulo.f4(ora_input, giorno_input , orari, docenti)
        
        elif scelta_utente == TERMINATORE:
            print("uscito")
            esci = True
        
        else:
            print("Hai scelto una voce inesistente.")
    return
main()