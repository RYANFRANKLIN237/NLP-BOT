import PyPDF2,pyttsx3
#importing the modules 

#path of the pdf file

path = open('AI Quick Guide.pdf', 'rb')

#creating the PdfFilereader object

pdfReader = PyPDF2.PdfFileReader(path)

#the page with which you want to start
#this will read the 9th page
from_page = pdfReader.getPage(8)

#extracting the text from the pdf 
text = from_page.extract_text()

#reading the text
speak = pyttsx3.init()

speak.say(text)
speak.runAndWait()

   