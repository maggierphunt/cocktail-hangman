import time
from flask import Flask, render_template, request, Response
import os

app = Flask("cocktail-hangman") #making an app

#Homepage
@app.route("/")  
def landing_page():
    name = input("What is your name? ")

    print ("Hello, " + name, "Time to play hangman!")

    #wait for 1 second
    time.sleep(1)

    print ("Start guessing...")
    time.sleep(0.5)

    #here we set the secret. You can select any word to play with. 
    word = ("pythonbite")

    #creates an variable with an empty value
    guesses = ''

    #determine the number of turns
    turns = 20

    # Create a while loop

    #check if the turns are more than zero
    while turns > 0:         

        # make a counter that starts with zero
        failed = 0             

        # for every character in secret_word    
        for char in word:      

        # see if the character is in the players guess
            if char in guesses:    

            # print then out the character
                print (char,end=""),    

            else:
        
            # if not found, print a dash
                print ("_",end=""),
        
            # and increase the failed counter with one
                failed += 1    

        # if failed is equal to zero

        # print You Won
        if failed == 0:        
            print ("You won")
        # exit the script
            break            
        # ask the user go guess a character
        guess = input("guess a character:") 

        # set the players guess to guesses
        guesses += guess  
            # turns counter decreases with 1 (now 9)
        turns -= 1 
        print ("You have", + turns, 'more guesses' )                     

        # if the guess is not found in the secret word
        if guess not in word: 
        # print wrong
            print ("Wrong")  

        # if the turns are equal to zero
            if turns == 0:           
        
            # print "You Lose"
                print ("You Lose"  )

    return render_template("index.html", name=name)


# @app.route("/success")  
# def video():
#     return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
