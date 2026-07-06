# urdu-ocr-codesaviours-si26-noorulaein-fatima-
# Urdu OCR Project

## Project Description
This project is focused on collecting and organizing Urdu text images for OCR model development.

## Dataset Structure
- Newspaper images
- Books images
- Signboard images
- Synthetic images
- Other images

## Week 1 Tasks Completed
- Created dataset folders
- Collected and organized images
- Created labels.csv
Research Task: Understanding Urdu OCR

 1. What is OCR (Optical Character Recognition)?
OCR is a technology that changes text in images, scanned papers, or PDFs into editable digital text.
It reads letters and words from an image and converts them into computer text.
OCR helps save time and is used for digitizing books, documents, and forms.

2. Why is Urdu OCR harder than English OCR?
Urdu OCR is difficult because Urdu uses a cursive writing style called Nastaliq.
Urdu letters change their shape according to their position in a word and are written from right to left.
Many letters join together, which makes it hard for OCR to recognize them correctly.

3. Two Real-World Situations Where Urdu OCR Would Be Useful
 a. Digitizing Historical and Legal Archives:
Urdu OCR can help convert old books, historical records, and legal documents into digital form.
This makes them easier to search, store, and protect from damage.
Researchers and students can access them quickly.

 b. Digitizing Educational Materials and Books:
Translating printed Urdu textbooks, poetry collections, and academic papers into digital formats allows for better distribution and accessibility.
OCR technology makes it possible to extract and format large quantities of Urdu literature for e-readers and online libraries

Why We Need a Better Model?
Tesseract fails on Urdu because Urdu is a right-to-left language where letters 
are connected and can change shape depending on their position in a word. From the results above,
Tesseract missed some words, recognized some characters incorrectly, and
in some cases produced incomplete text or random symbols
Some outputs were partially correct, but many words were not recognized properly.
This shows that Urdu text is more difficult for Tesseract to process because of different fonts,
image quality issues, and the complex writing style of the language.

