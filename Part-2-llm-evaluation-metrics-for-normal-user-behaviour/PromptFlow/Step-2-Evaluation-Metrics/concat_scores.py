import json
from promptflow import tool
import numpy as np
import re


@tool
def concat_results(gpt_coherence_output: str = None,
                   gpt_similarity_output: str = None,
                   gpt_fluency_output: str = None,
                   gpt_relevance_output: str = None,
                   gpt_groundedness_output: str = None,
                   f1_output: float = None,
                   gpt_retrieval_output: str = None,
                   analytical_retrieval_output: float = None,
                   analytical_tool_selection_output: float = None,
                   ada_cosine_similarity_output: float = None):

    load_list = [{'name': 'gpt_coherence', 'output': gpt_coherence_output},
                 {'name': 'gpt_similarity', 'output': gpt_similarity_output},
                 {'name': 'gpt_fluency', 'output': gpt_fluency_output},
                 {'name': 'gpt_relevance', 'output': gpt_relevance_output},
                 {'name': 'gpt_groundedness', 'output': gpt_groundedness_output},
                 {'name': 'f1_score', 'output': f1_output},
                 {'name': 'gpt_retrieval', 'output': gpt_retrieval_output},
                 {'name': 'analytical_retrieval', 'output': analytical_retrieval_output},
                 {'name': 'analytical_tool_selection', 'output': analytical_tool_selection_output},
                 {'name': 'ada_similarity', 'output': ada_cosine_similarity_output}]

    scalar_metrics = ["f1_score", "ada_similarity","analytical_retrieval","analytical_tool_selection"]
    score_list = []
    errors = []
    for item in load_list:
        if item['output']:
            try:
                output = item["output"]
                if item["name"] not in scalar_metrics:
                    try:
                        # First try reading it as a JSON object, and extract the star rating
                        score=json.loads(output)["stars"]
                        score = float(score)
                    except:
                        # If that fails, try reading it as a string and extract the star rating
                        match = re.search(r'\d', output)
                        if match:
                            score = match.group()
                        score = float(score)
                else:
                    score = round(float(output),3)
            except Exception as e:
                score = np.nan
                errors.append({"name": item["name"], "msg":   str(e), "data": item["score"]})
            score_list.append({"name": item["name"], "score": score})
        else:
            score_list.append({"name": item["name"], "score": np.nan})

    variant_level_result = {}
    for item in score_list:
        item_name = str(item["name"])
        variant_level_result[item_name] = item["score"]
        if 'gpt' in item_name:
            variant_level_result[item_name + '_pass_rate'] = 1 if item["score"] > 3 else 0
    return variant_level_result
