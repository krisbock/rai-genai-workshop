####

# Prerequisites

For this tutorial, we will be using the Azure AI SDK (which is currently in preview).  Follow the instructions in the link below to install the SDK.  You can either install the SDK into an existing development environment, or run it via an internet browser or Docker container by using VS Code (web) in Azure AI Studio, Visual Studio Code Dev Container, or GitHub Codespaces.

https://learn.microsoft.com/en-us/azure/ai-studio/how-to/sdk-install?tabs=linux

packages
pip install promptflow-rag
pip install azure-ai-ml -U

.env
AZURE_SUBSCRIPTION_ID=<your Azure subscription ID>
AZURE_RESOURCE_GROUP=<your Azure resource group that has the AI Studio>
AZUREAI_PROJECT_NAME=<your Azure AI Studio project name>
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=<your Azure OpenAI embedding deployment>
AZURE_OPENAI_CONNECTION_NAME=<the Azure OpenAI connection defined in AI Studio>    
AZURE_SEARCH_ENDPOINT=<your Azure Search endpoint>
AZURE_SEARCH_CONNECTION_NAME=<the Azure Search connection name defined in AI Studio>

Roles required

Azure OpenAI Service
Cognitive Services OpenAI User

_AI Search_
Search Index Data Contributor
Search Service Contributor
