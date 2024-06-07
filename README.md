# llm-evaluation-metrics-workshop

Azure AI Studio contains a powerful set of tools and capabilities for evaluating the performance of GenAI applications. This repository provides a simple, worked example to help translate theory into practice. This repository can be used as a template to build your own evaluation flows on top of.

##  Preparation

The following resources are required to complete this workshop:
- Azure AI Studio
- Azure OpenAI*

*note that access to Azure OpenAI requires approval through the gating process, which may take a few days.

## Pathways

There are two pathways to complete this workshop.

1) If you do not have your own existing GenAI application, and are looking to learn more about LLM Evaluation, start at Part-2.1-collecting-ground-truth-labels. You will start from the very beginning, and leverage an included, simple RAG application to generate your dataset.
2) If you already have an existing GenAI application, and wish to leverage your own dataset, skip to Part-2.3-building-an-evaluation-dataset. You may wish to review Part-2.1 and Part-2.2 to understand how the dataset inputs are collected.

For both pathways, you are encouraged to review the optional material in Part-1.

## Part 1 - Education

An overview of the LLM evaluation process is included, to help explain the key concepts and underlying theory.

## Part 1 - (Optional) Generating artefacts for evaluation

This step is optional, in order to create a dataset for evaluation which contains all the logged artefacts that are needed.

If you have an existing GenAI application, you should set up logging to create a dataset following the same structure as Step-2-Input-Dataset.

## Part 2 - Evaluation

In this step, Prompt Flow is used to evaluate the GenAI application.