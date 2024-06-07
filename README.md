# llm-evaluation-metrics-workshop

Azure AI Studio contains a powerful set of tools and capabilities for evaluating the performance of GenAI applications. This repository provides a simple, worked example to help translate theory into practice. This repository can be used as a template to build your own evaluation flows on top of.

##  Preparation

The following resources are required to complete this workshop:
- Azure AI Studio
- Azure OpenAI*

*note that access to Azure OpenAI requires approval through the gating process, which may take a few days.

## Pathways

There are two pathways to complete this workshop.

1) If you do not have your own existing GenAI application, and are looking to learn more about LLM Evaluation, start at _Part-2.1-collecting-ground-truth-labels_. You will start from the very beginning, and leverage an included, simple RAG application to generate your dataset.
2) If you already have an existing GenAI application, and wish to leverage your own dataset, skip to _Part-2.3-building-an-evaluation-dataset_. You may wish to review Part-2.1 and Part-2.2 to understand how the dataset inputs are collected.

For both pathways, you are encouraged to review the optional material in Part-1.

## Part 1 - Education

An overview of the LLM evaluation process is included, to help explain the key concepts and underlying theory.

## Part 2 - Build an evaluation dataset

Learn how an evaluation dataset is constructed, and build your own leveraging a provided RAG application. Alternatively, bring your own dataset created from your own GenAI application.

## Part 3 - Out-of-the-Box evaluation with Azure AI Studio

Leverage Azure AI Studio's powerful LLM evaluation capabilities

## Part 4 - Build custom evaluation metrics with PromptFlow and Azure AI Studio

Go further, and build advanced LLM evaluation metrics for your application.


## Future work
The following topics are not covered in this tutorial.

- CICD: how to implement a code first approach to leveraging Azure AI Studio.
- Few shot prompting: Customize the evaluation metrics with few shot prompts tailored to your use case.
- Other scenarios: testing for other harms or failure scenarios such as offensive content, jailbreaking attacks or unexpected inputs.