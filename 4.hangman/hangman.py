import random 
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # Randomly chooses something from the list
    
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word


def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    
    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        # Lives used
        print(f"Tienes {lives} restantes.")
        
        # letters used
        print("Has usado estas letras: ", ' '.join(used_letters))
        # what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        
        print("Palabra: ", ' '.join(word_list))
        
        user_letter = input('Introduce una letra: ').upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('letter is not in word.')
        elif user_letter in used_letters:
            print("Ya utilizaste esta letra. Intentalo de nuevo.")
        else:
            print("Caracter invalido. Intentalo de nuevo.")
    
    #Gets here when word_letters = 0 or lives = 0
    if lives == 0:
        print("Game Over!")
    else:
        print(f"Felicidades ganaste la palabra es {word_list}")
    
    
hangman()