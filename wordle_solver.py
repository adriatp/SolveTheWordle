# ----------------
# SOLVE THE WORLDE
# ----------------

# Importem llibraries
import json
import re

# Inicialitzem constants
WORD_LENGTH = 5


###########
## Funcions
###########

def update_tried_letters(tried_letters, word):
    for i in range(len(word)):
        letter = word[i]
        reps = word[:i].count(letter)
        regex_letter = '^.*' + letter + '.*'
        for i in range(reps):
            regex_letter = regex_letter + letter + '.*'
        regex_letter = regex_letter + '$'
        tried_letters.add(regex_letter)


def update_found_letters(found_letters, res_word, word):
    for i in range(len(word)):
        letter = word[i]
        res_letter = res_word[i]
        if res_letter == 'c' or res_letter == 'm':
            reps = word[:i+1].count(letter)
            found_letters.add(str(reps) + letter)


def different_leters_in_words(possible_words):
    diff_letters = set()
    for word in possible_words:
        for i in range(len(word)):
            letter = word[i]
            reps = word[:i].count(letter)
            regex_letter = '^.*' + letter + '.*'
            for i in range(reps):
                regex_letter = regex_letter + letter + '.*'
            regex_letter = regex_letter + '$'
            diff_letters.add(regex_letter)
    return diff_letters


def words_without_more_no_tried_letters(original_words, tried_letters):
    # Obtenim un llistat amb la quantitat de lletres provades que te cada paraula
    tried_letters_by_words = [0] * len(original_words)
    for regex_tl in tried_letters:
        for i in range(len(original_words)):
            word = original_words[i]
            if re.match(regex_tl, word):
                tried_letters_by_words[i] = tried_letters_by_words[i] + 1
    # Ordenem el llistat de les repeticions 
    min_rep = min(tried_letters_by_words)
    indices_best_words = [i for i in range(len(tried_letters_by_words)) if tried_letters_by_words[i] == min_rep]
    return [original_words[i] for i in indices_best_words]


def words_with_more_letters(words, letters):
    # Obtenim un llistat amb la quantitat de lletres provades que te cada paraula
    recount = [0] * len(words)
    for regex_tl in letters:
        for i in range(len(words)):
            word = words[i]
            if re.match(regex_tl, word):
                recount[i] = recount[i] + 1
    # Ordenem el llistat de les repeticions 
    min_rep = max(recount)
    indices_best_words = [i for i in range(len(recount)) if recount[i] == min_rep]
    return [words[i] for i in indices_best_words]
	
	
	
############
## Main code
############

# Demanar el diccionari
lang = input("Lang (ca/es/en): ").lower()

while True:
    # Loading dictionary
    print('Loading ' + lang + ' dictionary')
    
    # Llegir paraules possibles de fitxer i guardar-les en una llista
    with open('lang/' + lang + '.json') as json_file:
        original_words = json.load(json_file)
	
    # Fem una copia del diccionari original
    possible_words = original_words.copy()
    
    # Inicialitzem un conjunt buit on inclourem les lletres trobades
    # S'indicarà les repeticions provades en una paraula amb el número (ex. 2l)
    found_letters = set()
    
    # Inicialitzem un conjunt buit on inclourem les lletres provades
    tried_letters = set()
        
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
        update_tried_letters(tried_letters, word)
            
        # Actualitzem el conjunt de lletres trobades
        update_found_letters(found_letters, res_word, word)
    
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
        print('Possible words: ' + str(possible_words))
        print("Recount: " + str(len(possible_words)))
	
        # En cas que no s'hagin trobat totes les lletres suggerim la millor paraula en funció de les lletres no provades de les paraules possibles
        if len(found_letters) != WORD_LENGTH:
            # Aqui cal agafar les lletres que queden a les paraules possibles
            different_letters = different_leters_in_words(possible_words)
            # print("Different letters in words: " + str(different_letters))
			
			# Aqui cal obtenir les lletres de les anteriors que encara no s'han provat 
            suggested_letters = different_letters - tried_letters
            # print("Suggested letters: " + str(suggested_letters))
			
            # Aqui cal obtenir les paraules que tenen més lletres de les anteriors
            suggested_words = words_with_more_letters(original_words, suggested_letters)
            # print("Suggested words: " + str(suggested_words))
			
            # Obtenim les paraules del diccionari que contenen més lletres no provades
            # suggested_words = words_without_more_no_tried_letters(original_words, tried_letters)
		
		    # Suggerim una de les paraules
            print('Suggested words: ' + str(suggested_words))
            print("Recount: " + str(len(suggested_words)))
        
        
	
	
