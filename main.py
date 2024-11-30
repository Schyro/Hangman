import random
from stages import hangman, logo
from words import words as word_list

chose_list = []
selected_word = random.choice(word_list)
blank_word = ["_"] * len(selected_word)
display = ""
guessed = ", "
lives = 6
left_lives = lives
game_over = False

print(logo)

def checkHangman(word):
    print(hangman[lives-left_lives].format(guessed.join(chose_list), word, f"Lives left {left_lives}/{lives}"))

def checkStatus():
    global game_over
    if left_lives == 0:
        game_over = True
        checkHangman(selected_word)
        print("You run out of lives.")
    elif not "_" in blank_word:
        game_over = True
        checkHangman(selected_word)
        print("You got the word.")
    else:
        game_over = False

while not game_over:
    checkHangman(display.join(blank_word))
    choice = input("Guess a letter: ").lower()
    
    if choice in chose_list:
        print("You already guessed this letter.")
        continue

    for i in range(len(selected_word)):
        if selected_word[i] == choice:
            blank_word[i] = choice
    
    if choice in selected_word:
        print("Correct!")
        chose_list.append(choice)
    else:
        print("Wrong!")
        left_lives -= 1
        chose_list.append(choice)

    checkStatus()