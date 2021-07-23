"""
Created  21:00:34   05/07/2021

Muallif/Author: Xatamjonov Ulug'bek

"""
# Test oluvchi dastur/This is a programm which take a test

class Question:
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer
# test savollari/questions
question_prompts = [
    "  Olmaning rangi qanday ?\n(a) qizil\ko'k\n(b) sariq\n(c) qora\n\n ",
    "Olchaning suvning kimyoviy formulasini qanday ?\n(a) H2\n(b) O2H\n(c) H2O\n\n",
    "Qaysi oyda 28 kun bor ?\n(a) Dekabir\n(b) Febral\n(c) Mart\n\n  " ]
# kalitlar/keys
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"), ]
# Test oluvchi funksia/This is a function which take a test
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Sizda " + str(score) + "/" + str(len(questions)) + " ta to'g'ri javob bor :)\n")
    print("Javoblar:\n1-a\n2-c\n3-b")
    
run_test(questions)







