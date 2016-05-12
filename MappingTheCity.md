#####Department: Graphic Design

- Course: **Media Design**
- Year: 2015-2016, 2nd year
- Teacher: Dirk van Oosterbosch
- Semester: 2

###Assignment #4:
#Mapping the City

##### [Shared Data Repository: MappingTheCity-Data](https://github.com/ArtezGDA/MappingTheCity-Data)
##### [Design Work Repository: MappingTheCity-Maps](https://github.com/ArtezGDA/MappingTheCity-Maps)

## Introduction

For decades there is a global shift going of people moving from rural to urban areas. The same can be said of (digital) information. Cities are a concentration of vast quantaties of ever increasing data. This assigment is about getting a grasp on these vast amounts of data, and being able to use this data to perform research and to tell meaningfull stories and demonstrate analytical insights.

##Description

![Diagram showing the process of scraping and visualizing](images/diagram_process_of_scraping_and_visualizing.png)
*Diagram showing the process of scraping and visualizing (from Visualizing Data, Ben Fry, O'Reilly 2008)*

#### Iterations

For every complex project, whether that is an interactive or static work, the final quality will greatly benefit from doing small iterations instead of attempting to do all in one final stretch. Especially in a project where data is researched, scraped and visualized, iterations will present the opportunity to reflect on the work and to refine, enrich and amend the data and the end result.

That is why for this assignment we will do **three** iterations of a poster.

#### Two-part assignment

The assignment is a two part assignment:

- Collaborative Group assigment:
	- Group of maximum 3 people (team up coders with non-coders)
	- Collection and Grooming of the data
	- Store in [Shared Data Repository](https://github.com/ArtezGDA/MappingTheCity-Data)
- Individual assignment:
	- Constructing your own story and designing the poster
	- Store in [Design Work Repository](https://github.com/ArtezGDA/MappingTheCity-Maps)

#### Getting the data

- Do research. Find data sources. 
- From the data develop your own opinion, stance and vision on cities, agglomerations and urbanization.
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

#### Telling the story

- Design a poster that plots out the data as representational map of your story.
- Iterate the poster three times.

----
## Learning Goals

Acquire a fluency into working with big data research and creating information graphics. Articulate a vision or insight about cities and urbanization. Familiarize yourself with the process of creating a meaningful and readable map from structured data. Being able to independently create a concept, draft and multiple iterations of a research based map or poster.

----
## Planning

The complete planning of the next 11 weeks is not final yet, but we will go over these topics:

- Data formats for storing research data: csv, xml, **json**, database
- Python: database (sqlite) & SQL
- Javascript: TileMill / MapBox / Modest Maps
- Javascript: Illustrator Scripting
- Extra tools as inspiration:
	- Graphiz & dot
	- D3.js

####Week 1:
*March 24th 2016*

- Introduction to the **Mapping the City** assignment
- Formation of teams for the collaborative part of the assignment

**Homework:**

- Pick topic & Find data sources
- Team work to research and select the best data sources
- Investigate the data
- Make an analysis of its structure and properties

####Week 2:
*March 31st 2016*

- Lecture: Scraping: dealing with variability in Wikipedia
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

####Week 3:
*April 7th 2016*

- Plenary Discussion about the found data
- Collaborative organization and categorization of the data

**Homework:**

- Finish homework of last week!

####Week 4:
*April 14th 2016*

- Group evalutation of the data scraping part of the assignment
- Demonstration of some simple techniques to visualize the data: [Lesson: Graph Examples](ScrapingLecture/GraphExamples)

**Homework:**

- Create the first iteration of the poster

####Week 5:
*April 21st 2016*

- Group presentation of the **first iteration** of the poster
- Different types of graphs
- Analyzing your data (Python: map, reduce, filter)

**Homework:**

- Study different types of graps and describe which graph would convey which story
- Watch Bret Victor's talk

####Week 6:
*April 28th 2016*

Lesson cancelled

**Homework:**

- Finalizing the second iteration of the poster

#### Ascension Day

####Week 7:
*May 12th 2016*

- Group presentation of the **second iteration** of the poster
- Group talks

**Homework:**

- Work on the poster

####Week 8:
*May 19th 2016*

- Illustrator Scripting

**Homework:**

- Work on the poster

####Week 9:
*May 26th 2016*

- ...

**Homework:**

- Create the final iteration of the poster

####Week 10:
*June 2nd 2016*

- Group Presentation of the **third iteration** of the poster (and bring previous iterations)
- Celebrations

**Homework:**

- Finalize the online Documentation on GitHub

####Week 11:
*June 9th 2016*

- Evaluation

##Evaluation

Criteria for judging the work:
Process, Structure, Insight, Coding Skills, Persuasiveness and Relevance, Truthfulness, Open Source, Quantity of the Data (see below) and Communicating Quality of the Design and Presentation.

Finally, to make sure the poster is coded (and not drawn by hand), there is a formal criteria on the *quantity* of data. The data source and the poster should contain at least:

- over > 100 relations / links / connections,
- over > 250 locations on a map,
- over > 500 points in time,

**or** a combination of those.

----

### Examples of Data Visualization Maps

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
