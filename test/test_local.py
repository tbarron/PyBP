import bs4
import glob
import os
import pdb
import py
import pytest


def test_whitespace():
    """
    """
    for path in glob.glob("docs/c-*.txt"):
        fobj = py.path.local(path)
        text = fobj.readlines()
        for idx in range(-3, 0):
            if text[idx].strip() != "|":
                pytest.fail("{} does not end with whitespace lines".format(path))
    return True


def test_find_index():
    """
    prove py.test runs, find index.html
    """
    pytest.skip()
    cwd = py.path.local(os.getcwd())
    assert cwd.strpath == "/Users/tbarron/prj/github/PyBP"

    htmldir = cwd.join("docs/_build/html")
    index = htmldir.join("index.html")
    soup = bs4.BeautifulSoup(index.read(), "html.parser")
    for link in soup.find_all("a"):
        # print(link)
        # link types
        #   "#"
        #   "#anchor"
        #   filename
        #   filename#anchor
        #   http://host/uri
        href = link.attrs['href']
        # print(href)
        if "#" == href:
            file_o = index
            file_s = file_o.strpath
            anchor = ""
        elif "#" == href[0]:
            file_o = index
            file_s = file_o.strpath
            anchor = href[1:]
        elif "#" in href:
            (fname, anchor) = href.split("#")
            file_o = htmldir.join(fname)
            file_s = file_o.strpath
        elif 'http:' in href:
            file_s = href
            anchor = ""
        else:
            file_o = htmldir.join(href)
            file_s = file_o.strpath
            anchor = ""

        assert file_o.exists()
        print(href)
        print(">>> path:   '{}'".format(file_s))
        print(">>> anchor: '{}'".format(anchor))
        print(">>> exists: {}".format(file_o.exists()))
