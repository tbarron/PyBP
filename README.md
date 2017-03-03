ISSUES

  * URL SENSITIVITY: Locally, site.url is "https://localhost:4000". When
    we're deployed on github pages, site.url is
    "https://tbarron.github.io".

    Locally, pages are at locations like

        https://localhost:4000/pages/01_always.html

    On github pages, that page would show up at

        https://tbarron.github.io/PyBP/pages/01_always.html

  * GITHUB METADATA: Local regeneration after a file change triggers a
    github metadata message about "https://api.github.com/orgs/tbarron"
    being a 404 on the first regen. This is a bug in github metadata where
    they check whether tbarron is an org or a user and make the wrong
    choice because my account is associated with the ORNL TechInt org. As
    far as I can tell, this is harmless, just annoying.
