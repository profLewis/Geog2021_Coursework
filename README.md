# Geog2021_Coursework

## Coursework notes for Geog 2021

### Accessing a test dataset

Whilst you will need to order and download the data yourselves in this practical, a test dataset is available for you.

You should make a directory to work in, e.g.:

`bash% mkdir -p ~/DATA/where_I_put_the_notes`

`bash% cd ~/DATA/where_I_put_the_notes`


Then, download (selecting from menu) the test data file [`LT51220441995364-SC20150217103827.tar.gz`](http://www2.geog.ucl.ac.uk/~plewis/Geog2021_Coursework/LT51220441995364-SC20150217103827.tar.gz), or do one of the following:

`bash% wget http://www2.geog.ucl.ac.uk/~plewis/Geog2021_Coursework/LT51220441995364-SC20150217103827.tar.gz`

or, if you are on the UCL Geography system, you can simply copy the file:

`bash `cp ~plewis/p/Geog2021_Coursework/LT51220441995364-SC20150217103827.tar.gz ~/DATA/where_I_put_the_notes`


### Accessing the notes via a web page

These coursenotes are available as web pages (html) from the [Geog 2021 course overview page](http://www2.geog.ucl.ac.uk/~plewis/geog2021) or more directly from the [practical introduction page](http://www2.geog.ucl.ac.uk/~plewis/Geog2021_Coursework/CW-1-Pearl-River-Intro.html).

### Accessing the notes via github

The notes are also available on [github](https://github.com/profLewis/Geog2021_Coursework). You can directly download the notes from [github](https://github.com/profLewis/Geog2021_Coursework), either using some [`git`](http://en.wikipedia.org/wiki/Git_(software)) software, e.g:

`bash% mkdir -p ~/DATA/where_I_put_the_notes`

`bash% cd ~/DATA/where_I_put_the_notes`

`bash% git clone https://github.com/profLewis/Geog2021_Coursework.git`

or by downloading the [course notes as a zip file](https://github.com/profLewis/Geog2021_Coursework/archive/master.zip).

If you use `git`, you can apply any updates to the notes:

`bash% mkdir -p ~/DATA/where_I_put_the_notes`

`bash% cd ~/DATA/where_I_put_the_notes/Geog2021_Coursework`

`bash% git reset --hard HEAD`

`bash% git pull`

You can also fork the notes and create your own version.

## Using the notes for Geog 2021

You can of course just read and digest the html notes, but you will find that there are snippets of computer code (in Python) at times. Note that you **do not** need to use the Python codes to do this coursework: you can do everything you need in ENVI and Excel. That said, you will be processing quite a number of images, and you may find the Python codes useful for at least semi-automating the tasks.

### Running ipython to use the notes for Geog 2021

Assuming you are on a unix system (including OS X, linux etc.), then first change directory to where the notes are:

`bash% mkdir -p ~/DATA/where_I_put_the_notes`

`bash% cd ~/DATA/where_I_put_the_notes/Geog2021_Coursework`

Then start an [`ipython`] session:

`bash% ipython`


Then, for example, folling the code in the [`Download`](http://www2.geog.ucl.ac.uk/~plewis/Geog2021_Coursework/Download.html) section, type or paste the following at the ipython prompt (`In [1]:`):

`import sys`

`sys.path.insert(0,'python')`

`from uncompress_ls import uncompress_ls`

`from sort_landsat import sort_landsat`

This will load some python codes from the local `python` directory that you can use.

Again, following the example, we can specify a Landsat data file:

`dirname = 'LT51220441995364-*.tar.gz'`

which assumes there is one or more files that match the pattern `LT51220441995364-*.tar.gz` in the current directoy ('folder') (see section above on downloading a test dataset).

Then, uncompress this file with:

`files = uncompress_ls(dirname)`

The variable `files` then contains a list of the files:

`print files`



