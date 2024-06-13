#VARIABILI
risposta_1="sì"
risposta_2="no"
#PROGRAMMA
print("Ciao, sei qui per giocare a carta, forbice e sasso?")
risposta_utente=input()
if risposta_utente==risposta_1:
    print("\nPerfetto, conosci le regole giusto? Giochiamo!")
    print("Scegli la tua mossa!")
    mossa=input()
    from random import choice
    risposte='carta forbice sasso'.split()
    risposta=choice(risposte)
    print("Hai scelto: "+mossa,',io ho scelto:',risposta)
elif risposta_utente==risposta_2:
    print("Va bene, se cambi idea riavvia il programma!")
else:
    print("Qualcosa è andato storto, riprova riavviando il programma!")