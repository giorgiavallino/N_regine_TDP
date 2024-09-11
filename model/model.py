import copy

# Definire la classe Model
class Model:

    # Definire il metodo __init__
    def __init__(self):
        self.N_soluzioni = 0 # variabile aggiunta per calcolare delle statistiche
        self.N_iterazioni = 0 # variabile aggiunta per calcolare delle statistiche
        self.soluzioni = [] # variabile inserita per determinare le soluzioni effettive del problema (senza eventuali
        # duplicati)

    # Definire il metodo risolvi_n_regine, all'interno del quale verrà utilizzato il metodo _ricorsione
    def risolvi_n_regine(self, N):
        # Bisogna sempre resettare le variabili inizializzate nell'__init__
        self.N_soluzioni = 0
        self.N_iterazioni = 0
        self.soluzioni = []
        self._ricorsione([], N) # il parziale iniziale è quasi sempre una lista vuota

    # Definire il metodo _ricorsione
    def _ricorsione(self, parziale, N):
        self.N_iterazioni = self.N_iterazioni + 1 # per calcolare delle statistiche
        # Caso terminale
        if len(parziale) == N:
            # La soluzione viene aggiunta solo se è nuova attraverso il relativo metodo _soluzione_nuova
            if self._soluzione_nuova(parziale):
                self.N_soluzioni = self.N_soluzioni + 1 # per calcolare delle statistiche
                self.soluzioni.append(copy.deepcopy(parziale)) # il parziale viene copiato all'interno della lista
                # soluzioni solo qualora superi il test _soluzione nuova
        # Caso ricorsivo
        for row in range(N):
            for col in range(N):
                parziale.append((row, col))
                # Se è ammissibile, viene fatta la ricorsione
                if self._regina_ammissibile(parziale):
                    self._ricorsione(parziale, N)
                parziale.pop() #backtraking

    # Definire il metodo _regina_ammissibile
    def _regina_ammissibile(self, parziale):
        # Se la lunghezza del parziale è uno, allora è ammissibile per forza... la regina può, infatti, essere
        # posizionata ovunque
        if len(parziale) == 1:
            return True
        # Se la lunghezza è maggiore di uno,...
        ultima_regina = parziale[-1] # scrivendo così si intende l'ultimo elemento della lista
        for regina in parziale[:len(parziale)-1]:
            # Bisogna controllare le righe, le colonne e le diagonali
            # La regina non deve essere lungo la riga delle regine precedenti
            if ultima_regina[0] == regina[0]:
                return False
            # La regina non deve essere lungo la colonna delle regine precedenti
            if ultima_regina[1] == regina[1]:
                return False
            # La regina non deve essere lungo la diagonale delle regine precedenti
            if (ultima_regina[0] - ultima_regina[1]) == (regina[0] - regina[1]):
                return False
            if (ultima_regina[0] + ultima_regina[1]) == (regina[0] + regina[1]):
                return False
        return True

    # Definire il metodo _soluzione_nuova, che permette di verificare che le soluzioni proposte siano effettivamente
    # nuove
    def _soluzione_nuova(self, soluzione_nuova):
        # Per ogni soluzione presente nella lista delle soluzioni già immagazzinate,...
        for soluzione in self.soluzioni:
            # Per ogni regina della nuova_soluzione, se la regina si trova nella lista soluzioni allora la soluzione
            # non è nuova... in altre parole, vuol dire verificare se la nuova soluzione è equivalente a una
            # configurazione precedente
            for regina in soluzione_nuova:
                if regina in soluzione:
                    return False
        return True

# Prova
if __name__ == '__main__':
    model = Model()
    model.risolvi_n_regine(4)
    print(f"L'algoritmo ha trovato {model.N_soluzioni} soluzioni.")
    print(f"L'algoritmo ha chiamato la funzione ricorsiva {model.N_iterazioni} volte.")
    print(f"Le soluzioni sono: {model.soluzioni}")