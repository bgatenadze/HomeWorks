from collections import Counter
import re

with open('article.txt', 'r') as file:
    content = file.read()

words = re.findall(r'\b\w+\b', content.lower())

word_count = Counter(words)

second_most_common_word, count = word_count.most_common(2)[1]

print(f"The second most frequently repeated word is '{second_most_common_word}' with a count of {count}.")

