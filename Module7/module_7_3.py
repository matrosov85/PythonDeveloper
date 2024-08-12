# Домашнее задание по теме "Оператор "with"

class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                text = file.read().replace('\n', ' ').lower()
                for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ', ' — ']:
                    if punctuation in text:
                        text = text.replace(punctuation, ' ')
                all_words.update({file_name: text.split()})
        return all_words

    def find(self, word):
        return {file_name: words.index(word.lower())+1 for file_name, words in self.get_all_words().items()}

    def count(self, word):
        return {file_name: words.count(word.lower()) for file_name, words in self.get_all_words().items()}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
