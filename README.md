# line-to-bullets
A scripted way to deal with the lack of bullet copy/paste outside of Microsoft Word

# Requirements and Dependencies
* [Python 3.x](https://www.python.org/) (tested on 3.4.3 and 3.7.0)
* [Clipboard](https://pypi.org/project/clipboard/) `pip install clipboard` (Cross-platform)

# Goals of code
* Make it easier to bullet a list according to plain text
* **Automatically** copy bulleted list to clipboard for easy use

# Procedure
The procedure varies depending on system (or even program). Check the headings below to see which procedure to follow.
## IDLE (and possibly Linux-like systems after program start)
1. Start up the program (IDLE: F5; Linux-like: via either IDLE or command line similar to Windows below).
2. Provide the bullet character(s) you want to use as prompted.
3. Indicate whether a space should be added between the bullet character and text (default `True`; must type `no` (case-insensitive) to remove).
4. Either write or copy the lines. After the final line, start a new line, press `CTRL`+`D`, and then press `ENTER`.
  * NOTE: for IDLE, if pasted content ends with a new line, the pasted new line may have to be deleted before 4 is executed.

## Windows Command line
1. Type in `python [directory_location]/line-to-bullets.py`.
2. Provide the bullet character(s) you want to use as prompted.
3. Indicate whether a space should be added between the bullet character and text (default `True`; must type `no` (case-insensitive) to remove).
4. Either write or copy the lines. After the final line, start a new line, press `CTRL`+`Z`, and then press `ENTER`.

# Why make this code?
My End-User Desktop Support classmates at [Per Scholas](https://perscholas.org/) have been making LinkedIn profiles and have been cross-pollinating between their resumes and said profiles. This produces satisfactory results within *Microsoft Word*, which changes the text from a bulleted, indented list to a bulleted list with space between the bullet (if not ASCII, often changes into a square glyph) and the bulleted text. This is not the case in either Google Docs or Apache OpenOffice, however. Depending on the length of the list, this can incur much annoyance. This is an attempt to decrease said annoyance, not just for bulleted lists, but also, with some more information and adaptation (a dictionary or letter awareness) can be used in some form of morphological (linguistics) generator.

## Morphological generator?
Consider the prefix `a-`. One of the meanings of this prefix is "without". Several words use this prefix:
- Atheism (without + belief in God)
- Agnostic (without + knowledge of a/the/any divine)
- Asexual (without + sexual attraction)
- Anemia (without + blood)

In all but one of these words, the suffix `a-` is added to the word to form a new, negated word. In the final one, however, the presence of a vowel `e` at the beginning of the modified Greek word `emia` (blood) seems to force the variant `an-` instead of the default `a-`, possibly to avoid doubling the vowel nucleus. The `an-` form also appears in the word `anhydrous` (without water). Using the code above, the conditions can be added in to generate words with the matching prefix.
