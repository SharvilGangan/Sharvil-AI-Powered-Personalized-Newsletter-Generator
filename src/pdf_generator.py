import os
import re
from pathlib import Path
import markdown
import pdfkit
from bs4 import BeautifulSoup

def clean_and_generate_pdf(input_dir, output_dir):
    """
    Process all markdown files in the input directory:
    1. Remove unwanted text like "Sure, here is the summary:"
    2. Convert clean markdown to PDF
    3. Save in the output directory
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all markdown files
    md_files = list(Path(input_dir).glob('*.md'))
    
    if not md_files:
        print(f"No markdown files found in {input_dir}")
        return
    
    print(f"Found {len(md_files)} markdown files to process")
    
    # Path to wkhtmltopdf executable (replace with your actual path)
    path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    
    # Configure pdfkit with the path to wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    
    for md_file in md_files:
        file_name = md_file.stem
        print(f"Processing {file_name}...")
        
        # Read markdown content
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove unwanted text patterns
        clean_content = re.sub(r'Sure, here is the summary:\s*', '', content)
        
        # Save cleaned markdown
        clean_md_path = os.path.join(output_dir, f"{file_name}_clean.md")
        with open(clean_md_path, 'w', encoding='utf-8') as f:
            f.write(clean_content)
        
        # Convert to HTML first (for better styling)
        html_content = markdown.markdown(clean_content)
        
        # Add basic styling
        styled_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ 
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    margin: 40px;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                h1 {{ color: #2c3e50; }}
                h2 {{ color: #3498db; margin-top: 30px; }}
                blockquote {{
                    border-left: 4px solid #ccc;
                    margin-left: 0;
                    padding-left: 16px;
                    color: #555;
                }}
                a {{ color: #2980b9; text-decoration: none; }}
                hr {{ border: 1px solid #eee; margin: 30px 0; }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Save the HTML file
        html_path = os.path.join(output_dir, f"{file_name}.html")
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(styled_html)
        
        # Convert HTML to PDF
        pdf_path = os.path.join(output_dir, f"{file_name}.pdf")
        try:
            # Use pdfkit with the specified configuration
            pdfkit.from_file(html_path, pdf_path, configuration=config)
            print(f"✅ Generated PDF: {pdf_path}")
        except Exception as e:
            print(f"❌ Error generating PDF: {e}")
            print("Make sure wkhtmltopdf is installed on your system.")

if __name__ == "__main__":
    input_directory = r"D:\AI Newsletter Generator\output"
    output_directory = r"D:\AI Newsletter Generator\output\pdf"
    
    clean_and_generate_pdf(input_directory, output_directory)
