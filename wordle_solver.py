# ----------------
# SOLVE THE WORLDE
# ----------------

# Importem llibraries
import json
import re

# Inicialitzem constants
WORD_LENGTH = 5

# Demanar el diccionari
lang = input("Lang (ca/es/en): ").lower()

while True:
    # Loading dictionary
    print('Loading ' + lang + ' dictionary')
    
    # Llegir paraules possibles de fitxer i guardar-les en una llista
    with open('lang/' + lang + '.json') as json_file:
        possible_words = json.load(json_file)
    
    # Inicialitzem un conjunt buit on inclourem les lletres trobades
    found_letters = {}
    
    # Inicialitzem un conjunt buit on inclourem les lletres provades
    tried_letters = {}
        
    # Filtrar paraules que no tinguin WORD_LENGTH lletres
    possible_words = list(filter(lambda x: len(x) == WORD_LENGTH, possible_words))
    # print(possible_words)

    # Actualitzem les paraules possibles
    while len(possible_words) > 1:
    
        # Llegim intent de paraula
        word = input("Try a word: ").lower()
    
        # Llegim resultat de l'intent (c/m/i) - (Correct/Misplaced/Incorrect)
        res_word = input("Result: ").lower()
        
        # Actualitzem el conjunt de lletres provades
        tried_letters.add(letter)
            
        # Actualitzem el conjunt de lletres trobades
        if res_letter == 'c' or res_letter == 'm':
            found_letters.add(letter)
    
        # Per cada lletra actualitzem la llista:    
        for i in range(len(word)):
    
            # Obtenim la lletra
            letter = word[i]
        
            # Obtenim el resultat de la lletra
            res_letter = res_word[i]
    
            # Cas que la lletra estigui i en la posició que toca:
            if res_letter == 'c':
            
                # Regex (ex: ^.{1}a.*$ )
                regex_letter_pos = '^.{' + str(i) + '}' + letter + '.*$'
        
                # Eliminar les paraules que no tinguin la lletra a la posició, et quedes amb les que tenen la lletra a la posició
                possible_words = list(filter(lambda w: re.match(regex_letter_pos, w), possible_words))
            
            # Cas que la lletra estigui però no en la posició que toca:
            elif res_letter == 'm':
        
                # Contem la quantitat de vegades que la lletra apareix a la paraula
                letter_reps = str(len([word_pos for word_pos, word_letter in enumerate(word) if word_letter == letter and (res_word[word_pos] == 'c' or res_word[word_pos] == 'm')]))
        
                # Regex (ex: ^.*[a].*$ )
                # regex_no_letter = '^.*[' + letter + '].*$'
            
                # Regex (ex: ^(?:[^a]*a){3}[^a]*$ )
                regex_letter_min_X_times = '^(?:[^' + letter + ']*' + letter + '){' + letter_reps + ',}[^' + letter + ']*$'
        
                # Eliminar les que no tinguin la lletra, et quedes amb les que tenen la lletra
                possible_words = list(filter(lambda w: re.match(regex_letter_min_X_times, w), possible_words))
            
                # Regex (ex: ^.{2}[^a].*$ )
                regex_no_letter_pos = '^.{' + str(i) + '}[^' + letter + '].*$'

                # Eliminar les que tinguin la lletra a la posició, et quedes amb les que no tenen la lletra a la posició
                possible_words = list(filter(lambda w: re.match(regex_no_letter_pos, w), possible_words))
        
	    # Cas que la lletra no estigui
            elif res_letter == 'i':
        
                # Contem la quantitat de vegades que la lletra apareix a la paraula
                letter_reps = str(len([word_pos for word_pos, word_letter in enumerate(word) if word_letter == letter and (res_word[word_pos] == 'c' or res_word[word_pos] == 'm')]))
            
                # Regex (ex: ^(?:[^a]*a){3}[^a]*$ )
                regex_letter_X_times = '^(?:[^' + letter + ']*' + letter + '){' + letter_reps + '}[^' + letter + ']*$'
            
                # Eliminar de la llista les paraules que continguin la lletra més o menys vegades que letter_reps, et quedes amb les que en tenen igual
                possible_words = list(filter(lambda w: re.match(regex_letter_X_times, w), possible_words))
        
        # Mostrem les paraules que queden (la quantitat si és molt gran)
        print(possible_words)
        print("Possible words: " + str(len(possible_words)))
	
    # En cas que no s'hagin trobat totes les lletres suggerim la millor paraula en funció de les lletres no provades de les paraules possibles
    if len(found_letters) != WORD_LENGTH:
        
        
        
    
    # En cas que encara quedin incorrectes (res_word contingui 'i')
    # Obtenim les lletres de les paraules possibles que encara no s'han provat
    
    # 
	
	
	
