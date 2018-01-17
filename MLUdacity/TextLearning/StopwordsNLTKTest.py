from nltk.corpus import stopwords

sw = stopwords.words("english")
#print(len(sw))

#there are so many stemmers available
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
print(stemmer.stem('responsiveness'))
print(stemmer.stem('responsivity'))
print(stemmer.stem('unresponsive'))

