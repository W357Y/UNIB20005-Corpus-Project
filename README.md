# UNIB20005 Corpus Project

Authors:

  - Lucas Cooper: 540969
  - Matt Westwood: 377467

## Background

This project consists of two main files: 

  - getDocs.sh: This is designed to be run on a UNIX based system and downloads the pages specified in 'urls.txt' to the 'Docs' folder for processing.
  - Corpus.py: This file is designed to be used as a Python module and does a few things:
    - Creates a plaintext corpus out of the downloaded HTML documents by using lxml to extract plaintext from the 'bodyContent' div conveniently programmed in by Wikipedia.
    - Tokenizes the plaintext corpus with Regular Expressions.
    - Calculates the lexical diversity of the corpus.

## Usage

With Corpus.py and the Docs directory in the current working directory, do the following in Python:
    
    import Corpus

    Corpus.clean()
    words = Corpus.tokenize()

    #Other such things.