# llm-evaluation-metrics-workshop

Azure AI Studio contains a powerful set of tools and capabilities for evaluating the performance of GenAI applications. This repository provides a simple, worked example to help translate theory into practice. This repository can be used as a template to build your own evaluation flows on top of.

##  Preparation

The following resources are required to complete this workshop:
- Azure AI Studio
- Azure OpenAI*

*note that access to Azure OpenAI requires approval through the gating process, which may take a few days.

## Part 0 - Education

An overview of the LLM evaluation process is included, to help explain the key concepts and underlying theory.

## Part 1 - Generating artefacts for evaluation

This step is optional, in order to create a dataset for evaluation which contains all the logged artefacts that are needed.

If you have an existing GenAI application, you should set up logging to create a dataset following the same structure as Step-2-Input-Dataset.

## Part 2 - Evaluation

In this step, Prompt Flow is used to evaluate the GenAI application.