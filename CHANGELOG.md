# Changelog

Notable changes for this project. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/). This project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Each release header has the following format:

    [VERSION] / release date / title (branch, TAG)

The title describes the overall update made with this release. The tag is a
short marker that begins each of the related commit messages.

## [0.3.0] / 2018-11-04 / Quick Failure chapter
### Additions
 * Chapter on quick failure design

## [0.2.1] / 2018-11-04 / Link Layer Cake to Bricks
### Additions
 * Text linking the layer cake idea to the bricks vs monoliths idea

## [0.2.0] / 2018-09-20 / Chapter on Layer Cake Structure
### Additions
 * Add chapter on structuring code like a layer cake
 * Another reason for convention over configuration
 * Wordsmithing in c-internal.txt, c-foundation.txt, c-function.txt,
   c-module.txt

### Changes
 * Date for 0.1.0 was left undefined -- fixed [uc]


## [0.1.0] / 2018-09-20 / Define code layout policy
### Additions
 * Add chapter on code layout
 * Added policy about Oxford comma

### Changes
 * Wordsmithing (c-python3.txt, c-convention.txt, c-internal.txt)

### Removals
 * Removed policy against personal pronouns in README.md because I'm using
   them a lot


## [0.0.4] / 2018-09-17 / Sub-head tests
### Additions
 * Add local test to verify that sub-headings (eg., "Example") do not
   appear in table of contents
 * Add "remote" test to verify that sub-headings do not appear in TOC from
   the version of the content on readthedocs.io
 * Add __doc__ to describe test_whitespace()

### Changes
 * Point at 3.6 list of built-ins rather than the 2.7 list in the Python
   Built-Ins chapter
 * Wordsmithing

## [0.0.3] / 2018-09-17 / Detail tweaks (details, DT)
### Changes
 * Change the date of Python 2.7's end of support, per pyclock.org
 * Wordsmithing: c-convention.txt, c-idiomatic.txt, c-uncaught.txt
 * Make the sidebar sticky and collapsible
### Deletions
 * Eliminate "Example" and lower items in the Table of Contents


## [0.0.2] / 2018-09-16 / Trouble-shooting classic theme on readthedocs.io
### Additions
 * Add untracked files to .gitignore
 * Whitespace at the end of each chapter
 * Describe project policies in README.md

### Changes
 * Wordsmithing in lots of files

### Deletions
 * Removed the html_sidebars dictionary from conf.py


## [0.0.1] / 2018-09-16 / Implementing keep-a-changelog and semantic versioning
### Additions

 * Even better example in c-dry.txt
 * Wordsmith c-tdd.txt and c-bricks.txt to tighten the prose
