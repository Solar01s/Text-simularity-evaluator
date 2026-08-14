# Text-simularity-evaluator
Black Papochka is a project where I wanted to compare text word word by word. This program doesn't rely on word weights  and their weighting, but compares by word order. At the time, I wanted to understand NumPy - it's the first project using a mathematical engine in general.

# How it works: 
1) You enter two texts.
2) They are converted into a single list of words.
3) Two vectors of zeros are created, each representing the size of the words from step 2.
4) The program finds matches between the text and words from step 2 and replaces them with "1."
5) The vectors are then multiplied and normalized, and the probability of
similarity between the texts is calculated. The result is
multiplied by 100 (for %), and the data is output to the console.

# The point is:
it's not intelligence at all. it's just a program, that searches 
for matches by words, and even then only whole words.
