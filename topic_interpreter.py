import os
from gensim import models

def topic_words(topic):
    topic_words = [w_p.split('"')[1] for w_p in str(topic[1]).split('+')]
    return ' '.join(topic_words)

def find_nt(i, corpus, dictionary):
    
    model = models.LdaModel(corpus, id2word=dictionary, num_topics=i, random_state=2, minimum_probability=0.1) 
    lda_model = model.print_topics(i)
    
    all_topic_words = [topic_words(topic) for topic in lda_model]

    place = '/Users/elise/Documents/Capstone/Packages/topic_interpretability-master/data/topics.txt'
    
    f = open(place, 'w')
    for item in all_topic_words:
        f.write("%s\n" % item)
    f.close() 
    
    string = 'echo "Completed Loop: "' + str(i)
    os.system(string)
    os.chdir('/Users/elise/Documents/Capstone/Packages/topic_interpretability-master')
    os.system("bash 'run-oc.sh'")
    
    results = '/Users/elise/Documents/Capstone/Packages/topic_interpretability-master/results/topics-oc.txt'
    topic_coherence = []
    
    f = open(results)
    for x in f.readlines():
        topic_coherence.append(x)
    f.close()
    
    return [topic_coherence, lda_model]