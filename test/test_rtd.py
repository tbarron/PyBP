import bs4
import os
import pdb
import pytest
import requests
import util


def test_no_sub_heads_toc():
    """
    Verify that no 'Example' sub-headings show up in the rendered HTML TOC

    Examine the sphinxsidebarwrapper div. It will contain nested <ul>
    structures that should not go deeper than two layers deep. Items in the
    second layer should not contain <ul> children.
    """
    pytest.dbgfunc()
    url_tmp = "".join(["https://python-best-practices-",
                       "software-that-just-works",
                       ".readthedocs.io/en/latest/{}.html"])
    for url in [url_tmp.format(x) for x in util.major_files()]:
        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.text, "html.parser")

        for div in [x for x in soup.find_all("div")
                    if 'class' in x.attrs
                    and 'sphinxsidebarwrapper' in x.attrs['class']]:
            msg = "Too many ul layers in {}".format(os.path.basename(url))
            assert util.ul_layers(div) < 4, msg
