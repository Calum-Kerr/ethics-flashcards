import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""

        # Get the number of pages
        num_pages = len(pdf_reader.pages)
        print(f"Total pages: {num_pages}")

        # Extract text from each page
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += f"\n\n--- Page {page_num + 1} ---\n\n"
            text += page.extract_text()

        return text

if __name__ == "__main__":
    pdf_path = "CCS Lecture 1 Ethics and Computer Ethics.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)

    # Save the extracted text to a file
    with open("ethics_pdf_content.txt", "w", encoding="utf-8") as text_file:
        text_file.write(extracted_text)

    print("Text extraction complete. Saved to ethics_pdf_content.txt")
