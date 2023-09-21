"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def summarize(self):
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def summarize(self):
        num_of_words = len(self.text.split())
        return super().summarize() + f', total number of words in the text: {num_of_words}'


if __name__ == '__main__':
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, ' \
           'sed do eiusmod tempor incididunt ut labore et ' \
           'dolore magna aliqua. '
    text_processor = TextProcessor(text=text)
    print(f'TextProcessor:'
          f'\n {text_processor.to_upper()}'
          f'\n {text_processor.summarize()}')

    advanced_text_processor = AdvancedTextProcessor(text=text)
    print(f'\nAdvancedTextProcessor:'
          f'\n {advanced_text_processor.to_upper()}'
          f'\n {advanced_text_processor.summarize()}')
