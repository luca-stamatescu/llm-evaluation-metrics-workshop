# An Applied Example of Evaluating Changes to a GenAI Application

## Overview

Having an evaluation framework is key for tracking how the performance of your GenAI application changes over time. For example, if a new LLM is released, which has been reported to have  better performance and lower cost, you will likely want to switch across this model. However, how can you be sure that for your specific use case, performance won't degrade? Similarly, if your team add a significant number of new documents to your knowledge base to help the model answer a wider range of questions, how can you be sure that it will still be able to correctly answer the previous set of questions it was designed for, and that the model isn't confused by the additional volume of information?

In this step, we will demonstrate an example of evaluating a GenAI application before and after changing model versions.


## (Optional) Pre-work

The below steps are optional, as the output of the below steps have been included in the Input folder.

If you would like to try making your own changes to the either the included GenAI application, or to your own GenAI application, you are encouraged to develop your own evaluation datasets!

- (Optional) Make a change to the sample GenAI application PromptFlow provided, for generating testing artefacts. For example, modify the system prompt, change the model version, or add additional data to the Dummy SQL or knowledgebase. This is so that the testing artefacts (such as the model's response) are slightly different to before
- (Optional) Generate testing artefacts, as done before in the earlier steps.
- (Optional) Merge the generated testing artefacts with the ground truth dataset
- (Optional) Use this new evaluation dataset for the remaining steps. Alternatively, use the same evaluation dataset used in previous steps.

## Instructions for Local Development

- Open the Jupyter Notebook ("6.1-evaluating-changes-to-a-genai-application.ipynb") and run the cell.

After running the code cell, complete the following steps in Azure AI Studio.

- Open the Evaluations section in the sidebar. Ensure "Show Batch Runs" is toggled on.
- You should see your evaluation flow.

![Example Image](Images/AzureAIStudioLogging.png)

TBC