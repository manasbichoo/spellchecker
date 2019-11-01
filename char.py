import chars2vec
import sklearn.decomposition
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

wordsarray=[]
f = open('words.txt')
for word in f.read().split():
    wordsarray.append(str(word))  

print(wordsarray)
# Load Inutition Engineering pretrained model
# Models names: 'eng_50', 'eng_100', 'eng_150', 'eng_200', 'eng_300'
c2v_model = chars2vec.load_model('eng_50')

#words = ['Natural', 'Language', 'Understanding']

# Create word embeddings
word_embeddings = c2v_model.vectorize_words(wordsarray)
print(word_embeddings)
word = str(input("enter a word"))
words1=[]
words1.append(word)
word_embed1=c2v_model.vectorize_words(words1)
print(word_embed1)
similar=cosine_similarity(word_embeddings, word_embed1)
print(max(similar))
i = similar.tolist().index(max(similar)) # i will return index of 2
print(i)
print("The result is")
print(wordsarray[i])


'''# Project embeddings on plane using the PCA
projection_2d = sklearn.decomposition.PCA(n_components=2).fit_transform(word_embeddings)

# Draw words on plane
f = plt.figure(figsize=(8, 6))

for j in range(len(projection_2d)):
    plt.scatter(projection_2d[j, 0], projection_2d[j, 1],
                marker=('$' + words[j] + '$'),
                s=500 * len(words[j]), label=j,
                facecolors='green' if words[j]
                            in ['Natural', 'Language', 'Understanding'] else 'black')

plt.show()'''