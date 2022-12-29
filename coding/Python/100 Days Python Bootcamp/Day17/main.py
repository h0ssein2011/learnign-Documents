from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain


questions = [q['text'] for q in question_data]
answers = [a['answer'] for a in question_data]

question_bank = [Question(txt,ans) for txt,ans in zip(questions,answers)]
# print(question_bank[12].text,question_bank[12].answer)


text_quiz = Quiz_Brain(question_bank)

while text_quiz.still_has_question:
    text_quiz.next_question()
