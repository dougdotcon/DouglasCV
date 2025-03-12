import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

if __name__ == "__main__":
    pdf_path = "Profile.pdf"
    text = extract_text_from_pdf(pdf_path)
    print(text)
    
    # Salvar o texto em um arquivo
    with open("profile_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    
    print("Texto extraído e salvo em 'profile_text.txt'") 