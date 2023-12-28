def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print("====================")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)  
        
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1  
    display_score(correct_guesses, guesses)                  
def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0
def display_score(correct_guesses, guesses):
    print("====================")
    print("Results")
    print("====================")
    
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
        
    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " +str(score)+"%")

questions = {
 "1.What's the value of 'p'?": "A",
 "2.Is water wet?": "B",
 "3.What's my real name?" : "C",
 "4.How much money I currently have on by bank account?": "D"  
}
options = [["A. 3.14","B. 2.14","C. 3.15","D. 2.15"],
           ["A. Yes, it's wet","B. I don't know","C. No, it's dry","D. What is water?"],
           ["A. Unverified","B. Adolf","C. Bohdan","D. How am I supposed to know your real name?"],
           ["A. More then enough","B. Below 1000$","C. Above 1000$","D. None"]]

new_game()