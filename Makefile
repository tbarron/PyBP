# with.html: with.md
# 	markdown.pl $< > $@
# 
# context_mgr.html: context_mgr.md
# 	markdown.pl $< > $@


MD = $(wildcard *.md)
HTML = $(MD:%.md=%.html)

PyBP.html: *.txt
	asciidoc -a toc -a index -o $@ $<

all : $(HTML)

$(HTML) : %.html: %.md
	markdown.pl $< > $@

clean:
	rm -f *.html *~

sync:
	rsync -avdzp *.html integrel:~/www/PyBP

