## It is to check if the judgments contain headnote or not
## If the judgment contains headnote then it will not be included in the final dataset

import PyPDF2
import re

# we have to add try catch so that if there is no file then it will not stop running
def extract_text_from_pdf(pdf_path):
    text = ""
    flag=0
    
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            r=page.extract_text()
            lines = r.split('\n')
            for i in range(len(lines)-1):
                line = lines[i].strip()
                next_line = lines[i + 1].strip()

                # does not contain "Headnote", and next line is empty
                if ("Headnotes" in line) and (next_line == 'JUDGMENT:'):
                    return text,0
                if ("Headnotes" in line):
                    flag=1
                # Check if line does not start with an integer or "https",
                if (not re.match(r'^\d|https', line)) :
                    text += line + '\n'
    return text,flag
li=[]


for i in range(1,12855):
    pdf_text,flag = extract_text_from_pdf(str(i)+".pdf")
    if(flag==0):
        li.append(i)

#list of pdfs which do not contain headnote
print(li)