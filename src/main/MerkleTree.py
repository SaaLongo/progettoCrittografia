# import delle librerie
import hashlib, json
from collections import OrderedDict


# dichiarazione della classe
class MerkleTree:

    # inizializzazione
    def __init__(self, listoftransaction=None):
        self.listoftransaction = listoftransaction
        self.past_transaction = OrderedDict()

    # creazione del Merkle Tree
    def create_tree(self):
        listoftransaction = self.listoftransaction
        past_transaction = self.past_transaction
        temp_transaction = []

        for index in range(0, len(listoftransaction), 2):

            # prendere l'elemento più a sinistra
            current = listoftransaction[index]

            # Se è ancora presente l'indice sinistro, ottenere la parte destra dell'elemento più a sinistra
            if index + 1 != len(listoftransaction):
                current_right = listoftransaction[index + 1]

            # 3.4 Se è stato raggiunto il limite della lista, creare una stringa vuota
            else:
                current_right = ''

            # applicare la funzione Hash 256 sui valori correnti
            current_hash = hashlib.sha256(current)

            # se l'hash di destra corrente non è una stringa vuota
            if current_right != '':
                current_right_hash = hashlib.sha256(current_right)

            # aggiungere la transazione al dizionario
            past_transaction[listoftransaction[index]] = current_hash.hexdigest()

            # se il prossimo valore a destra non è vuoto
            if current_right != '':
                past_transaction[listoftransaction[index + 1]] = current_right_hash.hexdigest()

            # creazione di una nuova lista di transazioni
            if current_right != '':
                temp_transaction.append(current_hash.hexdigest() + current_right_hash.hexdigest())

            # se l'elemento più a sinistra è una stringa vuota, aggiungere solo il valore corrente
            else:
                temp_transaction.append(current_hash.hexdigest())

        # aggiornare le variabili e rieseguire la funzione
        if len(listoftransaction) != 1:
            self.listoftransaction = temp_transaction
            self.past_transaction = past_transaction

            # chiamare la funzione finchè non si ottiene la root
            self.create_tree()

    # ritornare la transazione past
    def Get_past_transacion(self):
        return self.past_transaction

    # ritornare la root della transazione
    def Get_Root_leaf(self):
        last_key = self.past_transaction.keys()[-1]
        return self.past_transaction[last_key]


# main
if __name__ == "__main__":
    # creazione di una nuova classe Merkle Tree
    Merkle_Tree = MerkleTree()

    # lista di transazioni
    transaction = ['a', 'b', 'c', 'd']

    # aggiunta della lista all'albero
    Merkle_Tree.listoftransaction = transaction

    # creazione della transazione sull'albero
    Merkle_Tree.create_tree()

    # recupero della transazione
    past_transaction = Merkle_Tree.Get_past_transacion()

    # recupero dell'ultima transazione
    print
    'Final root of the tree : ', Merkle_Tree.Get_Root_leaf()
    print(json.dumps(past_transaction, indent=4))
    print
    "-" * 50