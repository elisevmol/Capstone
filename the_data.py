from collections import Counter
from tqdm import tqdm_notebook

def topic_getter(topic_number, total_list):
    '''you give it a topic number (example 1) and the total_list (with_doc_n_and_year) and it returns a list 
    where the first element is the topic number, and the other elements are the topic probability matrix and 
    corresponding abstract number and year where the topic is occurs'''
    topic_list = [topic_number]
    for x in total_list:
        for y in x[1][1]:
            if y[0] == topic_number:
                topic_list.append(x)
    return topic_list

def cleaner(year_percentage):
    '''removes all the doubles in the list year_percentages for one topic so if two elements are posted in 2002 
    the second elements are added, and they are stored under the same name: 2002'''
    formatted = tuple([(year_and_procent[0], year_and_procent[1])] for year_and_procent in year_percentage)
    counts = sum((Counter(dict(sublist)) for sublist in formatted), Counter())
    result = list(counts.items()) 
    result.sort()
    return result

def transform(one_topic_data):
    the_result = []
    data = one_topic_data[1:]
    for abstract in data:
        second = 0
        for x in abstract[1][1]:
            if x[0] == one_topic_data[0]:
                second = x[1] 
        the_result.append([abstract[0], second])
    return the_result

def fill_empty(year_and_percentage, min_year, time_range):
    '''takes a list of years and corresponding percentages [so one topic], 
    and returns that same data, but for all years where there is no 
    corresponding percentage 0 is placed'''
    for year in [str(i + min_year) for i in range(time_range)]:
        if year not in [x[0] for x in year_and_percentage]:
            year_and_percentage.append((year, 0))
            
    year_and_percentage.sort()
    return year_and_percentage

def divide(x, all_years):
    '''devide each item of a list where the first element is a year and the second is the corresponding value
    by the amount of publications that year'''
    total = []
    for item in x:
        year = item[0]
        if Counter(all_years)[year] != 0:
            total.append([year, (item[1] / Counter(all_years)[year])])
    return total

def from_base_to_data(topic_number, with_doc_n_and_year, all_years):
    '''from the topic number and the list with_doc_n_and_year to a plot of one topic (the one which topic_number is given)'''
    min_year = int(min(all_years))
    max_year = int(max(all_years))
    time_range = (max_year - min_year)
    
    base = topic_getter(topic_number, with_doc_n_and_year)
    clean = cleaner(transform(base))
    complete = fill_empty(clean, min_year, time_range)
    divided = divide(complete, all_years)
    return divided

def code_the_data(with_doc_n_and_year, all_years, n):
    
    the_data = []
    for i in tqdm_notebook(range(n)):
        the_data.append(from_base_to_data(i, with_doc_n_and_year, all_years))
        
    return the_data
