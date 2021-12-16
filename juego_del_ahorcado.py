import random
import os

HANGMAN_IMAGES = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

def cleanScreen(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def getSecretWord():
    words = []
    with open('./archivos/data.txt','r',encoding='utf8') as f:
        for line in f:
            words = [i for i in f] 
            line = line.upper()#Capital leters
            line = line.rstrip()#without spaces
            line = normalize(line)#remove the accents
            words.append(line)

    posicion = random.randint(0, len(words) - 1)
    secret_word = words[posicion]
    return secret_word


def normalize(s): # It removes the accents of a string
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s    

def printHead(word_game, count_wrong):
    label_head = """ 
    ------------------------------------------------------------------------------------------------------------
    ------------------------------------------------------------------------------------------------------------
    ##  ##     ##     ##  ##    ####    ##   ##    ##     ##  ##        ####      ##     ##   ##  ######
    ##  ##    ####    ### ##   ##  ##   ### ###   ####    ### ##       ##  ##    ####    ### ###  ##
    ##  ##   ##  ##   ######   ##       #######  ##  ##   ######       ##       ##  ##   #######  ##
    ######   ######   ######   ## ###   ## # ##  ######   ######       ## ###   ######   ## # ##  ####
    ##  ##   ##  ##   ## ###   ##  ##   ##   ##  ##  ##   ## ###       ##  ##   ##  ##   ##   ##  ##
    ##  ##   ##  ##   ##  ##   ##  ##   ##   ##  ##  ##   ##  ##       ##  ##   ##  ##   ##   ##  ##
    ##  ##   ##  ##   ##  ##    ####    ##   ##  ##  ##   ##  ##        ####    ##  ##   ##   ##  ######
    -------------------------------------------------------------------------------------------------------------
    -------------------------------------------------------------------------------------------------------------
    """    
    print(label_head)
    print(HANGMAN_IMAGES[count_wrong]+ "\n") 
    print('Adivina la palabra oculta\n')
    print(''.join(word_game))

 
def run():
    secret_word = getSecretWord()    

    loser = False
    winner = False
    word_game = ['__ ' for i in range(0, len(secret_word))]

    count_wrong = 0
    max_wrong = len(HANGMAN_IMAGES) - 1

    while loser == False and winner == False:        
        printHead(word_game, count_wrong)
        letter = input('\nIngresa una letra y presiona enter: ')
        letter = letter.upper()

        if letter in secret_word:
            pos = 0
            ini = 0
            fin = len(secret_word)
            while pos >= 0:                
                pos = secret_word.find(letter, ini, fin)
                if pos >= 0:
                    word_game[pos] = letter

                ini = pos + 1

        else:
            count_wrong += 1

        if count_wrong >= max_wrong:
            loser = True
            
        if secret_word == str("").join(word_game):
            winner = True 
        
        cleanScreen()


    printHead(word_game, count_wrong)

    if winner:
        print('\nGANASTE!!!')
    else:
        print('\nPERDISTE!!!')        
        print(f'La palabra oculta era {secret_word}')


if __name__ == '__main__':
    run()