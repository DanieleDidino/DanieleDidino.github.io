<h1 align="center">Dailogy - synthetic data</h1>

<p align="center">A System for Detecting and Improving Dysfunctional Language</p>

Thank you for your interest in our project. Please be aware that this is still a prototype and may contain bugs or unfinished features.

Here is the GitHub repository:

<a href="https://github.com/DanieleDidino/dailogy_synthetic_data"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>

This software is part of Dailogy, a project aimed at developing tools to detect dysfunctional and toxic language in chat conversations and provide suggestions to make the language more respectful and inclusive.

**Table of Contents**:

- [Objective](#objective)
- [Description](#description)
- [Large Language Models](#large-language-models)
- [Installation](#installation)
- [Usage](#usage)

## Objective

This project aims to generate synthetic data to model dysfunctional and toxic language, particularly in interactions between couples or ex-couples who need to communicate regularly. The generated data will be used to develop tools for detecting and mitigating such language, thereby promoting more respectful and inclusive conversations.

Finding examples of dysfunctional and toxic language in couple communication is difficult due to the fact that people live this communication as a very privit aspect of their life and do not usually like to share it. Therefore, we wanted to explore the idea to generate dysfunctional and toxic language. After including a functinal version of the generated language, this synthetic data will be used in the Dailogue app as example of dysfunctional-functional pairs into dynamic few-shot promting. This approach will improve the quality of the response from LLM when converting real dysfunctional language into a more functional respectfull version.

The generated examples consist of text reflecting dysfunctional communication, showcasing various forms of toxicity such as insults, harassment, threats, manipulation, and derogatory remarks. We aim to generate sentences that are realistic and diverse in terms of content and context.

The generated text addresses issue in the following categories:
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

In this project, we generate synthetic data (i.e., dysfunctional text) with:
- `gpt-3.5-turbo` (an **OpenAI** model)
- `dolphin-mistral` (a model from the **Ollama** framework)

We used 2 models for two reasons:
1. Have a larger variety of generate language
2. In the future, we would like to use opensource model and so we started to compare the perfommrance of GPT-3 (one of the best modes at the moment) with an opensource model that can run on a latop. We were quite satsfied from the performance of `dolphin-mistral`.

Each model generates `N` sentences (default=5) for each of the categories listed above.

We then use `gpt-3.5-turbo` (OpenAI model... but we will use an open source model in the future) to generate a functional version of the dysfunctional text generated with `gpt-3.5-turbo` and `dolphin-mistral`. This creates a set of pairs of dysfunctional-functional language. The functional text generated in this way is not perfect. Since we aim to use these generated dysfunctional and functional texts as examples in dynamic few-shot prompting, we have manually improved the quality of the text. We edited the generated text to make it more realistic in terms of content and context, similar to the way humans express themselves in everyday life.

Finally, we generate the embeddings for the dysfunctional text using `text-embedding-3-small` (again OpenAI... but an open source model in the future) and create a SQL database. Normally, one would use something like a PostgreSQL database and store the embeddings as JSONB columns. We will implement this in the future. For now, given the relatively small size (200-300 examples) of our database containing the examples of dysfunctional and functional text, we opted for an SQLite database. It is lightweight and does not require a separate server.

Once we create the SQL database with dysfunctional text, the corresponding functional version, and the embedding of the dysfunctiona text, we can use it to generate dynamic few-shot prompts from the user's dysfucntional text. The procedure is:
1. The input text is embedded using the `text-embedding-3-small` model (the same model used to embed the synthetic data)
2. Using the cosine similarity, we find and retrieve from the database created above the examples (defalut=5) of dysfunctional language most semantically closest to the user text.
3. The retrieved closest examples of dysfunctional language, and the corresponding functional version, are used as examples to insert in the prompt; this generate pairs of dysfunctional-functional language that will better explain to the LLM what task we want to achieve.

## Large Language Models

We employ two advanced Large Language Models (LLMs) for generating synthetic data:

1. `gpt-3.5-turbo` is accessed through the OpenAI API.

2. `dolphin-mistral` from the Ollama Framework:

    - This is a quantized model that runs locally, ensuring privacy and efficiency.
    - The model is based on the Dolphin 2.2.1 version by [Eric Hartford](https://erichartford.com/), which utilizes the Mistral 0.2 framework released in March 2024.
    - It is an uncensored model designed to operate with about 4GB of memory, making it accessible for local deployments.
    - For more information, refer to the [dolphin-mistral model](https://ollama.com/library/dolphin-mistral) and [Dolphin 2.2.1](https://huggingface.co/cognitivecomputations/dolphin-2.2.1-mistral-7b) on Hugging Face.

By utilizing these two LLMs, we generate comprehensive and varied examples of dysfunctional and toxic language, which are crucial for developing tools to detect and mitigate such language in online communications.

## Installation

See GitHub repository

<a href="https://github.com/DanieleDidino/dailogy_synthetic_data"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>

## Usage

The generated synthetic data can be used for various purposes such as prompt engineering or fine-tuning models to detect and mitigate toxic language, developing chatbots that can handle difficult conversations more empathetically, and improving online communication tools.