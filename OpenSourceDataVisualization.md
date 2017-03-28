##### Department: Graphic Design

- Course: **Media Design**
- Year: 2016-2017, 2nd year
- Teacher: Dirk van Oosterbosch
- Semester: 2

### Assignment #4:
# Open Source Data Visualization

## Description

1. Watch 3 movies:
	- 1.1. Revolution OS (available on youtube)
	- 1.2. Everything is a Remix (5 part series)
	- 1.3. R.I.P. a Remix Manifesto
2. From these movies develop your own opinion, stance and vision on remixing, open source, copyrights and/or patents.
3. With this vision and these movies as inspiration, find a rich data source with:
	 - *points in time*
	 - *geographical locations*
	 - *network of connections* to illustrate your point.
4. Parse this data, filter it, mine it, scrape additional data, combine it and refine it, while documenting your process as open source on github.
5. Make a design that plots the data as a representational map of your story.
6. Iterate the poster three times.

![Diagram showing the process of scraping and visualizing](images/diagram_process_of_scraping_and_visualizing.png)
*Diagram showing the process of scraping and visualizing (from Visualizing Data, Ben Fry, O'Reilly 2008)*

#### Iterations

For every complex project, whether that is an interactive or static work, the final quality will greatly benefit from doing small iterations instead of attempting to do all in one final stretch. Especially in a project where data is researched, scraped and visualized, iterations will present the opportunity to reflect on the work and to refine, enrich and amend the data and the end result.

That is why for this assignment there are **three** iterations.

#### Working with data

- Do research. Find data sources.
- From the data develop your own opinion, vision and critical stance.
- To illustrate your point, select one or more rich data sources with either:
	 - points in time
	 - geographical locations
	 - network of connections
- Groom the data into one or more `.json` files, ready to be used:
	- Parse this data,
	- Filter it,
	- Mine it,
	- Scrape additional data,
	- Combine it and
	- Refine it,
- All of this, while documenting your process and results open source on github.

----

## Learning Goals

Acquire a fluency into working with big data research and creating information graphics. Articulate a vision about open source and copyright. Familiarize yourself with the process of creating a meaningful and readable map from structured data. Being able to independently create a concept, draft and multiple iterations of a research based map or poster. 

----

## Planning

### Week 1:
*March 28th 2017*

- Introduction to the **Open Source Data Visualization** assignment

**Homework:**

- Pick topic & Find data sources
- Investigate the data
- Make an analysis of its structure and properties

### Week 2:
*April 4th 2017*

- THEORY: Lecture: Scraping: dealing with variability in Wikipedia
	- [Lecture Notes](Lesson_09_Scraping_Notes.md), Video and [Code](ScrapingLecture/) (video is still being uploaded)

**Homework:**

- Scrape the data from the sources.
- Create and groom one or more `.json` files.
- Document the purpose, contents, structure, and attributes of your `.json` files.
- Make open source:
	- the source data (or link to live data)
	- your analysis of the data
	- your methods and tools to scrape and groom the data
	- the structured .json files

### Week 3:
*April 11th 2017*

- Present your data

- THEORY: Demonstration of some simple techniques to visualize the data: [Lesson: Graph Examples](ScrapingLecture/GraphExamples)

**Homework:**

- Parse the data
- Count the data
- Get a sense of what you collected
- Create a simple graph (histogram / bar chart / plot)

### Tokyo & May Holliday Weeks
*April 18th 2017*  
*April 25th 2017*

### Week 4:
*May 2nd 2017*

- Deadline of iteration 1:
- Present a first diagram

- THEORY: Analyzing your data (Python: map, reduce, filter)

**Homework:**

- What story can be told?
- Is that story specific for your data?
- Do you need additional data?
- Study different types of graps and describe which graph would convey which story
- Pick type of graph to tell this story best.

### Week 5:
*May 9th 2017*

- THEORY: [Lesson: Illustrator Scripting](Lesson_10_Illustrator_Scripting.md)

### Week 6:
*May 16th 2017*

- Deadline of iteration 2:
- Most meaningful graph for data

**Homework:**

- Does it work? (Does the graph tell the story?)
- How can it be improved?
- What do you need next? (Other graphs? / More graphs? / More data? )
- Pick your medium: poster? / 3D print? / movie? / interactive?

### Week 7:
*May 23rd 2017*


### Week 8:
*May 30th 2017*

- Deadline of iteration 3:
- Group presentation

**Homework:**

- Finalize the online Documentation on GitHub

### Week 9: **Evaluation**
*June 6th 2017*

- Evaluation & Grades

## Evaluation

Criteria for judging the work:
Process, Structure, Insight, Coding Skills, Persuasiveness and Relevance, Truthfulness, Open Source, Quantity of the Data (see below) and Communicating Quality of the Design and Presentation.

Finally, to make sure the poster is coded (and not drawn by hand), there is a formal criteria on the *quantity* of data. The data source and the poster should contain at least:

- over > 100 relations / links / connections,
- over > 250 locations on a map,
- over > 500 points in time,

**or** a combination of those.

----

### Examples of Data Visualization

##### Geographical Diagram
![Napolean and Hannibal](images/map_example_Napoleon_and_Hannibal.jpg)  
*Figurative Map of [...] marches by Hannibal and Napolean - Charles Joseph Minard (1861)*

----

##### Evolving data: differences over time
![Origin of Species - Ben Fry](images/map_example_Ben_Fry__Origin_of_Species.png)  
*Origin of Species - Ben Fry*

----

##### Evolving data: differences per file and per user
![Code commits visualized](images/map_example_code_swarm.png)  

----

##### Visualizing Statistics of Tourism
![Data of Piedmond, Italy](images/map_example_Piedmond.jpg)  

----

##### Charting Relations of Power
![They Rule, relations in a map](images/map_example_They_Rule.png)  
*They Rule*

----

##### Archeology and city expansion
![Dutch buildings by year of construction](images/map_example_amsterdam_building_by_year.png)
*Dutch buildings by year of construction([http://code.waag.org/buildings/](http://code.waag.org/buildings/))*

----

##Literature

#### Movies:

- Media For Thinking The Unthinkable
	 - Bret Victor [video talk & lecture notes](http://worrydream.com/#!/MediaForThinkingTheUnthinkable) (40 min, 2013)

#### Books:

- **The Visual Display of Quantitative Information**
	- *Edward R. Tufte* (Graphics Press, 1992)
- **Envisioning Information**
	- *Edward R. Tufte* (Graphics Press, 1990)
- **Beautiful Evidence**
	- *Edward R. Tufte* (Graphics Press, 2006)
- **Visual Explanations**: Images and Quantities, Evidence and Narrative
	- *Edward R. Tufte* (Graphics Press, 1997)
- **Now You See It**: Simple Visualization Techniques for Quantitative Analysis
	- *Stephen Few* (Analytics Press, 2009)
- **Show Me the Numbers**: Designing Tables and Graphs to Enlighten
	- *Stephen Few* (Analytics Press, 2012)
- **Form+Code** in Design, Art, and Architecture (Design Briefs)
	- *Casey Reas* (Princeton Architectural Press, 2010)
- **The Book of Trees**: Visualizing Branches of Knowledge
	- *Manuel Lima* (Princeton Architectural Press, 2014)
- **Visual Complexity**: Mapping Patterns of Information
	- *Manuel Lima* (Princeton Architectural Press, 2011)
- **Visualize This**: The FlowingData Guide to Design, Visualization, and Statistics
	- *Nathan Yau* (Wiley, 2011)
- **Visual Insights**: A Practical Guide to Making Sence  of Data
	- *Katy Bömer & David E. Polley* (MIT Press, 2014)
- **Beautiful Visualization**: Looking at Data through the Eyes of Experts (Theory in Practice)
	- *Julie Steele* (O'Reilly Media, 2010)
- **Data Flow**: Visualising Information in Graphic Design
	- Robert Klanten (Die Gestalten Verlag, 2008)
- **Data Flow 2**: Visualizing Information in Graphic Design
	- Robert Klanten (Die Gestalten Verlag, 2010)
- **Generative Design**: Visualize, Program, and Create with Processing
	- *Hartmut Bohnacker* (Princeton Architectural Press, 2012) 
- **Knowledge Is Beautiful**: Impossible Ideas, Invisible Patterns, Hidden Connections--Visualized
	- *David McCandless* (Harper Design, 2014)

#### Websites:
- Information Aesthetics
	- [infosthetics.com](http://infosthetics.com)
- Visual Complexity
	- [visualcomplexity.com](http://www.visualcomplexity.com/vc/)
- The Design of Information
	- [blog.threestory.com](http://blog.threestory.com)
	
#### Extra:	
- List of possible tools
	- [list of design tools](http://www.creativebloq.com/design-tools/data-visualization-712402)
