import PyPDF2

with open('cover_letter.pdf', 'rb') as f:

    pdf_reader = PyPDF2.PdfReader(f)

    text = ''
    for i in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[i]
        text += page.extract_text()
print(text)
