from promptflow import tool

@tool
def format_reply(knowledgebase_reply: str,sql_reply: str,selected_tool:str,knowledge_base_context:str,sql_context:str) -> str:
  if selected_tool == "AzureOpenAIKnowledgeBase":
    reply=knowledgebase_reply
    context=knowledge_base_context
  else:
    reply=sql_reply
    context=sql_context

  reply = clean_markdown(reply)
  return {"agent_reply":reply,"context":context}

def clean_markdown(input: str) -> str:
  start = 0
  inBlock = False
  result = ""
  while True:
    nextStart = input.find("```", start)
    if nextStart == -1:
      break
    result += input[start:nextStart]
    if inBlock:
      if nextStart > 0 and input[nextStart - 1] != '\n':
        result += "\n"
      result += "```\n"
      inBlock = False
    else:
      result += "```"
      inBlock = True
    start = nextStart + 3
  result += input[start:]
  if inBlock:
    result += "```"
  return result
