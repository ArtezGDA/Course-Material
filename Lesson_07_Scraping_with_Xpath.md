# Scraping with Xpath and Google Spreadsheets

####Some prerequisites:

- Use Google Chrome
- Install the **XPather** extension in Google Chrome

### Step 1: Choose a page from which you want to scrape

Unfortunalely, Chrome will crash if you try this on a page with 5000 links. So we need to find a simpler page to demonstrate this technique as example: https://en.wikipedia.org/wiki/List_of_Walt_Disney_Animation_Studios_films

### Step 2: Inspect the element you want to scrape

Use the **Developer Tools Inspector** (cmd + alt + i) (from the View Menu, -> Developer -> Developer Tools).

The inspector lets you see the `HTML` code responsible for the page. It also lets you select HTML, and then highlight the corresponding element in the browser.  
Vice versa, it can also do the reverse: choose the selection tool: the top-left icon in the top row of the Developer Tools. (In the most recent version the icon looks like a pointer inside a box, in previous versions this was a magnifying glass). Then hover over any element in the browser and the corresponding code will light up. Click on an element in the browser and the corresponding code will be selected.

If we try that with the url above, we find that the titles of the movies all have this path:

![Web Inspector showing the path to the title of a Disney movie](images/disney_path_of_titles.png)

### Step 3: Analyse which parts of the path to this element is unique and which is common for all elements you want to scrape

... to be continued

