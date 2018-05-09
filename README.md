# box_of_rain

Available publicly at: [sebscho.pythonanywhere.com](sebscho.pythonanywhere.com)

## Project description/ motivation
In the 1970s, my dad operated a radio station out of his home and owned three record (and waterbed) stores in Spokane, Washington. Thousands of records ended up in our basement. [‘Box of Rain’](http://www.sebscho.com/boxofrain) is a project about music, design and family as my brother and I attempt to catalogue my dad's vinyl collection. 

This visualization displays blues artists' relationships, clustered by both location and collaborations. Each colored node is an individual blues artist. The colors correspond to their primary instrument, after vocals. The data was manually compiled based on records I’ve catalogued so far, and the connections stem from anecdotes from dad. Questions this vis is trying to solve are: 

* How are different genres related to the blues? 
* How are relationships between artists in this collection clustered geographically? 
* Where are different instruments within clusters, and what is the distribution of instruments at key nodes? 

The center cluster is full of Delta Blues Singers, artists from the south like BB King. Connected to BB by Robert Johnson are the Chicago Blues men, including Muddy Waters and Howlin’ Wolf. This cluster collaborated with Paul Butterfield, who is perhaps best known for playing with John Mayall and Eric Clapton. This cluster leans more towards rock and roll. On the other side of the Delta Blues Cluster, Eddie “Cleanhead” Vinson connects a jazz cluster. Finally, a “bad ass women” cluster also connects to the Delta Blues Singers at with Big Mama Thorton, a fellow Texan to Albert King. 

**Interactions and interpretation:** On hover, the name of each node appears. On click in legend, the colors are highlighted, which shows the viewer the importance and popularity of certain instruments, and the variety of instruments and individuals that draw the most connectivity. I chose a force-directed diagram because I wanted to emphasize the connections and relationships between individuals, more than the individual names themselves. 


#### other resources in this repo
* web scrape for exploration: scraping "associated acts" from wikipedia to compile initial dataset (I ended up going with a personal dataset instead)

