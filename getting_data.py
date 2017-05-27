import os
from tqdm import tqdm_notebook
from xml.etree.cElementTree import iterparse 

def constructing_metadata(path):
    context = iterparse(path, events=("start", "end"))

    context = iter(context)
    event, root = context.next()

    metadata = [[x.text for x in root.findall("./front/article-meta/title-group/article-title")],
               [x.text for x in root.findall("./front/article-meta/abstract/p")],
               [x.text for x in root.findall("./front/article-meta/pub-date/year")],
               [x.text for x in root.findall("./front/journal-meta/journal-title-group/journal-title")]]
    
    for event, elem in context:
        for x in elem:
            if event == "end" and elem.tag == "record":
                root.clear()
    
    return metadata


def source_to_xml(source):
    
    list_of_paths = []
    for path, dirs, files in os.walk(source):
        for f in files:
            list_of_paths.append(path + '/' + f)

    xml_paths = []
    for path in tqdm_notebook(list_of_paths):
        if path[-3:] == 'xml':
            xml_paths.append(path)
            
    metadata = []
    for path in tqdm_notebook(xml_paths):
        metadata.append(constructing_metadata(path))
        
    return metadata