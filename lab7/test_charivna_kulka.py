from file import charivna_kulka, configure_magic_ball, answers

def test_kulka():
    assert charivna_kulka('ss') in answers
    
def test_kulka_string():
    assert type(charivna_kulka('some string')) == str
    
def test_kulka_is_string():
    assert charivna_kulka(5) == 'Помилка: Питання повинно бути рядком'
    
def test_kulka_is_empty():
    assert charivna_kulka('') == 'Помилка: Питання не може бути пустим'
    
def test_configure_magic_ball():
    configure_magic_ball(['Наступного разу', 'За умови що ви чоловік'])
    assert charivna_kulka('some question') in answers