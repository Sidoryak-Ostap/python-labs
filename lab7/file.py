import random

answers = ['Ні', 'Так', 'Можливо']

class EmptyError(Exception):
    def __init__(self, message):
        super().__init__(message)

def charivna_kulka(question):
    """
    charivna_kulka(question)\n
    takes one argument: 'question' ,typed string\n
    returns 'Так' 'Ні' 'Можлвио' , typed string\n
    """
    try:
        if not isinstance(question, str): raise TypeError('Питання повинно бути рядком')
        if len(question) == 0: raise EmptyError('Питання не може бути пустим')

        answer_index = random.randint(0, len(answers) - 1)
        return answers[answer_index]

    except TypeError as e:
        return f"Помилка: {e}"
    
    except EmptyError as e:
        return f"Помилка: {e}"

def configure_magic_ball(new_answers: list):
    answers.extend(new_answers)
