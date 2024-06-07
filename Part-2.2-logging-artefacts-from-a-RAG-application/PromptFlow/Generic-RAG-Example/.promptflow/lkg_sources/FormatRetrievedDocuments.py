import json
import os
from promptflow import tool
import numpy as np
from numpy.linalg import norm

# This is a dummy function, to represent a knowledgebase that returns context documents. Azure AI Search was used here, however it was removed to simplify this workshop. This is not ideal, as optimizing the retrieval step (number of documents returned, search parameters, etc) is key to the performance of a RAG application, but this is useful as a reference. 
@tool
def dummy_knowledgebase(user_query: str,embedded_user_query) -> str:

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Join the directory of the current script with the filename
    file_path = os.path.join(script_dir, 'knowledgebase.json')

    # Load the JSON data
    with open(file_path) as f:
        data = json.load(f)

    # List to store the elements and their corresponding results
    results = []

    # Iterate over the elements in the 'value' list
    for element in data['value']:
        # Access the 'content_vector' key in each element (which is a dictionary)
        content_vector = element['content_vector']
        result = np.dot(embedded_user_query, content_vector) / (norm(embedded_user_query) * norm(content_vector))
        
        # Add the element and its result to the list
        results.append((result, element))

    # Sort the list in descending order by result
    results.sort(key=lambda x: x[0], reverse=True)

    # Get the content of the top 3 elements and combine them into a single string
    top_3_content = ' '.join(element['content'] for result, element in results[:3])


    if "RETRIEVAL_OVERRIDE" in user_query:
        returned_document="""
        Aardvarks are medium-sized, burrowing, nocturnal mammals native to Africa.[2][3] They have a long snout, similar to that of a pig, which is used to sniff out food.

        Aardvarks are the only living species of the order Tubulidentata,[4][5] although other prehistoric species and genera of Tubulidentata are known. They are afrotheres, a clade that also includes elephants, manatees, and hyraxes.

        They are found over much of the southern two-thirds of the African continent, avoiding areas that are mainly rocky. Nocturnal feeders, aardvarks subsist on ants and termites by using their sharp claws and powerful legs to dig the insects out of their hills. Aardvarks also dig to create burrows in which to live and rear their young.

        Aardvarks are listed as least concern by the IUCN, although their numbers are decreasing.
        """
    else:
        returned_document=top_3_content

    # certain new line characters cause problems in later steps.
    returned_document = returned_document.replace('\r\n', '').replace('\n', '')
    return returned_document