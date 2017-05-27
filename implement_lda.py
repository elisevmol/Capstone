from gensim import corpora, models, similarities
from nltk import word_tokenize
from tqdm import tqdm_notebook

def strip_abstract(abstract, vocab_set):
    
    stripped_abstract = []
    for word in word_tokenize(abstract.lower()):
        if word in vocab_set:
            stripped_abstract.append(word)
    return stripped_abstract


def from_abstracts_to_topics(complete_abstracts, complete_vocab, n_topics):
    
    complete_vocab_set = set(complete_vocab)
    
    stripped_abstracts = []
    for abstract in tqdm_notebook(complete_abstracts):
        stripped_abstracts.append(strip_abstract(abstract, complete_vocab_set))
    
    dictionary = corpora.Dictionary(stripped_abstracts)

    corpus = []
    for text in tqdm_notebook(stripped_abstracts):
        corpus.append(dictionary.doc2bow(text))
       
    model = models.LdaModel(corpus, id2word=dictionary, num_topics=n_topics, random_state=2, minimum_probability=0.1)
    lda_model = model.print_topics(n_topics)
    
    return stripped_abstracts, lda_model, corpus, model, dictionary