import random


class EmptyError(Exception):
    def __init__(self, message):
        super().__init__(message)


answers = {
        "Так": 1,      
        "Ні": 30,       
        "Можливо": 1    
    }



def charivna_kulka(question):
    """
    charivna_kulka(question)\n
    takes one argument: 'question' , typed string\n
    returns 'Так' 'Ні' 'Можлвио' , typed string\n
    """
    try:
        if not isinstance(question, str): raise TypeError('Питання повинно бути рядком')
        if len(question) == 0: raise EmptyError('Питання не може бути пустим')

        
        weights = [answers[ans] for ans in answers]
        chosen_answer = random.choices(list(answers.keys()), weights=weights, k=1)[0]
        return chosen_answer

    except TypeError as e:
        return f"Помилка: {e}"
    
    except EmptyError as e:
        return f"Помилка: {e}"

def configure_magic_ball(new_answers: list):
    """
    configure_magic_ball(new_answers: list)\n
    takes one argument: 'new_answers' , typed list\n
    adds the elements of the list to answers list of the magic ball\n
    """
    for choice in new_answers:
        answers[choice] = 1

configure_magic_ball(['50/50', 'Незнаю'])

for i in range(5):
    print(charivna_kulka('Question'))
