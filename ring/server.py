#!env/bin/python
# -*- coding: UTF8 -*-


import time
import datetime

from flask import *
from werkzeug.contrib.atom import AtomFeed

import util
from models import Entry, Session, Feed, all_feeds
from config import config

CFG = config()

# Constants
MAX_ENTRIES = 5

BLOG = {
    'url': 'http://blogs.nuxeo.com/',
    'title': u"Blogs Nuxeo",
    'tagline': u"Open Source ECM - by the team who does it",
    'menu': [{'url': "", 'title': 'Home'},
             #{'url': "about", 'title': 'About'},
             #{'url': "category/public-speaking", 'title': 'Public Speaking'},
    ]
}


# Use /media instead of default /static because /static is already used.
app = Flask(__name__, static_path='/media')
app.jinja_loader.searchpath = ['./templates'] + app.jinja_loader.searchpath

@app.before_request
def connect_db():
    g.session = Session()
    g.age = util.age

# REST endpoints

@app.route('/')
def home():
    feeds = all_feeds()
    feeds_dict = {}
    for feed in feeds:
        feeds_dict[feed.id] = feed

    query = g.session.query(Entry)

    # "Featured" blogs (everything but "dev")
    featured = query.filter(Entry.source!='dev').order_by(Entry.published.desc()).limit(MAX_ENTRIES).all()
    for post in featured:
        post.feed = feeds_dict[post.source]

    # Dev blog
    dev = query.filter(Entry.source=='dev').order_by(Entry.published.desc()).limit(MAX_ENTRIES).all()
    for post in dev:
        post.feed = feeds_dict[post.source]

    model = dict(featured=featured, dev=dev, feeds=feeds, blog=BLOG)
    response = make_response(render_template("home.html", **model))
    return response


@app.route('/rss')
@app.route('/atom.xml')
def feed():
    feed = AtomFeed(BLOG['title'], url=BLOG['url'], feed_url=request.url,
                    subtitle=BLOG['tagline'])
    query = g.session.query(Entry)
    entries = query.order_by(Entry.published.desc()).limit(MAX_ENTRIES)

    for e in entries:
        title = "[%s] %s" % (e.source, e.title)
        feed.add(title=title, content=e.content, content_type='text/html',
                 author=e.author, url=e.link, id=e.id,
                 updated=datetime.datetime.utcfromtimestamp(e.updated),
                 published=datetime.datetime.utcfromtimestamp(e.published))
    return feed.get_response()

# Utility functions

def get_new_dates(entries):
    d = {}
    for entry in entries:
        date = time.localtime(entry.published)[0:3]
        d[date] = d.get(date, ()) + (entry,)

    l = d.items()
    l.sort(lambda x, y: -cmp(x[0], y[0]))
    new_dates = {}
    for date, l1 in l:
        new_dates[l1[0]] = datetime.date(*date)
    return new_dates


def main():
    app.run(port=7000, debug=True)

if __name__ == '__main__':
    main()

