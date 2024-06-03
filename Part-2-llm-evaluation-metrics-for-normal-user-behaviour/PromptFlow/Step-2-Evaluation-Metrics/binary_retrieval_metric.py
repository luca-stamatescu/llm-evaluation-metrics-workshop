from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def is_groundtruthcontext_in_retrievedcontext(retrievedcontext: str,ground_truth_context: str) -> str:
    if ground_truth_context.replace('\n', '') in retrievedcontext.replace('\n', ''):
        return 1
    else:
        return 0