# spellchecker


This is a NLP(Natural Language Processing) model.
We used character embedding (chars2vec model) to generate vectorized words and plotted them on vector space to map the closest and semantically similar words together using cosine similarity as the metric.
We used a pre trained NLP model called as chars2vec for this purpose. Having the character embedding, every single word’s vector can be formed even it is out-of-vocabulary words. This model is a CNN which performs the character embedding.
The step by step solution for this problem statement is:
Import the chars2vec model for character embedding.
Import the text file and read the words stored in it.
Make a array(list) of words of the file.
Vectorize all the words of that file by chars2vec model’s vectorize method.
Train the chars2vec model with training set as the list of vectorized words.
Take an input word from the user.
Vectorize the input word using chars2vec vectorize method.
Find the cosine similarity of that input word with every other word from the text file’s list of words.
The word with the highest cosine similarity is the output.
Return the word with the highest cosine similarity which is the correct spelling of the misspelled word.

Problem: Given a text file with a list of words, implement a spell checker to check a given input against the file and recommend corrections to incorrect words. 

Eg: The file contains the following words: "hello, world, java, python, ruby"

Sample input: "word" 
Sample output: "word -> world"
