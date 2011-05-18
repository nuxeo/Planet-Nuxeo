
from BeautifulSoup import BeautifulSoup
import re, time

# Real constants
MINUTE = 60
HOUR = 60*MINUTE
DAY = 24*HOUR
MONTH = 30*DAY
YEAR = 365*DAY

def strip_tags(src):
    """Strips html tags and consolidates white spaces."""
    res = ''.join(BeautifulSoup(src).findAll(text=True))
    res = re.sub(r"\s+", " ", res).strip()
    return res

def summarize(text, length=100):
    """Returns a summary of the text, i.e. text cut to ~length characters"""
    if len(text) < length:
        return text
    else:
        dot_position = text[length:].find(".")
        if dot_position < 0:
            return text
        else:
            return text[0:length] + text[length:length+dot_position+1]

def age(t):
    now = int(time.time())
    dt = now - t
    if dt < MINUTE:
        return "%d seconds ago" % dt
    if dt < 2*MINUTE:
        return "about 1 minute ago"
    if dt < HOUR:
        return "%d minutes ago" % (dt/MINUTE)
    if dt < 2*HOUR:
        return "about 1 hour ago"
    if dt < DAY:
        return "about %d hours ago" % (dt/HOUR)
    if dt < 2*DAY:
        return "yesterday"
    if dt < MONTH:
        return "about %d days ago" % (dt/DAY)
    if dt < 2*MONTH:
        return "last month"
    if dt < YEAR:
        return "about %d months ago" % (dt/MONTH)
    return "%d years ago" % (dt/YEAR)

