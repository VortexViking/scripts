TO SAVE THE OUTPUT OF THE (ADVANCED)SCRAPE (TEXT ONLY)

TYPE 

LINUX/MACOS
```
python3 web-scrape.md > chosen_name.txt
```

Pick any file format you want!

For the images it wil just put them in your downloads folder.

FOR THE `article-scrape.py` IT EXTRRACTS ALL TEXT AS PLAIN TEXT

``` bash
python3 article-scrape.py > chosen_name.txt
```

IF YOU WANT TO SEARCH FOR KEYWORDS AND NO EXPORT:

``` bash
python3 article-scrape.py | grep keyword
```

AND IF YOU WANT TO SEARCH KEYOWRDS AND ONLY SAVE THE KEYWORD SEARCH OUTPUT:

``` bash
python3 article-scrape.py | grep keyword > chosen_name.txt
```

AND IF YOU WANT AUTOMATIC MARKDOWN SYNTAX HIGHLIGHTING, USE PANDOC

`sudo apt install pandoc`

AND RUN:
```
python3 article-scrape.py > chosen_name.txt && pandoc chosen_name.txt -o markdown_file_name.md
```

AND YOU CAN DO THE SAME WITH THE GREP:

```
python3 article-scrape.py | grep keyword > chosen_name.txt && pandoc chosen_name.txt -o markdown_file_name.md
```
