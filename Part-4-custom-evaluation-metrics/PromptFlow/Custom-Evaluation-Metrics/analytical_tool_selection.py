from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def tool_selection_validation(selected_tool: str,selected_tool_ground_truth: str) -> str:
    if str(selected_tool) == str(selected_tool_ground_truth):
        return 1
    else:
        return 0