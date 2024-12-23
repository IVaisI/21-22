import random
import re
import string
import time
import tracemalloc
start_time = time.time()

class TextProcessor:
    def __init__(self):
        self.message = ""

    def input_text(self):
        print("Введите текст для обработки (для завершения ввода нажмите клавишу Enter): ")
        text = []
        while True:
            line = input()
            if line == "":
                break
            text.append(line)
        self.message = "\n".join(text)
        return self.message

    def random_text(self):
        letters = string.ascii_letters + ' ' * 7
        length = random.randint(20, 100)  # Генерация случайной длины
        self.message = ''.join(random.choice(letters) for _ in range(length))
        return self.message

    def count_words(self):
        text = self.message.lower()
        words = re.findall(r'\b\w+\b', text)
        return len(words)

    def print_text(self):
        print(f"Введенный текст:\n{self.message}")

class Menu:
    def __init__(self):
        self.text_processor = TextProcessor()
        self.result = None
        self.text_input = False

    def is_int(self, choice):
        return choice.isdigit()

    def f1(self):
        print("Выберите тип ввода:\n1. Ввод текста с клавиатуры\n2. Случайная генерация")
        type_choice = input()

        if self.is_int(type_choice):
            type_choice = int(type_choice)
            if type_choice == 1:
                self.text_processor.input_text()
                print(f"Вы ввели следующий текст: {self.text_processor.message} ")
            elif type_choice == 2:
                self.text_processor.random_text()
                print(f"Сгенерированный текст: {self.text_processor.message}")
            else:
                print('Ошибка: неверный выбор')
        else:
            print('Ошибка: введите число')
        self.text_input = True

    def f2(self):
        if self.text_input:
            self.result = self.text_processor.count_words()
            print("Алгоритм выполнен\n")
        else:
            print("Ошибка!\nСначала введите текст\n\n")

    def f3(self):
        if self.text_input and self.result is not None:
            print(f"Количество слов в тексте: {self.result}")
        else:
            print("Ошибка!\nСначала выполните алгоритм подсчета слов\n\n")

    def print_text(self):
        if self.text_input:
            self.text_processor.print_text()
        else:
            print("Ошибка!\nСначала введите текст\n\n")

    def run(self):
        while True:
            print("Выберите пункт меню:\n"
                  "1. Ввод исходного текста \n"
                  "2. Выполнение алгоритма подсчета количества слов в тексте\n"
                  "3. Вывод результата\n"
                  "4. Вывод текста\n"
                  "5. Выход из цикла")
            choice = input()
            if self.is_int(choice):
                choice = int(choice)

                if choice == 1:
                    self.f1()
                elif choice == 2:
                    self.f2()
                elif choice == 3:
                    self.f3()
                elif choice == 4:
                    self.print_text()
                elif choice == 5:
                    break
                else:
                    print('Ошибка: неверный выбор')
            else:
                print('Ошибка: введите число')

if __name__ == "__main__":
    menu = Menu()
    menu.run()
"""1.Оптимизация ввода текста: Вместо использования цикла для ввода текста, можно использовать метод input с параметром end для завершения ввода.
2.Упрощение проверки на целое число: Метод is_int можно упростить, используя встроенную функцию isdigit.
3.Улучшение генерации случайного текста: Можно использовать библиотеку string для генерации случайного текста.
4.Улучшение подсчета слов: Можно использовать библиотеку re для более эффективного подсчета слов.
5.Улучшение структуры кода: Разделить код на более мелкие функции для повышения читаемости и поддержки.
"""
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 memory consumers ]")
for stat in top_stats[:10]:
    print(stat)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Время выполнения программы: {elapsed_time} секунд")