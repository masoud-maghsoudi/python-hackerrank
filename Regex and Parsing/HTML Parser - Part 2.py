import re
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if (re.search(r"\n|\r", comment)):
            print(">>> Multi-line Comment", comment, sep="\n")
        else:
            print(">>> Single-line Comment", comment, sep="\n")
    def handle_data(self, data): 
        if not (re.search(r"\n|\r", data)):
            print(">>> Data", data, sep="\n")
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()