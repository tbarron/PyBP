import glob


def section_list():
    """
    Return the list of section files globbed from docs

    Source section files have names like docs/s-SECTION.txt. This routine will
    return just the SECTION part.
    """
    rval = []
    for fpath in glob.glob("docs/s-*.txt"):
        section_name = fpath.replace("docs/", "").replace(".txt", "")
        rval.append(section_name)
    return rval


def major_files():
    """
    Return the section files plus index
    """
    rval = section_list()
    rval.insert(0, "index")
    return rval


def ul_layers(soup):
    """
    Count the layers of <ul> nesting in a BeautifulSoup object. This function
    is recursive.
    """
    rval = max([ul_layers(ul) for ul in soup.find_all('ul')], default=0)
    return rval + 1
