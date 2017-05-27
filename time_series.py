from tqdm import tqdm_notebook
import matplotlib.pyplot as plt

def doc_and_year(corpus, all_years, model):
    
    per_doc_topic = []
    for x in tqdm_notebook(model[corpus]):
        per_doc_topic.append(x)
        
    pdtpm_with_doc_n = []
    for x in enumerate(per_doc_topic):
        pdtpm_with_doc_n.append(x)
        
    with_doc_n_and_year = zip(all_years, pdtpm_with_doc_n)
    
    return with_doc_n_and_year

def plot_one_topic(the_data, topic):
    y = [x[1] for x in the_data[topic]]
    x = [int(x[0]) for x in the_data[topic]]
    plt.plot(x, y, 'r:o', color='darkblue')
    plt.title('Percentages of the discussion over time: Topic ' + str(topic))
    plt.show()