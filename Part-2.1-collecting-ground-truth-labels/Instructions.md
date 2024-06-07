# Build out the question and ground truth dataset

## Overview

The first step is to gather a range of questions that you expect the GenAI application to receive. It is important that these are diverse and cover the range of scenarios you expect to see in production.

For this tutorial, examples of questions from the dataset include:
- _"Does Azure OpenAI use customer data to retrain models?"_
- _"Is the latest release of the OpenAI Python library (version>=1.0) supported by Azure OpenAI?"_

Next, a subject matter expert (SME) should generate the responses to these questions. For example:

- _"No, Azure OpenAI doesn't use customer data to retrain models."_
- _"Yes, Azure OpenAI is supported by the latest release of the OpenAI Python library."_

Lastly, other ground truth labels should be included. These include:

- selected_tool_ground_truth: this is the tool that the LLM decided to leverage to answer the question. For example, an LLM might have two tools available to it, an AzureOpenAIKnowledgeBase and a Inventory_SQL database. The SME should label where the data used to answer the question should have been retrieved from.
- groundtruthcontext: this is a single sentence or small chunk of information, taken from the relevant document that contains the information. For example, this RAG application leverages data from the Micrsoft Learn webpages about Azure OpenAI. The SME should label the specific sentence that should be retrieved, in order to answer the question. For example, from the webpages, this answer should have been used using this sentence as the reference _"prompts and generations are not used to train, retrain, or improve the\n\nbase models."_. 

By including these labels in the ground truth dataset, the quality of the retrieval system can be evaluated, to ensure this critical component of the GenAI application is working well.


You may be wondering how many data points are needed to evaluate an LLM. A good starting point is to collect ~50-100 questions, which will have labels provided by a subject matter expert. The more data points, the higher degree of confidence you will have in your application, however these datasets are time consuming to create, so there is a practical limit to the size of your evaluation dataset.

It is possible to leverage techniques such as synthetic data generation, to generate thousands of data points. It is even possible to log the groundtruthcontext and selected_tool_ground_truth when building out synthetic data, by simply generating question and ground truth pairs on a single document at a time.

## Instructions

Review the output CSV from this step, to better understand the structure of an LLM evaluation dataset.
