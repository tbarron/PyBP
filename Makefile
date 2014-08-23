# with.html: with.md
# 	markdown.pl $< > $@
# 
# context_mgr.html: context_mgr.md
# 	markdown.pl $< > $@


MD = $(wildcard *.md)
HTML = $(MD:%.md=%.html)

PyBP.html: *.txt *.css
	asciidoc -o $@ PyBP.txt

all : $(HTML)

$(HTML) : %.html: %.md
	markdown.pl $< > $@

clean:
	rm -f *.html *~

sync:
	rsync -avdzp *.html integrel:~/www/PyBP


ASCIIDOC_HTML = asciidoc.py --backend=xhtml11 --conf-file=${LAYOUT}.conf \
                --attribute icons \
                --attribute iconsdir=./images/icons \
                --attribute=badges \
                --attribute=revision=$VERS  \
                --attribute=date=$DATE"
