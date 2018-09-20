Working on deploying this material at readthedocs.io:

   [Python Best Practices: Writing Software that Just Works](http://python-best-practices-software-that-just-works.readthedocs.io/en/latest/)

Policies:

 * [Semantic Versioning](https://semver.org/spec/v2.0.0.html): MAJOR.MINOR.PATCH

    * PATCH advances on minor changes to the text that don't affect the table of
      contents
    * MINOR advances on content changes that alter the table of contents
    * MAJOR advances on global edits intended to change the overall
      character of the text (e.g., removing personal pronouns, minimizing
      passive voice, edition updates, etc.)

 * Release Cycle

    * git checkout -b meaningful-branch-name
       * ... edit the content ...
       * ... update docs/pybp_ver.py ...
       * ... update CHANGELOG.md ...
       * git commit
       * verify desired outcome or return to edit step
    * git tag -a new-version
    * git checkout master
    * git merge meaningful-branch-name
    * git push

 * Follow the general conventions of
   [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

 * Avoid passive voice.

 * Use the Oxford comma. That is, in a list of parallel constructions like
   "this, that, and the other", insert a comma after the penultimate item
   before the word "and". Without the Oxford comma, one may wind up with
   ambiguous phrases like, "To my parents, Ayn Rand and God".
