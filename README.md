Planet Nuxeo (based on Ring)
============================

Intro
-----

Here's the code for the Nuxeo blog agregator (http://blogs.nuxeo.com/).

It's based on a project called Ring (generic blog agregator written on
top of Flask) but actually it's a fork, due to Ring not being flexible
enough to address the specific needs of this app (yet).

Make and test
-------------

To run the app, you need:

- A recent version of Python (> 2.7, I think)
- At least libxml2-dev and libxslt1-dev (Debian package names)
- pip and virtualenv (use `easy_install pip` if needed)
- Type "make" to fetch and compile dependencies
- Activate the environment (". env/bin/activate")
- Type "make crawl" then "make run" and point your browser to the URL
  given

Deploy
------

For production work:

- Add somehting similar to:
      "5 * * * *     cd /home/blogs/engine ; ./ring.sh crawl"
    to the "blogs" user crontab.
- Start the server (`./ring.sh serve`)
- Set up Apache reverse proxying.

TODO: use `mod_wsgi`

