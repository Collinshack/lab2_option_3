import csv
import random
import xml.dom.minidom as minidom 


# 1. Записи, у которых поле «Название» длиннее 30 символов.

with open('books-en.csv', 'r') as books_data:
    data = csv.reader(books_data, delimiter=';')
    for data in list(data):
        if len(data[1]) > 30:
            print(data[1], '---', len(data[1]), 'символы')


        
# 2. Поиск книг по автору
flag = 0
search = input('search for: ')

years_to_search = ['2014', '2016', '2017']

with open('books-en.csv', 'r') as books_data:
    data = csv.reader(books_data, delimiter=';')

    for row in data:
        year_of_publication = row[3]
        if year_of_publication in years_to_search:
            author_column = row[2].lower()
            search_file = author_column.find(search.lower())
            if search_file != -1:
                print(row[2])
                flag = 1

if flag == 0:
    print('Nothing found!')





# 3. Библиографическая ссылка Генератор
with open('books-en.csv', 'r') as books_data:
    data = list(csv.reader(books_data, delimiter=';'))


random_entries = random.sample(data[1:], 20)  

references = []
for i, entry in enumerate(random_entries, start=1):
    author = entry[2]
    title = entry[1]
    year = entry[3]
    reference = f"{author}. {title} - {year}"
    references.append(reference)

with open('bibliography.txt', 'w') as outfile:
    for i, reference in enumerate(references, start=1):
        outfile.write(f"{i}. {reference}\n")

print("Bibliographic references have been generated and saved to 'bibliography.txt'.")



# 4. Извлечение «Charcodes» для валют с Nominal=1

with open('currency.xml', 'r') as currency_file:
    file = currency_file.read()
    dom = minidom.parseString(file)
    charcodes = dom.getElementsByTagName('CharCode')
    nominals = dom.getElementsByTagName('Nominal')
    for charcode_element, nominal_element in zip(charcodes, nominals):
        nominal_value = int(nominal_element.firstChild.nodeValue)
        if nominal_value == 1:
            print(charcode_element.firstChild.nodeValue)



# 5. Все теги без повторов
with open('currency.xml', 'r') as currency_file:
    file = currency_file.read()
    dom = minidom.parseString(file)

    elements = dom.getElementsByTagName('*')
    unique_tags = set()
    for element in elements:
        unique_tags.add(element.tagName)
    for tag in unique_tags:
        print(tag)


# 6. Все издательства без повторов
unique_publishers = set()
with open('books-en.csv', 'r') as books_data:
    data = list(csv.reader(books_data, delimiter=';'))
    for row in data:
        publishers = row[4]
        publisher_list = publishers.split(',')
        for publisher in publisher_list:
            unique_publishers.add(publisher.strip())  
for publisher in unique_publishers:
    print(publisher)
    

# 7. 20 лучших книг
books = []
with open('books-en.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    next(reader)
    for row in reader:
        books.append(row)
sorted_books = sorted(books, key=lambda x: int(x['Downloads']), reverse=True)

top_20_books = sorted_books[:20]
for book in top_20_books:
    print(book)








