
import book_info
import uuid
import random

# Загальний клас книжок
class Book():
    def __init__(self, type):
        self.title = ''
        self.type = type
        self.author = ''
        self.pages = []


    def show_pages(self):
        for page in self.pages:
            print(page)

    def __str__(self):
        return f'Автор: {self.author}\nНазва: {self.title}\nК-сть сторінок: {len(self.pages)}\nТип: {self.type}\n'


# Клас для наукових книжок
class ScientificBook(Book):
    def __init__(self, type):
        super().__init__(type)
        self.list_of_references = []
        self.glosary = []

    #Виведення використаних джерел
    def show_references(self):
        print("Використані джерела:")
        for ref in self.list_of_references:
            print(ref, end='\n')
        print()
    # Виведення слів та їх терміни
    def show_glosary(self):
        print("Терміни та поняття:")
        for glos in self.glosary:
            print(glos, end='\n') 
        print()
    
# Клас для Балетристика
class FictionBook(Book):
    def __init__(self, type):
        super().__init__(type)
        self.character_list = []
        self.character_desc = []

    # Вивести назви персонажів 
    def show_characters(self):
        print("Персонажі")
        print(self.character_list)
    # Вивести опис персонажів
    def show_characters_desc(self):
        print("Опис персонажів")
        print(self.character_desc)

# Клас посібника  
class ManualBook(Book):
    def __init__(self,  type):
        super().__init__(type)
        self.pictures = []

    # Метод показу картинок
    def show_pictures(self):
        print("Картинки")
        print(self.pictures)

# Клас сторінки
class Page():
    def __init__(self, page_text, num):
        self.page_text = page_text
        self.page_num = num

    def change_page_num(self, id):
        self.page_num = id
        return self
    
    def __str__(self):
        return f'Сторінка №{self.page_num}\n{self.page_text}\n'   
    
# Білдер загальний
class BookBuilder():
    def __init__(self, book):
        self.book = book

    # Вказати автора 
    def set_author(self, author = ''):
        if(author == ''):
            author = input("Введіть автора\n")
            self.book.author = author
        else:
            self.book.author = author
        return self
    
    # Вказати назву книги (можна просто передати назву)
    def set_title(self, title = ''):
        if(title == ''):
            title = input("Введіть назву\n")
            self.book.title = title
        else: 
            self.book.title = title
        return self
    
    def set_page(self):
        page_register = PageRegister()

        write = True
        num = 1
        while write:
            page = input("Заповніть сторінку:\n")
            page = Page(page, num)
            self.book.pages.append(page)

            #Додавання сторінки в реєестр з унікальним id
            page_register.add_page(page)
            num+=1

            action = int(input(print("1. Заповнити наступну сторінку\n2. Закінчити заповнювати")))
            match action:
                case 1: pass
                case 2: write = False
        return self

    #Загальна функція для заповнення різних використаних джерел, посилань і глосарій і тд
    def fill_list(self, list, prompt):
        fill = True
        while fill:
            data = input(prompt)
            list.append(data)
            action = int(input("1. Продовжити\n2. Закінчити\n"))
            match action:
                case 1: pass
                case 2: 
                    fill = False
        return self

    def build(self):
        return self.book

# Білдер для наукових книжок
class ScientificBookBuilder(BookBuilder):
    def __init__(self):
        self.scientific_book = ScientificBook('Наукова')
        super().__init__(self.scientific_book)

    # Заповнення глосарію
    def fill_glosary(self):
        return self.fill_list(self.scientific_book.glosary, "Введіть термін та значення:\n")

    #Заповнення використаних джерел
    def fill_references(self):
        return self.fill_list(self.scientific_book.list_of_references, "Введіть використану літературу:\n")

# Білдер для балетрситики
class FictionBookBuilder(BookBuilder):
    def __init__(self):
        self.fiction_book = FictionBook('Балетристика')
        super().__init__(self.fiction_book)
    #Заповнення персонажів
    def fill_characters(self):
        return self.fill_list(self.fiction_book.character_list, "Введіть назву персонажа:\n")

    # Заповнення опису персонажа
    def fill_character_desc(self):
        return self.fill_list(self.fiction_book.character_desc, "Введіть опис персонажа:\n")

# Білдер для посібників
class NovelBookBuilder(BookBuilder):
    def __init__(self):
        self.manual_book = ManualBook('Посібник')
        super().__init__(self.manual_book)

    # Заповнення картинок
    def set_picture(self):
        return self.fill_list(self.manual_book.pictures, "Введіть посилання на картинки:\n")


#Регістр сторінок 
class PageRegister():
    _instance = None
    unique_pages=[]

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def add_page(self, page):
        changed_page = Page(page.page_text, uuid.uuid4())
        self.unique_pages.append(changed_page)

    def get_pages(self):
        for page in self.unique_pages:
            print(page)
    
#Клас генерації книжок
class BookGenerator():
    def create_book(self):
        self.book = None
        book_type = random.choice(book_info.book_types)
        author = random.choice(book_info.authors)
        title = random.choice(book_info.book_titles)

        match book_type:
            case 'Наукова': 
                scientific_book = ScientificBookBuilder()
                self.book = scientific_book
            case 'Балетристика': 
                fiction_book = FictionBookBuilder()
                self.book = fiction_book
            case 'Посібник': 
                manual_book = NovelBookBuilder()
                self.book = manual_book
        

        self.book = self.book.set_author(author).set_title(title).build()

        pages_num = random.randint(1, 15)
        page_register = PageRegister()

        for i in range(1, pages_num + 1):
            page_text = self.generate_page_text()
            page = Page(page_text, i)
            self.book.pages.append(page)
            page_register.add_page(page)

        return self.book

    def generate_page_text(self):
        text = ''
        paragraphs_num = random.randint(5, 10)
        for i in range(paragraphs_num):
            paragraph = ''
            sentences_num = random.randint(3, 10)
            for i in range(sentences_num):
                sentence = " ".join(random.choices(book_info.word_list, k=random.randint(5, 15)))
                paragraph+=sentence+'. '
            text+=paragraph+'\n\n'
        return text


# Генерація книги
generated_book = BookGenerator().create_book()
generated_book.show_pages()
print(generated_book)

# Створення наукової книги 
book = ScientificBookBuilder().set_author().set_title().set_page().fill_glosary().fill_references().build()
print(book)
book.show_pages()
book.show_references()
book.show_glosary()