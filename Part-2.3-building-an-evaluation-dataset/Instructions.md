# Building an evaluation dataset

## Overview

An evaluation dataset is made up of two parts:
- The ground truth labels: "what should the application have done?"
- The logged artefacts: "what did the application do?"

By combining these into a single dataset, they can be evaluated to see how the application is performing.

## Instructions

In this step, a CSV will be created following a set template.

The headings used in the template are important, as they will allow the columns to be automatically mapped to the right input. This can be done when running the evaluation manually, but this approach is much simpler to manage.

#### _If you are using the tutorial's dataset:_

The datasets created in the earlier steps should be combined. An example template CSV is included in this step, to show what the output should look like. 

Examine the input data and the resulting output data to see how this has been done. This can be achieved simply through copy pasting in Excel.

#### _If you are using a custom dataset:_

Duplicate the CSV contained in the output folder for this step. Use the same column headings, and paste in the ground truth and logged artefacts from your own GenAI application.

Most RAG applications will already provide a function for logging the question and answer from an application. This is sufficient for simple LLM evaluation metrics. 

However, for more advanced evaluation metrics, additional intermediate artefacts from the application will need to be logged, such as the context that was retrieved, and if multiple tools are available, which tool was selected. This may require the application code to be modified to allow these interim data points to be logged.

Whilst this may incur additional effort, the benefit is that the LLM evaluation framework is completely decoupled from the application- any application, whether it is built in LangChain, PromptFlow or directly in code, can be evaluated by this approach.