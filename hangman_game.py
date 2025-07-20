import random #using random for guessing
words=["red","blue","green","pink","white"] #predefined words 
word=random.choice(words) #so that we can guess a word without giving input as total word
guessed_word=[]
attempts=6   #intialisation of while loop
print("WELCOME TO HANGMAN GAME")
print("THEME IS BASED ON COLOURS")
print("*YOU HAVE 6 CHANCES TO GUESS A WORD*")

print("The word guessed to be :")
print("_ " * len(word)) #space after undercode so that it wont join
while attempts>0:
    guess_letter = input("Enter a letter : ").lower()
    if not guess_letter.isalpha() or len(guess_letter) != 1: #only after checking 2 if , it is used to append a letter to empty list
        print("Enter a single letter")
        continue
    if guess_letter in guessed_word:
        print("Already you guessed")
        continue
    guessed_word.append(guess_letter) #appending
    if guess_letter in word:
        print("Your guess is right")    #checking right or wrong
    else:
        print("Your guess is wrong")
    attempts-=1   #decrement of while loop
    final_word= " "
    for i in word:            #Every time you guess, it loops from 0 to len(word)-1,The loop always runs from the first letter on every guess.so that it even checked it updates.
        if i in guessed_word:
            final_word += i+" "   #add space after letter(" ")
        else:
            final_word += "_ "     #add undercode if not guessed(space after undercode so that it wont join)
    print("WORD IS : " , final_word.strip())
    if "_" not in final_word:
        print("YOU WON! , YOU GUESSED THE WORD RIGHT & THE WORD IS : ",word)
        break
    else:
        print(f"REMAINING TRIES : {attempts}")
if attempts==0:
    print("GAME OVER! YOU LOST ALL YOUR CHANCES & THE WORD YOU MISSED IS : ",word)
    
