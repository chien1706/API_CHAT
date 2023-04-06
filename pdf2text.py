import PyPDF2

# Open the PDF file in read-binary mode
with open('cover_letter.pdf', 'rb') as pdf_file:

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Get the number of pages in the PDF file
    num_pages = pdf_reader.getNumPages()

    # Create a new text file to write the converted text to
    with open('file.txt', 'w', encoding="utf-8") as text_file:

        # Loop through each page in the PDF file
        for page in range(num_pages):

            # Get the text contents of the current page
            page_contents = pdf_reader.getPage(page).extractText()
            print(page_contents)
            # Write the page contents to the text file
            text_file.write(page_contents)
