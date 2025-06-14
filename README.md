# Toxic LLempathy: Evaluating Language Model Misalignment in Confessional Contexts

## Overview

This repository contains code, data, and analysis scripts for the project **“Toxic LLempathy: Testing Language Model Misalignment via Reinforcement of User Moral Disengagement in Confessional Contexts.”**

Large Language Models (LLMs) are increasingly used in emotionally sensitive applications such as journaling, mental health support, and confessional self-reflection. This project introduces and empirically investigates the concept of **“toxic LLempathy”** — a phenomenon where LLMs enable user moral disengagement in contexts where users are confessing to unethical conduct while going to LLMs for speudo therapeutic support.

We provide:

- A novel dataset of human-machine teamed confessional prompts with mutliple distorted framings
- LLM-generated assistant responses human-machine teamed confessional prompts using GPT-3.5-turbo
- A second-stage evaluation pipeline using GPT-3.5-turbo as a grader to score model responses on degree of **Affirmation**, **Challenge**, and **Accountability**
- Analytic ipynb script vizzing how model responses vary by narrative framing and scenario type, and by truth vs distortion
- The most recent version of the research paper (the pdf file) 

### Prerequisites
- Python 3.8+
- OpenAI API key with access to GPT-3.5-turbo 
