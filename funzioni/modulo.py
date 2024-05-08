def menu(TERMINATORE):
    """
    La funzione menu stampa le voci del menu e ritorna la scelta dell'utente, TERMINATORE per uscire.
   
    Parametri (TERMINATORE):
        TERMINATORE: Il terminatore serve per uscire dal programma.
   
    Ritorna (scelta):
        scelta: è l'input dato dall'utente.
   
    """
    msg1 = "Inserire 1 per l'elenco dei docenti di una data classe."
    msg2 = "Inserire 2 per l'orario di un determinato docente e il numero totale delle ore del docente."
    msg3 = "Inserire 3 per il numero di ore a disposizione ('D') di un docente"
    msg4 = "Inserire 4 per elenco dei docenti che hanno lezione (classe o disposizione) una determinata ora di un determinato giorno della settimana (esempio prima ora del lunedì) e numero totale dei docenti"
    msguscita = "Inserire '"+TERMINATORE+"' per uscire."
    tupla_messaggi = (msg1,msg2,msg3,msg4,msguscita)
    for messaggio in tupla_messaggi:
        print(messaggio)
    scelta = input("Cosa vuoi fare? ")
    return(scelta)

def leggidocenti():
    """
    Legge il file csv e genera 2 liste, la prima contiene la lista dei docenti nell'istituto, la seconda, contiene la lista degli orari dei docenti.
    Quindi il primo professore della prima lista avrà il primo orario della seconda lista.
   
    Parametri ():
   
    Ritorna (lista_docenti,lista_orari):
   
        lista_docenti: contiene la lista di tutti i nomi dei docenti nell'istituto.
       
        lista_orari: contiene la lista degli orari di ogni professore.

    """
    filecsv = open("OrarioTabellaGlobale.csv","r")
    riga = filecsv.readline().strip().split(",")
    lista_docenti = []
    lista_orari = []
    while riga != [""]:
        docente = riga[0].strip()
        orario = riga[1:]
        lista_docenti.append(docente)
        lista_orari.append(orario)
        riga = filecsv.readline().strip().split(",")

    lista_docenti = lista_docenti[2:]
    lista_orari = lista_orari[2:]
    filecsv.close()
    return(lista_docenti,lista_orari)

def f1(classe_input, orari, docenti):
    """
    Crea un file dove inserisce i nomi di tutti i docenti della data classe.
   
    Parametri (classe_input, orari, docenti):
   
        classe_input: La classe data dall'utente che deve cercare.
       
        orari: lista di tutti gli orari dei docenti nell'istituto.
        
        docenti: lista di tutti i nomi dei docenti nell'istituto.
   
    Ritorna ():
   
    """
    nomefile = "elencodocenti.txt"
    file1 = open(nomefile,"a")
    file1.close()
    file1 = open(nomefile,"w")
    file1.write("Elenco docenti nella classe " + classe_input + ":\n\n")
    dizionario = {}
    lista_docenti = []
    for i in range(len(docenti)):
        dizionario[docenti[i]] = orari[i]
    for docente in dizionario:
        for ora in dizionario[docente]:
            if ora == classe_input:
                if docente in lista_docenti:
                    pass
                else:
                    file1.write(docente + "\n")
                    lista_docenti.append(docente)
    file1.close()
    print("Controlla il file", nomefile)
    return

def f2(docenti, orari, docente_input):
    """
    Cerca l'orario di un determinato docente e stampa le ore totali di esso.
   
    Parametri (docenti, orari, docente):
   
        docenti: lista di tutti i nomi dei docenti nell'istituto.
       
        orari: lista di tutti gli orari dei docenti nell'istituto.
       
        docente_input: variabile che contiene il cognome e nome del docente da cercare.

    Ritorna ():

    """
    dizionario = {}
    nomefile = "orario " + docente_input.lower() +".txt"
    file2 = open(nomefile,"a")
    file2.close()
    file2 = open(nomefile,"w")
    file2.write("Orario di "+ docente_input + ":\n\n")
    c = 0
    for i in range(len(docenti)):
        dizionario[docenti[i]] = orari[i]
    file2.write("Lu ,Lu ,Lu ,Lu ,Lu ,Lu ,Lu ,Lu ,Ma ,Ma ,Ma ,Ma ,Ma ,Ma ,Ma ,Ma ,Me ,Me ,Me ,Me ,Me ,Me ,Me ,Me ,Gi ,Gi ,Gi ,Gi ,Gi ,Gi ,Gi ,Gi ,Ve ,Ve ,Ve ,Ve ,Ve ,Ve ,Ve ,Ve\n")
    
    for ora in dizionario[docente_input]:
        file2.write(ora + " ")
        if ora != "   ":
            c += 1
    file2.write("\n\n" + docente_input.lower() + " ha " + str(c - 1) + " ore di lezione.")
    file2.close()
    print("Controlla il file", nomefile)
    return

def f3(docenti, orari, docente_input):
    """
    Cerca il numero di ore D di un determinato docente dato dall'utente.
   
    parametri (docenti, orari, docente_input):
       
        docenti: lista di tutti i nomi dei docenti nell'istituto.
       
        orari : lista di tutti gli orari dei docenti nell'istituto.
       
        docente_input: variabile che contiene il cognome e nome del docente da cercare.
       
    Ritorna ():
   
    """
    nomefile = "disposizione " + docente_input.lower() +".txt"
    file3 = open(nomefile,"a")
    file3.close()
    file3 = open(nomefile,"w")
    file3.write("Ore a disposizioni di "+ docente_input + ":\n\n")
    c = 0
    dizionario = {}
    for i in range(len(docenti)):
        dizionario[docenti[i]] = orari[i]
    for ora in dizionario[docente_input]:
        if ora == " D ":
            c += 1
    file3.write(docente_input + " ha " + str(c) + " ore in cui è a disposizione.")
    file3.close()
    print("Controlla il file", nomefile)
    return

def f4(ora_input, giorno_input , orari, docenti):
    """
    Cerca il docente di un determinato giorno a una determinata ora date dall'utente.
   
    Parametri (ora_input, giorno_input , orari, docenti):
       
        ora_input: variabile che contiene l'ora della giornata da cercare.
       
        giorno_input: variabile che contiene il giorno dato dall'utente.
     
        orari : lista di tutti gli orari dei docenti nell'istituto.
        
        docenti: lista di tutti i nomi dei docenti nell'istituto.
   
    Ritorna ():

    """
    nomefile = "elencodocentilezione.txt"
    file4 = open(nomefile,"a")
    file4.close()
    file4 = open(nomefile,"w")
    file4.write("Elenco dei docenti che hanno lezione il "+ giorno_input + " alla " + str(ora_input) + "° ora.\n\n")    
    c = 0
    dizionario = {}
    giorni = {"LUN" : 0,"MAR" : 8,"MER" : 16,"GIO" : 24,"VEN" : 32}
    for i in range(len(docenti)):
        dizionario[docenti[i]] = orari[i]
    for docente in dizionario:
        if dizionario[docente][(ora_input - 1) + (giorni[giorno_input])] != "   ":
            file4.write(docente + "\n")
            c += 1
    file4.write("\nIl " + str(giorno_input) + " alla " + str(ora_input) + " ° ora " + str(c) +" docenti hanno lezione.")
    file4.close()
    print("Controlla il file", nomefile)    
    return