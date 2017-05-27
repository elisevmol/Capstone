from fastdtw import fastdtw
from tqdm import tqdm_notebook
from scipy.spatial.distance import euclidean
from sklearn.preprocessing import normalize
import numpy as np
import fastcluster

def DTW(s1, s2):
    'implementing dynamic time warping'
    x = np.array([[int(i[0]), i[1]] for i in s1])
    y = np.array([[int(i[0]), i[1]] for i in s2])
    distance, path = fastdtw(x, y, dist=euclidean)
    return distance

def one_row(row, the_data, n_topics):
    'implemented with DTW so with fastdtw'
    first_row = []
    for i in range(n_topics):
        s1 = the_data[row]
        s2 = the_data[i]
        first_row.append(DTW(s1, s2))
    return first_row

def from_the_data_to_dendogram(n_topics, the_data):
    
    # making a similarity matrix from the DTW values
    similarity_matrix = []
    for i in tqdm_notebook(range(n_topics)):
        similarity_matrix.append(one_row(i, the_data, n_topics))
    
    # reformatting the similarity matrix
    SM = np.array(similarity_matrix).reshape(n_topics,n_topics)
    # l2 normalizing the similarity matrix       http://scikit-learn.org/stable/modules/preprocessing.html
    SM_normalized = normalize(SM, norm='l2')
    # making a distance matrix from the similarity matrix
    DM = 1 - SM_normalized
    
    # Apply Hierchical Aggolmarative Clustering   https://www2.warwick.ac.uk/fac/sci/sbdtc/people/students/2010/jason_piper/code/
    Z = fastcluster.linkage(DM, method='ward', metric='euclidean', preserve_input=True)
   
    return Z