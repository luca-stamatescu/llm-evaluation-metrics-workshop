from typing import List
from promptflow import tool, log_metric
import numpy as np
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score

@tool
def aggregate_variants_results(results: List[dict], metrics: List[str]):
    aggregate_results = {}
    for result in results:
        for name, value in result.items():
            if name in metrics[0]:
                if name not in aggregate_results.keys():
                    aggregate_results[name] = []
                try:
                    float_val = float(value)
                except Exception:
                    float_val = np.nan
                aggregate_results[name].append(float_val)

    for name, value in list(aggregate_results.items()):  # Create a copy for iteration
        if name in metrics[0]:
            if name == 'analytical_tool_selection':
                # Calculate metrics directly from the list of predictions
                precision = precision_score(value, [1]*len(value))
                recall = recall_score(value, [1]*len(value))
                accuracy = accuracy_score(value, [1]*len(value))
                f1 = f1_score(value, [1]*len(value))
                
                aggregate_results["analytical_tool_selection_precision"] = precision
                aggregate_results["analytical_tool_selection_recall"] = recall
                aggregate_results["analytical_tool_selection_accuracy"] = accuracy
                aggregate_results["analytical_tool_selection_f1_score"] = f1
                log_metric('analytical_tool_selection_precision', precision)
                log_metric('analytical_tool_selection_recall', recall)
                log_metric('analytical_tool_selection_accuracy', accuracy)
                log_metric('analytical_tool_selection_f1_score', f1)

            aggregate_results[name] = np.nanmean(value)
            aggregate_results[name] = round(aggregate_results[name], 2)
            log_metric(name, aggregate_results[name])
    return aggregate_results
