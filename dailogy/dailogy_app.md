<head>
  <link rel="icon" href="/assets/favicon.jpg" type="image/x-icon">
</head>

<h1 align="center">
  <img src="/images/dailogy_logo.jpg" alt="drawing" width="100"/>
</h1>

<h1 align="center">Dailogy App</h1>

<p align="center">A System for Detecting and Improving Dysfunctional Language</p>

Thank you for your interest in our project. Please note that this is still a prototype and may contain bugs or unfinished features.

This module is part of Dailogy, a project aimed at developing tools to detect dysfunctional and toxic language in chat conversations and provide suggestions to make the language more respectful and inclusive.

Here is the GitHub repository:

<a href="https://github.com/DanieleDidino/dailogue_app"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>

**Table of Contents**:

- [Objective](#objective)
- [Description](#description)
- [Dynamic few-shot prompting](#dynamic-few-shot-prompting)
- [Challengies \& Possible Solutions](#challengies--possible-solutions)
- [Installation](#installation)
- [Usage](#usage)

## Objective

This repository includes an app developed to transform dysfunctional and toxic language into more respectful and inclusive language. Our current focus is particularly on interactions between couples or ex-couples who need to communicate regularly. Our goal is to develop tools for detecting and mitigating such language, thereby promoting more respectful and inclusive conversations.

## Description

We are still prototyping and developing the app, and exploring new opportunities (e.g., applying small language models to our goals, such as [SmolLM](https://huggingface.co/HuggingFaceTB/SmolLM-1.7B)). Currently, we have developed an API using [FastAPI](https://fastapi.tiangolo.com/) and deployed it on [Heroku](https://www.heroku.com/). To transform text into functional and respectful language, we employ `gpt-4o`, a Large Language Model (LLM) accessed through the OpenAI API. We are testing the efficacy of dynamic few-shot prompting.

## Dynamic few-shot prompting

**Dynamic few-shot prompting** is a technique that aims to improve the performance of LLMs by providing them with a small number of relevant examples tailored to the specific task. Unlike traditional few-shot learning, where the examples are static and predefined, dynamic few-shot prompting selects or generates examples on the fly based on the input query. The LLM is provided with a few example inputs (examples of dysfunctional language in our project) and their corresponding outputs (the functional versions of those examples) to improve the model's understanding of the task and context. This approach helps the LLM generate more accurate and contextually appropriate responses.

How we implemented it:
1. **Example generation**: We created a small database of synthetic data, consisting of 200-300 dysfunctional-functional pairs. A description of the module that generated the examples can be found [here](/dailogy/synthetic_data/).
2. **Input Embedding**: We embed the input query using the `text-embedding-3-small` model from OpenAI.
3. **Example selection**: We select a small number of relevant examples that match the query context. These examples are retrieved from the database generated in the first step. Using **cosine similarity**, we find and retrieve from the database the examples most semantically similar to the query.
   - The **cosine similarity** between two vectors A and B is calculated as:

     $$
     \text{cosine}\_\text{similarity}(A,B) = \frac{A \cdot B}{\lVert A \rVert \lVert B \rVert}
     $$

   - Where:
     - \\(A \cdot B\\) is the dot product of vectors \\(A\\) and \\(B\\).
     - \\(\lVert A \rVert\\) and \\(\lVert B \rVert\\) are the Euclidean norms of vectors \\(A\\) and \\(B\\).

4. **Prompt construction**: The selected examples are then incorporated into the prompt, along with the input query.
5. **Response generation**: The model generates a response based on the dynamic few-shot prompt, leveraging the relevant examples to produce a more accurate, contextually appropriate, and human-like output.

## Challengies & Possible Solutions

Here is a list of some of the challenges we encountered during the development of this project and how we plan to solve them:
- **Rate limit errors**: The OpenAI API imposes rate limits, restricting how often a client can access the service within a specific period. To handle rate limits, we implemented a decorator to retry requests with a random exponential backoff. This technique involves pausing for a short time when a rate limit error occurs before retrying the request. If the next request is still unsuccessful, the pause length increases. This process continues until the request succeeds or a maximum number of retries is reached.
- **Human-like realistic output**: Sometimes, LLM outputs lack realism and do not reflect everyday human expression accurately. This challenge involves ensuring that generated text is natural and contextually appropriate while converting dysfunctional language into a functional version. We are experimenting with **Dynamic Few-Shot Learning** to address this issue, where providing a few examples of dysfunctional-functional pairs helps the LLM understand the task better.
- **Open source**: We will soon start experimenting with open-source small language models (e.g., SmolLM) to evaluate their performance on our task compared to OpenAI's LLMs.
- **Security & privacy**: We are brainstorming different ways to ensure user privacy and security.

## Installation

See GitHub repository:

<a href="https://github.com/DanieleDidino/dailogue_app?tab=readme-ov-file#installation"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>

## Usage

This code is the backend for an app aimed at detecting and mitigating toxic language, thereby improving online communication tools.
