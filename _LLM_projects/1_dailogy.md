---
title: "<div class='center-title'>Dailogy App <br/></div>"
excerpt: "A System for Detecting and Improving Dysfunctional Language.<br/><img src='/images/chatbot_afa_2.png'>"
collection: LLM_projects
---

<h1 align="center">
<img src="/images/dailogy_logo.jpg" alt="drawing" width="300"/>
</h1>

A System for Detecting and Improving Dysfunctional Language

<style>
  div {text-align: center;}
</style>

## Description

Thank you for your interest in our project. Please be aware that this is still a prototype and may contain bugs or unfinished features.

Dailogy is a project aimed at developing tools to detect dysfunctional and toxic language in chat conversations and provide suggestions to make the language more respectful and inclusive.

This project includes:
- Synthetic data

## Retrieval-Augmented Generation (RAG)

**RAG** enhances the performance of a Large Language Model (LLM). It does so by providing an additional, external knowledge base that extends beyond the LLM's original training data. This supplementary information is integrated into the LLM's process before it generates a response, enabling it to produce more informed and accurate outputs.

The RAG pipeline consists of the following steps:

1. **Vector DB**:<br>
For the construction of the knowledge base, specifically the embeddings for the Agentur für Arbeit (AfA) documents, we utilized OpenAI's “**text-embedding-ada-002**” model. The process involves breaking down the documents into smaller segments (chunks), which are then parsed into nodes. These nodes not only store the text data but also maintain metadata and relational information. The resulting data is stored in a LlamaIndex’s Vector Store. We then save these vector embeddings to disk for efficient retrieval.

2. **Hypothetical Document Embeddings (HyDE)** [[link](https://arxiv.org/abs/2212.10496)]:<br>
With HyDE, a user's query is processed by a Large Language Model (in this case, “**gpt-3.5-turbo**”) to generate a Hypothetical Document. This hypothetical document, while inaccurate, is designed to closely resemble the kind of documents that should ideally be retrieved from our knowledge base. This hypothetical document can enhance the retrieval process from the vector database, potentially outperforming direct queries from users.

3. **Retrieval**:<br>
The system retrieves the top-k (here 5) relevant items from the vector database. This is achieved by calculating the cosine similarity between the embeddings of the Hypothetical Document and those in the knowledge base. Such a method enhances the relevance and accuracy of the information retrieved.

4. **Response generation**:<br>
In the final step, the context obtained from the retrieved documents is combined with the original user query. This combined input (prompt) is then fed into an LLM (here, “**gpt-3.5-turbo**”) for response generation. This process enables the LLM to produce responses that are contextually relevant, leveraging both the query and the retrieved document information. Additionally, the chatbot provides the source details (i.e., the title and page) of the top-k retrieved items, along with their respective cosine similarity scores.

<p align="center">
<img src="/images/chatbot_afa_RAG_pipeline.png" alt="drawing" width="500"/>
<br>RAG pipeline
</p>
