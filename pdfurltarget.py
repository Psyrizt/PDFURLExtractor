import fitz  # PyMuPDF
import sys

def extract_hyperlink_urls(pdf_path):
    urls = []
    
    pdf_document = fitz.open(pdf_path)
    
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        annotations = page.annots()
        
        for annotation in annotations:
            if annotation.get('subtype') == 'Link':
                url = annotation.get('uri')
                if url:
                    urls.append(url)
    
    pdf_document.close()
    return urls

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <pdf_file_path>")
    else:
        pdf_path = sys.argv[1]
        extracted_urls = extract_hyperlink_urls(pdf_path)
        
        if extracted_urls:
            print("Extracted Hyperlink URLs:")
            for url in extracted_urls:
                print(url)
        else:
            print("No hyperlink URLs found in the PDF.")
