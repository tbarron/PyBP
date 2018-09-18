import bs4
import glob
import os
import pdb
import py
import pytest
import re
import util


def test_whitespace():
    """
    Verify that each chapter file ends with three lines of whitespace (i.e., in
    the source, this appears as three lines each containing only a vertical
    bar)
    """
    for path in glob.glob("docs/c-*.txt"):
        fobj = py.path.local(path)
        text = fobj.readlines()
        for idx in range(-3, 0):
            if text[idx].strip() != "|":
                pytest.fail("{} does not end with whitespace lines".format(path))
    return True


def test_no_sub_heads_toc():
    """
    Verify that no 'Example' sub-headings show up in the rendered HTML TOC

    Examine the sphinxsidebarwrapper div. It will contain nested <ul>
    structures that should not go deeper than three layers.
    """
    pytest.dbgfunc()
    path_tmp = "docs/_build/html/{}.html"
    for fpath in [path_tmp.format(x) for x in util.major_files()]:
        fobj = py.path.local(fpath)
        soup = bs4.BeautifulSoup(fobj.read(), "html.parser")

        for div in [x for x in soup.find_all("div")
                    if 'class' in x.attrs
                    and 'sphinxsidebarwrapper' in x.attrs['class']]:
            msg = "Too many ul layers in {}".format(fpath)
            assert util.ul_layers(div) < 4, msg


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
