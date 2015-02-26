# Geog2021_Coursework

## Coursework notes for Geog 2021

### Accessing the notes via a web page

These coursenotes are available as web pages (html) from the [Geog 2021 course overview page](http://www2.geog.ucl.ac.uk/~plewis/geog2021) or more directly from the [practical introduction page](http://www2.geog.ucl.ac.uk/~plewis/Geog2021_Coursework/CW-1-Pearl-River-Intro.html).

### Accessing the notes via github

The notes are also available on [github](https://github.com/profLewis/Geog2021_Coursework). You can directly download the notes from [github](https://github.com/profLewis/Geog2021_Coursework), either using some [`git`](http://en.wikipedia.org/wiki/Git_(software)) software, e.g:


`bash% git clone https://github.com/profLewis/Geog2021_Coursework.git`

or by downloading the [course notes as a zip file](https://github.com/profLewis/Geog2021_Coursework/archive/master.zip).

If you use `git`, you can apply any updates to the notes:

`bash% cd where_I_put_the_notes/Geog2021_Coursework`

`bash% git reset --hard HEAD`

`bash% git pull`

You can also fork the notes and create your own version.

## Using the notes for Geog 2021

You can of course just read and digest the html notes, but you will find that there are snippets of computer code (in Python) at times. Note that you **do not** need to use the Python codes to do this coursework: you can do everything you need in ENVI and Excel. That said, you will be processing quite a number of images, and you may find the Python codes useful for at least semi-automating the tasks.

### Running ipython to use the notes for Geog 2021

Assuming you are on a unix system (including OS X, linux etc.), then first change directory to where the notes are:

`bash% cd where_I_put_the_notes/Geog2021_Coursework`

Then start an [`ipython`] session:

`bash% ipython`


Then, for eaxmple, folling the code in the [`Download`](http://www2.geog.ucl.ac.uk/~plewis/Geog2021_Coursework/Download.html) section, type or paste the following at the ipython prompt (`In [1]:`):

`import sys`
`sys.path.insert(0,'python')`
`from uncompress_ls import uncompress_ls`
`from sort_landsat import sort_landsat`





