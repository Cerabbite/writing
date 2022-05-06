# writing
![writing](images/writing.png)  
<!--A converter for markdown files to a pdf for novels or screenplay-->

# Why use writing?

# Documentation
## Running the program
```
writing writing "Input File.md" Outputfile.pdf
```

## Settings
The settings section is where you put all information about your document. The information you put here includes style, author and title.<br>
You can start and end the settings section by putting three dashes in a row.
```
---
style: novel
title: Sample Title
author: Test Author
---
```
Style options:
- novel
- screenplay

## Chapters
You can start a new chapter with a ```#``` and then put the name of the chapter after it like so ```# Sample Title```. This will create a new chapter on a new page.

## Content
The content of a chapter can be put after ```# Sample Title``` on a new line like so 
```# Sample Title
Sample Content```

## Good to know
Be sure to have an empty line after your last line of text in your document otherwise the last line will NOT be included in the document.
