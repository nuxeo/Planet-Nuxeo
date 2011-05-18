import time
import util

from nose.tools import assert_equals

def test_strip_tags():
    src = "<html>\n<body><p>toto titi.</p>\n  tata tutu.</html>"
    expected = "toto titi. tata tutu."
    assert_equals(util.strip_tags(src), expected)

def test_sumarize():
    src = "Hello. Kernigham. Ritchie."
    expected = "Hello. Kernigham."
    assert_equals(util.summarize(src, 8), expected)

def test_sumarize2():
    src = "Hello. Kernigham & Ritchie."
    expected = src
    assert_equals(util.summarize(src, 8), expected)

def test_age():
    now = time.time()
    assert_equals(util.age(now - util.MINUTE * 1.5), "about 1 minute ago")
