Web Scraper
===========
Some things I learned from this project:
- How to traverse the DOM using jQuery (and PyQuery, the Python equivalent)
- Basic Firebug skills
- How to use a virtual environment to avoid version conflicts between apps
- Regular expressions are a thing
- That my trusty old Macbook Pro isn't up to the task of modern web development, therefore:
- How to install and use Ubuntu

### 9/27/11
jQuery uses similar syntax to CSS, like . and # to specify HTML elements. (If you query just a word, it searches all tags?) You can then apply methods to whatever you've scraped - html() gives you the text, for example.

PyQuery tutorial: http://www.vertstudios.com/blog/pyquery-tutorial-basic-html-parsing-pyquery/

Tried installing PyQuery: "failed with error code 1
Storing complete log in /Users/rachelsakry/.pip/pip.log"

### 10/5
data() allows you to attach dictionary-style data to HTML elements - but it lives outside the HTML.
- getter: $object.data("key") - returns the associated value
- setter: $object.data("key", value)
- use $object.val() to get/set the value attr

attr() is falling out of use - replaced by prop() as of jQuery 1.6 which came out 3 months ago.

Firebug tip: button in lower right corner opens a multi-line editor.

NEXT: http://jqfundamentals.com/#chapter-6 - Add Tabbed Navigation (end of chap 5)

### 10/7
Basic jQuery according to Jeff: $(' ') - this is the selector. Here are some things you can put in it:
- div - all the divs
- div a - all the a's within divs
- .foo - class foo
- #foo - id foo
- #foo a - all the a's within the element with id foo
- div.bar a.foo - all the a's of class foo within divs of class bar

Instead of this: var $divs = $('div'), do this: var divs_dom_object = $('div')

To read in _JS: The Definitive Guide_: HTML attributes vs DOM properties

### 10/12
Went over jQFun tabs.js exercise with Chris. Review how his version solves the problem of how to associate the li with its div.

QUESTION: $.each() vs $('foo').each() - when to use which?

NEXT: back to PyQuery?

### 10/17
Need gcc-4.0 to install PyQuery

### 11/3
Tried installing PyQuery again w/ same result as before; noticed that the version of gcc it's using is for powerpc systems: WTF?
- Jeff suggested installing lxml instead?
- Chris suggested installing Homebrew: http://mxcl.github.com/homebrew/

I have Xcode version 3.2.6. 
Info about Xcode: http://guide.macports.org/chunked/installing.xcode.html

Installed Homebrew; tried using it to install pyquery; it said no formula exists for pyquery. Learned how to create a formula here: https://github.com/mxcl/homebrew/wiki/Formula-Cookbook

Went looking for a pyquery URL and found this instead: http://jbalogh.me/2009/03/24/pyquery/
Tried this tip; got the same fail message.

Jeff says: use Brew to install lxml and then maybe pip will be willing to install pyquery.

### 11/9
Tried using Brew to install lxml and got the same error message as with pyquery.
Tried using pip to install lxml and had the same problems as before.

Tried upgrading to Lion and couldn't because it requires at least a Core 2 Duo CPU and I have the previous generation, a Core Duo. This means I won't be able to upgrade to Xcode 4, because it requires Lion.

Jeff suggests: Running ubuntu in a virtualbox

NEXT: install ubuntu on li'l Dell? 
https://help.ubuntu.com/community/Installation/FromUSBStickQuick

### 11/11
virtualenv:
- "mkvirtualenv foo" creates foo in ~/.virtualenvs
- "workon foo" to activate
- "deactivate" (from within foo) to deactivate

IPython: a python shell with stuff like tab completion, and:
- foo = _ - assigns whatever the last result was.

To install a specific version of something: pip install django == 1.1.1 (or use >= for something at least as recent as.)

Every project should have a requirements.txt file. That way you can use "pip install -r requirements.txt" to get everything on the list that you don't already have.

"pip freeze" - lists all Python packages on the the system. 
- Add "-l" to list local packages only.
- "pip freeze -l > requirements.txt" will write the list to the txt file.

### 12/14 
Installed IPython

### 12/15 
Created virtualenv called webscraper. Tried to pip install PyQuery and it didn't work.

### 12/19 
apt: package manager for Debian. If pip isn't working, try apt. It may give you an outdated version, but the install will be easy.

apt installed PyQuery. It worked, whoo!

Jeff says: the webscraper should take three things: 
- the URL of the forum page
- the title (i.e. the question posed)
- the set of links posted in response to the question

and dump them into a DB (SQLite is fine).

### 1/8/12 
Did PyQuery tutorial 

### 1/9 
Modified testScrape.py so it only selects links from the div with class="post_body"

### 1/10
Jeff says: try getting the first 5 topics in a forum and for each of them return the topic title, each post title(?), and any links in the posts.

Installed Firebug

Forum topics are tr's in a table with id="forum_table"

So I have a list of topic links, and a for loop to pull the links from the posts on each topic, but what do I do with them? Stick them in some sort of data structure – an object?

### 1/12
The next step is to create a Django project to dump data into a DB; _then_ we'll process it and get rid of what we don't want.
- Installed Django
- Created project myDjangoWebscraper
- Created app webscraperApp

NEXT: Create "scrapeweb" management command w/ no args

### 1/17
- Wrote scrapeweb.py; ran it and got this error:
TypeError: handle_noargs() got an unexpected keyword argument 'pythonpath' 
- Created testCommand.py using functional code from Chris and got the same error.

### 1/31
- installed git
- ran pip freeze > requirements.txt

### 2/1
Use "self.stdout.write(foo)" to see the value of var foo.

###2/2
- created git repository
- changed class names to Topic and Link; added topicLink attr to Topic

### 2/5
TODO:
- edit model so link field is unique
- edit management command: TRY to add link to DB EXCEPT if you get a non-unique error

