import random

class hangman:
    def __init__():
        pass

    def select_word():
        words = '/usr/share/dict/words'
        dictionary = []
        with open(words, 'r') as wf:
            words = wf.readlines()
        for word in words:
            dictionary.append(word.strip())
        
        r = random.randint(0,len(dictionary))

        word = dictionary[r]
        
        return word
    
    def draw_display(word):
        hidden_word = []
        for _ in range(len(word)):
            hidden_word.append('•')
   
        return hidden_word

    
    def redraw_display(word, display, cmd):
        for i in range(len(word)):
            if word[i] == cmd:
                display[i] = cmd
        
        return display
       
    def handle_input(word, letters, display, used, cmd):
        if len(cmd) > 1:
            print('Only a single character is accepted as an input')
            return False
        
        if cmd not in used:
            used[cmd] = True
            if cmd in letters:
                return True
        else:
            print("Hey you've already used: " + cmd)
            return False

    def count_letters_left(word, letters_left):
        for i in range(len(word)):
            if word[i] != '•':
                letters_left -= 1

        return letters_left

    def word_complete(display):
        display = display
        if '•' not in display:
            print('     '.join(display))
            print('You win!')
            return True
        return False

    def check_status(word, guesses_left):
        if guesses_left == 0:
            print('You Lost! The word was ' + word)
            return True
        
        return False

    def play_again(cmd):
        if cmd == 'y':
            return True
        
        return False

    def start_session(word):
        session_started = True
        display = hangman.draw_display(word)
        letters = set(word)
        used = {}
        guesses_left = 5
        
        while session_started:
            print('     '.join(display))
            print('Guesses left: ' + str(guesses_left))
            cmd = input('Select a letter: ')
            if hangman.handle_input(word,letters, display, used, cmd):
                display = hangman.redraw_display(word, display, cmd)
            else:
                guesses_left -= 1

            if hangman.check_status(word, guesses_left) or hangman.word_complete(display):
                session_started = False
        
        #ask to play the game again
        print('Play Again?')
        cmd = input('press y to play again or any other key to exit: ')
        if hangman.play_again(cmd):
            hangman.start_game()
        

    def start_game():
        word = hangman.select_word()
        hangman.start_session(word)
        return
    
hangman.start_game()