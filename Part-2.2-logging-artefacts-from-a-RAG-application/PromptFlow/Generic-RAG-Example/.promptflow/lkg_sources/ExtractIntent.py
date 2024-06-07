from promptflow import tool

@tool
def extract_intent(input: str, query: str) -> str:

  # Split the string into parts
  parts = input.split('Tool: ')

  # Extract the message intent
  current_message_intent = parts[0]

  # extract intent
  entries = None
  if 'Single Intents:' in parts[1]:
    tool_part, single_intent_part = parts[1].split('\nSingle Intents:',2)
  elif 'Single Intent:' in parts[1]:
    tool_part, single_intent_part = parts[1].split('\nSingle Intent:',2)
  
  tool_part=tool_part.replace('\"', '').replace('\'', '').replace('\n', '').replace('[', '').replace(']', '')
  if tool_part=="Inventory_SQL":
    chosen_tool="Inventory_SQL"
  elif tool_part=="AzureOpenAIKnowledgeBase":
    chosen_tool="AzureOpenAIKnowledgeBase"
  # this should ideally resolve to some form of exception handling or chitchat function, however to keep the function simple, if a tool is not identified, it defaults to the knowledgebase flow.
  else:
    chosen_tool="AzureOpenAIKnowledgeBase"


  if single_intent_part and len(single_intent_part) == 2:
    return {
      "current_message_intent": current_message_intent,
      "search_intents": entries[1].strip(),
      "tool":tool_part.replace('\"', '').replace('\'', '').replace('\n', '').replace('[', '').replace(']', '')
    }
  return {
      "current_message_intent": query,
      "search_intents": query,
      "tool":tool_part.replace('\"', '').replace('\'', '').replace('\n', '').replace('[', '').replace(']', '')
  }
