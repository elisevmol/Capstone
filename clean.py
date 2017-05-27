import string
from tqdm import tqdm_notebook
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.wordnet import WordNetLemmatizer


def complete_metadata_code(metadata):
    
    # remove all elements that do not have an year, abstract or journal
    all_data = []
    for e in tqdm_notebook(metadata):
        if e[1] != [] and e[1] != [None] and e[2] != [] and e[3] != []:
            all_data.append(e)
   
    # convert all abstracts and journals to strings
    strings = []
    for entry in tqdm_notebook(all_data):
        strings.append([entry[0], [entry[1][0].encode('ascii', 'ignore')], entry[2], [entry[3][0].encode('ascii', 'ignore')]])
          
    # remove all entries where the abstracts are empty in any way
    complete_metadata = []
    for e in tqdm_notebook(strings):
        if e[1][0].isspace() == False and e[1][0] != '' and any(x.isalpha() for x in e[1][0]) == True:
            complete_metadata.append(e)
 
    return complete_metadata


def replace_chars(inp):
    '''replaces / - . \ by a space so we won't delete any words that are actually two words later such as km/mm'''
    chars_to_replace = "/-.\\'"
    replace_punctuation = string.maketrans(chars_to_replace, ' '*len(chars_to_replace))
    text = inp.translate(replace_punctuation)
    return text

def complete_abstracts_code(journals, complete_metadata):
    
    #make a list of all the abstracts if the journal is in journals
    specific_abstracts = []
    check = [x[3][0] for x in complete_metadata]
    no_double_journals = list(set(journals))
    
    if check == journals:
        specific_abstracts = [e[1][0] for e in complete_metadata]
    else:
        for e in tqdm_notebook(complete_metadata):
            if any(e[3][0] == x for x in no_double_journals):
                specific_abstracts.append(e[1][0])

    # apply replace_chars to all abstracts to avoid losing the wrong words when making the vocab
    complete_abstracts = []
    for abstract in tqdm_notebook(specific_abstracts):
        complete_abstracts.append(replace_chars(abstract))
        
    return complete_abstracts


def complete_vocab_code(complete_abstracts):
    lmtzr = WordNetLemmatizer()
    
    vectorizer = TfidfVectorizer(min_df=0.0003, max_df=0.5) 
    X = vectorizer.fit_transform(complete_abstracts)
    rough_vocab = vectorizer.get_feature_names()
    
    complete_vocab = []
    for word in tqdm_notebook(list(set(rough_vocab))):
        word = lmtzr.lemmatize(word)
        if word.isalpha() == True and len(word) > 1 and word not in stopwords.words('english'):
            complete_vocab.append(word)
        
    return complete_vocab