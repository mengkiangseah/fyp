#!/bin/bash

alias ts='./typeset.sh'

pdflatex --file-line-error --synctex=1 --shell-escape "main.tex"

bibtex main

pdflatex --file-line-error --synctex=1 --shell-escape "main.tex"

pdflatex --file-line-error --synctex=1 --shell-escape "main.tex"

rm main.aux
rm main.log
rm main.bbl
rm main.blg
rm main.synctex.gz
