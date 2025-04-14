# Sharvil-AI-Powered-Personalized-Newsletter-Generator

An intelligent and automated pipeline for generating personalized newsletters from RSS feeds. The system fetches articles, classifies them, matches them to user interests and preferred sources, and generates both markdown and PDF newsletters.

###### **💡 Project Overview**
- This project automates the process of:
- Fetching articles from configured RSS feeds.
- Classifying articles into categories using keyword-based logic.
- Matching articles to users based on their interests and preferred sources.
- Generating clean, structured markdown newsletters.
- Converting markdown files into professional-looking PDF newsletters.

###### **TO VIEW THE OUPUT:**
- Follow the path: output -->  pdf
- The "pdf" folder contains the newsletters generated in the pdf file format for each User!

###### **📁 Directory Structure:**
```
AI Newsletter Generator/
├── src/
│   ├── fetcher.py
│   ├── classifier.py
│   ├── matcher.py
│   ├── summarizer.py
│   ├── newsletter_generator.py
│   ├── pdf_generator.py
│   └── main.py
├── users/
│   └── user_profiles.json
├── output/
│   ├── (generated .md newsletters)
│   └── pdf/
│       └── (converted .pdf newsletters)
├── requirements.txt
└── README.md
```
###### **⚙️ Setup**
1) Install dependencies:
   pip install -r requirements.txt

2) Install wkhtmltopdf from:
   https://wkhtmltopdf.org/

**Update its path in converter.py:**
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

###### **🧑‍💼 User Profiles:**
All user preferences are saved in users/user_profiles.json.

###### **🚀 How to Run:**
**Run the program from the terminal:**
python main.py

**The system will:**
- Ask for your name.
- Fetch, filter, and generate a markdown newsletter in /output.
- Convert the markdown to PDF in /output/pdf.

###### **📰 Newsletter Output includes:**
- A highlights section (top 3 recent articles).
- Categorized articles based on their content.
- Enhanced summaries.
- Clean markdown layout, converted into PDF with consistent styling.

###### **⚠️ Notes**
The system will only select articles that match both user interests and preferred sources.
If no matching articles are found, a placeholder message will be written to the newsletter.
