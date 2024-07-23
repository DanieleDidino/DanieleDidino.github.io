<h1 align="center">Dailogy - Synthetic Data</h1>

<p align="center">A System for Detecting and Improving Dysfunctional Language</p>

<h1 align="center">
  <img src="/images/dailogy_logo.jpg" alt="drawing" width="100"/>
</h1>

Thank you for your interest in our project. Please note that this is still a prototype and may contain bugs or unfinished features.

This software is part of Dailogy, a project aimed at developing tools to detect dysfunctional and toxic language in chat conversations and provide suggestions to make the language more respectful and inclusive.

Here is the GitHub repository:

<a href="https://github.com/DanieleDidino/dailogy_synthetic_data"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>

**Table of Contents**:

- [Objective](#objective)
- [Description](#description)
- [Large Language Models](#large-language-models)
- [Installation](#installation)
- [Usage](#usage)

## Objective

This project aims to generate synthetic data to model dysfunctional and toxic language, particularly in interactions between couples or ex-couples who need to communicate regularly. The generated data will be used to develop tools for detecting and mitigating such language, thereby promoting more respectful and inclusive conversations.

Finding examples of dysfunctional and toxic language in couple communication is challenging due to the private nature of these interactions. Therefore, we have explored generating synthetic examples of such language. After generating also a functional version of these examples, this synthetic data will be used in the Dailogy app as examples of dysfunctional-functional pairs in **dynamic few-shot prompting**. This approach will improve the quality of the responses from large language models (LLMs) when converting real dysfunctional language into more functional, respectful versions.

The generated examples consist of text reflecting dysfunctional communication, showcasing various forms of toxicity such as insults, harassment, threats, manipulation, and derogatory remarks. We aim to generate sentences that are realistic and diverse in terms of content and context.

The generated text addresses issues in the following categories:
- Financial disagreements (e.g., spending habits, debt, child support payments).
- Division of household responsibilities (e.g., chores, maintenance).
- Communication breakdowns (e.g., lack of communication, misunderstandings).
- Trust issues (e.g., infidelity, suspicion, jealousy).
- Differences in parenting styles or decisions.
- Time management and scheduling conflicts (e.g., visitation schedules, personal time).
- Personal boundaries and respect for privacy.
- Extended family involvement (e.g., in-laws, family obligations).
- Social life and friendships (e.g., differing social circles, time spent with friends).
- Emotional support and empathy (e.g., lack of emotional support, neglect).
- Career or job-related stress and decisions.
- Relocation or living arrangements (e.g., moving cities, living apart).
- Health and wellness issues (e.g., disagreements about medical decisions, lifestyle choices).
- Substance abuse or addiction problems.
- Legal issues (e.g., divorce proceedings, custody battles).
- Shared custody of children.
- Differing future goals and aspirations.
- Handling of past conflicts and unresolved issues.
- Intimacy and sexual compatibility.
- Vacations and leisure activities (e.g., differing interests, planning conflicts).
- Child discipline and education decisions.
- School-related issues (e.g., homework, school performance, educational decisions)
- Medications and child health (e.g., medical treatments, health care decisions)
- Eating habits and nutrition (e.g., diet, meal planning, nutritional disagreements)

## Description

In this project, we generate synthetic data (i.e., dysfunctional-functional pairs) using:

- `gpt-3.5-turbo` (an **OpenAI** model)
- `dolphin-mistral` (a model from the **Ollama** framework)

We used two models for two reasons:

1. To have a larger variety of generated language
2. To compare the performance of GPT-3.5 (one of the best models at the moment) with an open-source model that can run on a laptop. We were quite satisfied with the performance of `dolphin-mistral`.

Each model generates `N` sentences (default = 5) for each of the categories listed above.

We then use `gpt-3.5-turbo` (OpenAI model) to generate a functional version of the dysfunctional text generated with `gpt-3.5-turbo` and `dolphin-mistral`. This creates a set of pairs of dysfunctional-functional language. The functional text generated in this way is not perfect. Since we aim to use these generated texts as examples in dynamic few-shot prompting, we have manually improved the quality of the text to make it more realistic in terms of content and context, similar to the way humans express themselves in everyday life.

Finally, we generate embeddings for the dysfunctional text using `text-embedding-3-small `(OpenAI model) and create a SQL database. Normally, one would use a PostgreSQL database and store the embeddings as JSONB columns. We will implement this in the future. For now, given the relatively small size (200-300 examples) of our database containing examples of dysfunctional and functional text, we opted for an SQLite database. It is lightweight and does not require a separate server.

Once we create the SQL database with dysfunctional text, the corresponding functional version, and the embedding of the dysfunctional text, we can use it to generate **dynamic few-shot prompts** from the user's dysfunctional text. The procedure is:
1. The input text is embedded using the `text-embedding-3-small` model (the same model used to embed the synthetic data).
2. Using cosine similarity, we find and retrieve from the database the examples (default = 5) of dysfunctional language most semantically closest to the user text.
3. The retrieved closest examples of dysfunctional language, and their corresponding functional versions, are used as examples in the prompt to generate pairs of dysfunctional-functional language that will better explain to the LLM the task we want to achieve.

## Large Language Models

We employ two advanced Large Language Models (LLMs) for generating synthetic data:

1. `gpt-3.5-turbo` is accessed through the OpenAI API.
2. `dolphin-mistral` from the Ollama Framework:
    - This is a quantized model that runs locally, ensuring privacy and efficiency. The model is based on the Dolphin 2.2.1 version by [Eric Hartford](https://erichartford.com/), which utilizes the Mistral 0.2 framework released in March 2024. It is an uncensored model designed to operate with about 4GB of memory, making it accessible for local deployments. For more information, refer to the [dolphin-mistral model](https://ollama.com/library/dolphin-mistral) and [Dolphin 2.2.1](https://huggingface.co/cognitivecomputations/dolphin-2.2.1-mistral-7b) on Hugging Face.

By utilizing these two LLMs, we generate comprehensive and varied examples of dysfunctional and toxic language, which are crucial for developing tools to detect and mitigate such language in online communications.

## Installation

See GitHub repository

<a href="https://github.com/DanieleDidino/dailogy_synthetic_data"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>

## Usage

The generated synthetic data can be used for various purposes, such as prompt engineering, fine-tuning models to detect and mitigate toxic language, developing chatbots that can handle difficult conversations more empathetically, and improving online communication tools.
