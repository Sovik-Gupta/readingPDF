'''
    PyPDF2 is a python library built as pdf toolkit.
    Textract is a core function for extracting text.
    NLTK stands for natural language toolkit .

'''

import PyPDF2, urllib.request, nltk, textract
from io import BytesIO
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from PyPDF2 import PdfReader

# we fetch the pdf from the given url using urllib.request
reader = urllib.request.urlopen('https://udri.org/pdf/02%20working%20paper%201.pdf')
bytes_stream = BytesIO(reader.read())

# create an object of PdfFileReader class of PyPDF2 module 
reader = PdfReader(bytes_stream)
page = reader.pages[0]
# print("my doc is all about ",page.extract_text())  # Logging

pageobj = reader.pages[1]
page2 = pageobj.extract_text()

# perform tokenization and remove the punctuations and stopwords from the data
punctuations = ['.', '(', ')', ';', ':', '[', ']', ',', '...']
tokens = word_tokenize(page2)
# print(tokens) # Logging
stop_words = stopwords.words('english')

name_list = list()
check = ['Mr.', 'Mrs.', 'Ms.']
# extract the full names
for idx, token, in enumerate (tokens):
    if token.startswith(tuple(check)) and idx < (len(tokens) - 1) : 
        name = token + tokens[idx + 1] + ' ' + tokens[idx + 2]
        name_list.append(name)

# print the names and close the file
print(name_list)
reader.close()



