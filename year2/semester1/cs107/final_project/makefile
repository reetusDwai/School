# Makefile for zipping Python and Markdown files in the current directory

ZIPFILE = cse107_Kalem_Smith_finalProject.zip
INCLUDE = *.py *.md

all: $(ZIPFILE)

$(ZIPFILE):
	@echo "Creating zip file $(ZIPFILE) with Python and Markdown files..."
	@zip -r $(ZIPFILE) $(INCLUDE)

clean:
	@echo "Cleaning up..."
	@rm -f $(ZIPFILE)

.PHONY: all clean
