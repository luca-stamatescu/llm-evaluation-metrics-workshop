from promptflow import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool() -> str:
    return '{"current_spend_in_USD":"$50.24","current_vm_count":19,"subscription_count":3}'