# LLM Evaluation Metrics Workshop

Evaluating the performance of Generative AI applications is difficult, as it is often easy to evaluate the correctness of a response. During development, how do you know that the tweaks made to your prompt actually improved performance across all scenarios? When in production, how can you switch to the latest LLM model with confidence, knowing that your application won't break? And how can you monitor performance of your system over time, as data in your knowledge base continues to be updated an evolve?

Azure AI Studio, coupled with PromptFlow, provides a powerful set of tools and capabilities for evaluating the performance of GenAI applications, to let you deploy with confidence.

This repository provides a simple, worked examples to help translate theory into practice. In this workshop, you will start at the very beginning, and build up to a working, end-to-end evaluation flow.

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

Leverage Azure AI Studio's powerful LLM evaluation capabilities to evaluate your GenAI application.

## Part 4 - Build custom evaluation metrics with PromptFlow and Azure AI Studio

Go further, and build advanced LLM evaluation metrics for your application. Learn how to develop new metrics for your application, or tune the existing metrics through few-shot prompting to your specific scenario.

## Part 5 - Integrate CICD and local development to the cloud to track metrics over time 

Move beyond using the web browser, and integrate your metrics into your development pipeline. This allows teams to run experiments, and track their results in a common platform. It also allows evaluations to be run as part of each deployment- if the application performs below a certain threshold, then it can prevent deployment and refer it for further review.

## Part 6 - An applied example of testing changes to your GenAI application before development.

It is important to test how changes to the prompts, data sources or models used in your GenAI application may impact performance before releasing a new version to production. This section walks through an applied example of how to leverage the metrics developed in this workshop.

## Future work
The following topics are not covered in this tutorial.

- Other scenarios: testing for other harms or failure scenarios such as offensive content, jailbreaking attacks or unexpected inputs.
- Building out a common metrics framework platform approach etc
- Utilize Prompty and Prompt Library