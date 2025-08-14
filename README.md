#Wiki

## Intro

This is the Project 1 from **CS50's Web Programming with Python and JavaScript**.  
Instructors: Brian Yu and David J. Malan

### Summary

The goal of this activity is to recreate an encyclopedia as the wikipedia page, applying the knowledge acquired from the first few classes on HTML, CSS styling, Django and python.

### Specifications

#### Entry Page
- [x] Visiting /wiki/TITLE should display the contents of the encyclopedia entry with that title.
- [x] If the entry exists, display its Markdown content converted to HTML.
- [x] If the entry does not exist, show an error page indicating the page was not found.
- [x] The page title should include the entry’s name.
#### Index Page
- [x] On index.html, list all encyclopedia entries as clickable links.
- [x] Clicking an entry should open its respective entry page.
#### Search Functionality
- [x] Users can search via the sidebar search box.
- [x] If the query matches an entry title exactly, redirect to that entry page.
- [x] If the query is a substring of any entry title, display a search results page listing all matching entries.
- [x] Clicking any result should open the respective entry page.
#### New Page Creation
- [x] Clicking "Create New Page" opens a form to add a new entry.
- [x] Form includes: Title field; Textarea for Markdown content
- [x] On save: 
- [x] If an entry with the given title already exists → show an error message.
- [x] Otherwise, save the entry and redirect to its page.
#### Edit Page
- [ ] Each entry page has an "Edit" link.
- [ ] Editing form is pre-filled with the current Markdown content.
- [ ] On save, update the entry and redirect to its page.
#### Random Page
- [x] Clicking "Random Page" opens a random encyclopedia entry.
#### Markdown Conversion
- [ ] Convert Markdown to HTML before displaying entries.
- [ ] May use markdown2 or implement custom parsing (headings, bold, unordered lists, links, paragraphs).
### Links

- [🔗 Project Specification](https://cs50.harvard.edu/web/projects/1/wiki/)  


### Author
Rafael Mourato (Rafael.mourato@hotmail.com) - Student of Informational Systems at Federal University of Pernambuco.

### License
This project is for educational purposes only and is not affiliated with Wikipedia.
