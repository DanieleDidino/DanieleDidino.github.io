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
- [Challengies \& possible solutions](#challengies--possible-solutions)
- [Installation](#installation)
- [Usage](#usage)

## Objective

This repository includes an app developed to transform dysfunctional and toxic language into more respectful and inclusive language.
Currently, our focus is particularly on interactions between couples or ex-couples who need to communicate regularly.
Our goal is to develop tools for detecting and mitigating such language, thereby promoting more respectful and inclusive conversations.

## Description

We are still prototyping and developing the app, and exploring new opportunities (e.g., apply small language models to our goals, such as [SmolLM](https://huggingface.co/HuggingFaceTB/SmolLM-1.7B)). Currently, we developed an API using [FastAPI](https://fastapi.tiangolo.com/) and deployed it on [Heroku](https://www.heroku.com/). To transform text into functional and respectful language, we employ `gpt-3.5-turbo`, a Large Language Model (LLM) accessed through the OpenAI API. We are testing the efficacy of dynamic few-shot prompting.

## Dynamic few-shot prompting

**Dynamic few-shot prompting** is a technique that aims to improve the performance of LLMs by providing them with a small number of relevant examples tailored to the specific task. Unlike traditional few-shot learning, where the examples are static and predefined, dynamic few-shot prompting selects or generates examples on the fly based on the input query. The LLM is provided with a few example inputs (examples of dysfunctional language in our project) and their corresponding outputs (the functional versions of those examples) to improve the model's understanding of the task and the context. This approach helps the LLM generate more accurate and contextually appropriate responses. 

How we implemented it:
1. **Example generation**: We generated a small database of examples, consisting of synthetic data consisting of 200/300 dysfunctional-functional pairs. A description of the module that generated the examples can be found [here](/dailogy/synthetic_data/).
2. **Input Embedding**: We embed the input query using the `text-embedding-3-small` model (from OpenAI).
3. **Example selection**: We select a small number of relevant examples that match the query context. These examples are retrieved from the database, generated at point 1. Using **cosine similarity**, we find and retrieve from the database the examples most semantically similar to the query.
   - The **cosine similarity** between two vectors A and B is calculated as:

     $$
     \text{cosine}\_\text{similarity}(A,B) = \frac{A \cdot B}{\lVert A \rVert \lVert B \rVert}
     $$

   - Where:
     - \\(A \cdot B\\) is the dot product of vectors \\(A\\) and \\(B\\).
     - \\(\lVert A \rVert\\) and \\(\lVert B \rVert\\) are the Euclidean norms of vectors \\(A\\) and \\(B\\).

4. **Prompt construction**: The selected examples are then incorporated into the prompt, along with the input query.
5. **Response generation**: The model generates a response based on the dynamic few-shot prompt, leveraging the relevant examples to produce a more accurate, contextually appropriate, and human-like output.

## Challengies & possible solutions

These is a list of some of the challenges we met during the development of this project and how we plan to solve them:

- **Rate limit errors**: OpenAI API imposes rate limits, that is restrictions on how often a client can access the API service. In other words, the number of times a client can access the service is limitted within a specific period of time. To deal with the rate limits, we used a decorator to implement retry requests with a random exponential backoff. This technique involves planning a short sleep when a rate limit error is hit before retrying the unsuccessful request. If the next request is still unsuccessful, the sleep length is increased. The process is repeated until the request is successful or until a maximum number of retries is reached.
- **Human-like realistic output**: The issue of LLM outputs sometimes lacking realism and not accurately reflecting everyday human expression is a well-known challenge in the field of natural language processing. Sometimes the output generated by LLMs does not align perfectly with human-like expressions or lacks contextual understanding, the nuance, or emotional aspects of a human expressions. Since we want to convert dysfunctional language into a more functional version but maintaining the generated text realistic and natural in term of content and context, it is important for us to obtain an output that is similar to the way humans express themselves in everyday life. To deal with this problem, we are experimenting with **Dynamic Few-Shot Learning**. Few-shot learning consists in providing a few examples of the desired input-output pairs can help the LLM better understand the task. In our project this consists of few examples of dysfunctinal-functional pairs. As described above, "dynamic" refers to the fact that the examples are selected based on the semantic similarity with the user's text.
- **Examples generation**: Dynamic few-shot prompting comes with the challenge to develop high-quality examples generation and selection methods. We will keep experimenting with different approaches.
- **Open source**: Soon we will start experimenting with small language model (e.g., [SmolLM](https://huggingface.co/HuggingFaceTB/SmolLM-1.7B)) to evaluate how they can perform well on our task compared to LLM.
- **Security & privacy**: We are brainstorming about different ways to garantee user's privacy and security. 

## Installation

See GitHub repository

<a href="https://github.com/DanieleDidino/dailogue_app?tab=readme-ov-file#installation"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>

## Usage

This code is the backend for an app aimed at detecting and mitigating toxic language, thus improving online communication tools.
