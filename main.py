
import PyPDF2, urllib.request, nltk, textract
from io import BytesIO
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from PyPDF2 import PdfReader



reader = urllib.request.urlopen('https://udri.org/pdf/02%20working%20paper%201.pdf')
bytes_stream = BytesIO(reader.read())

reader = PdfReader(bytes_stream)
page = reader.pages[0]
print("my doc is all about ",page.extract_text())

pageobj = reader.pages[1]
page2 = pageobj.extract_text()

punctuations = ['.', '(', ')', ';', ':', '[', ']', ',', '...']
tokens = word_tokenize(page2)
print(tokens)
stop_words = stopwords.words('english')

name_list = list()
check = ['Mr.', 'Mrs.', 'Ms.']
for idx, token, in enumerate (tokens):
    if token.startswith(tuple(check)) and idx < (len(tokens) - 1) : 
        name = token + tokens[idx + 1] + ' ' + tokens[idx + 2]
        name_list.append(name)

print(name_list)



