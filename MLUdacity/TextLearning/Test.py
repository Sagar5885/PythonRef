from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

str1 = "Hi this is sagar here wanted to talk to you in the meeting"

str2 = "The main topic is about go project and many question regarding it"

str3 = "Also question regarding job we ran yesterday"

email_list = [str1, str2, str3]
vectorizer.fit(email_list)
bag_of_words = vectorizer.transform(email_list)

print(bag_of_words)

print(vectorizer.vocabulary_.get("question"))