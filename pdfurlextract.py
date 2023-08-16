import re
import PyPDF2
import sys

def extract_urls_from_pdf(pdf_path):
    urls = []
    
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            page_text = page.extractText()
            
            url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            page_urls = re.findall(url_pattern, page_text)
            
            urls.extend(page_urls)
    
    return urls

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <pdf_file_path>")
    else:
        pdf_path = sys.argv[1]
        extracted_urls = extract_urls_from_pdf(pdf_path)
        
        if extracted_urls:
            for url in extracted_urls:
                print(url)
        else:
            print("No URLs found in the PDF.")
