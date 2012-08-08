12/14 Installed IPython
12/15 Created virtualenv called webscraper. Tried to pip install pyQuery and it didn't work.
12/19 apt installed pyQuery

1/8 Did PyQuery tutorial 

1/9 Modified testScrape.py so it only selects links from the div with class=”post_body”

1/10
Jeff says: try getting the first 5 topics in a forum and for each of them return the topic title, each post title(?), and any links in the posts.

Installed Firebug
Forum topics are <tr>s in a table with id=”forum_table”
So I have a list of topic links, and a for loop to pull the links from the posts on each topic, but what do I do with them? Stick them in some sort of data structure – an object?

1/12
Installed Django
Created project myDjangoWebscraper
Created app webscraperApp
Created scrapeweb.py command (but didn't put anything in it)

1/17
Wrote scrapeweb.py; ran it and got this error:
TypeError: handle_noargs() got an unexpected keyword argument 'pythonpath' 
Created testCommand.py using functional code from Chris and got the same error.

1/31
installed git
ran pip freeze > requirements.txt

2/2
created git repository
changed class names to Topic and Link; added topicLink attr to Topic

