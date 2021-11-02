'''
Use TFIDF to classify top-n neighbor topics for each topic. 
Document frequency is determined using a 3 step process
1. Gather the word and its neighbors (politics, politic, politician, political) or use a prefix search for the general meaning of the word

Retrieve article for topic
Find top-n terms for that article, these are the terms most related to our topic
    the top-n calculation is done by indexing the article using TFIDF
Return the top-n
'''

def get_top_n(topic):
    top_n = []
    return top_n