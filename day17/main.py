# Rich Whiffen - 9/9/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 17 - making our own classes
#
# Quiz game - lots of sample code provided in the class files


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

DEBUG = False
question_bank = []

for item in question_data:
    if DEBUG:
        print("inside for loop")
        print(item["text"],item["answer"])
    add_question = Question(item["text"],item["answer"])
    if DEBUG:
        print (add_question.text)
        print (add_question.answer)

    question_bank.append(add_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_quesions():
    quiz.next_question()

print(" You completed the quiz")
print(f" your final score is {quiz.score} out of {len(question_bank)}")
