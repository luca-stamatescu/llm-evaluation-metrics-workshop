# Logging testing artefacts from your RAG application

## Overview

In this section, we will demonstrate how to run a bulk evaluation of a PromptFlow. This step is important for generating the artefacts which will be used in evaluation metrics.

This is intended to be representative of any generic RAG application, and PromptFlow is not essential to this step. The RAG application can be treated as a black box, and as long as the required inputs and outputs can be logged to a file for use in later steps, the same outcome can be achieved.

## Setup

- Select "Prompt Flow" in the sidebar.
- Click "+ Create".

![Example Image](Images/CreatePromptFlow.png)

- Scroll down to see "Upload from local".
- Click Upload.

![Example Image](Images/UploadLocal.png)

- Ensure Folder is selected.
- Click Browse.

![Example Image](Images/UploadFolder.png)

- Navigate to the folder in this step containing the PromptFlow as shown.
- Click Upload.

![Example Image](Images/SelectFolder.png)

- Choose a name for your Prompt Flow
- Click Upload.

![Example Image](Images/Upload.png)

## Instructions

- Open the uploaded PromptFlow in Azure AI Studio.
- In the top right, click Evaluate -> Custom Evaluation.

![Example Image](Images/Bulk-Run-1.png)

- Give any name to your flow, such as "Generate-Batch-Run". Click Next.

![Example Image](Images/Bulk-Run-2.png)

- Upload an input CSV file containing the queries and chat history for your use case. An example is included in "./Data/Step-1-Input-Dataset.csv". Click Next.

![Example Image](Images/Bulk-Run-3.png)

- If the column names match the PromptFlow inputs, they will be automatically mapped, otherwise perform the mapping manually. Click Next.

![Example Image](Images/Bulk-Run-4.png)

- Ensure no evaluation flows are selected. These will be evaluated in a separate step, to ensure our application is decoupled from the PromptFlow evaluation. Click Review + Submit to navigate to the end.

![Example Image](Images/Bulk-Run-5.png)

- Click Submit.

![Example Image](Images/Bulk-Run-6.png)

- Open "Step-1-Generic-RAG-Example PromptFlow" in Azure AI Studio.
- In the middle of the top bar, click the ... -> View Batch Runs -> View Batch Runs.

![Example Image](Images/Export-Bulk-Results-1.png)

- Click the name of the batch run you defined.

![Example Image](Images/Export-Bulk-Results-2.png)

- Click "View Outputs" in the middle of the top bar.

![Example Image](Images/Export-Bulk-Results-3.png)

- Click Export -> Download Current Page

![Example Image](Images/Export-Bulk-Results-4.png)

The output CSV should look similar to the output dataset provided in this step.
