# ----------------
# SOLVE THE WORLDE
# ----------------

# Importem llibraries
import json
import re

# Llegir paraules possibles de fitxer i guardar-les en una llista
with open('words_es.json') as json_file:
    possible_words = json.load(json_file)

# Filtrar paraules que no tinguin 5 lletres
possible_words = list(filter(lambda x: len(x) == 5, possible_words))
print(possible_words)

# Mentrestant
while True:
	
	# Llegim intent de paraula
    word = input("Try a word: ").lower()
    
    # Llegim resultat de l'intent (c/m/i) - (Correct/Misplaced/Incorrect)
    res_word = input("Result: ").lower()
    
    # Per cada lletra actualitzem la llista:    
    for i in range(len(word)):
    
        # Obtenim la lletra
        letter = word[i]
        
        # Obtenim el resultat de la lletra
        res_letter = res_word[i]
    
        # Cas que la lletra estigui i en la posició que toca:
        if res_letter == 'c':
        
            # Eliminar les paraules que no tinguin la lletra a la posició, et quedes amb les que tenen la lletra a la posició
            possible_words = list(filter(lambda w: re.match('^.{' + str(i) + '}' + letter + '.*$', w), possible_words))
        
        # Altrament
        else:
            # Contar quantes vegades es repeteix la lletra a la paraula
            times_repeated = word.count(word[i])
            
            # Si la lletra es repeteix en les lletres de la paraula introduïda que falten avaluar:
            if True:
                # 
            # Altrament
            else:
                # Cas que la lletra estigui però no en la posició que toca:
                if res_letter == 'm':
                
                    # Eliminar les que no tinguin la lletra, et quedes amb les que tenen la lletra
                    possible_words = list(filter(lambda w: re.match('^.*[' + letter + '].*$', w), possible_words))
                    
                    # Eliminar les que tinguin la lletra a la posició, et quedes amb les que no tenen la lletra a la posició
                    possible_words = list(filter(lambda w: re.match('^.{' + str(i) + '}[^' + letter + '].*$', w), possible_words))
                
                # Cas que la lletra no estigui
                elif res_letter == 'i':
                
                    # Eliminar de la llista les paraules que continguin la lletra, et quedes amb les que està 
                    possible_words = list(filter(lambda w: re.match('^((?!' + letter + ').)*$', w), possible_words))
        
        print(possible_words)
	# Mostrem les paraules que queden (la quantitat si és molt gran)
