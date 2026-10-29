# LLM Jailbreak Attack & Evaluation Framework Reproduction

This repository documents my engineering reproduction of an LLM safety evaluation framework (based on StegoRedTeam and LLM-as-a-Judge methodologies) during my internship at Lingxin Digital Tech.

## 🎯 Objective
To build a localized, automated pipeline for evaluating LLM vulnerability against steganographic jailbreak attacks, using commercial APIs (Claude/GLM-4) and an LLM-based evaluator.

## 🛠️ Engineering Contributions (What I Did)
While the core attack algorithms are based on open-source baselines, I engineered the following components for production deployment:

1. **Environment Migration**: Migrated the framework from Windows to **Linux (WSL/Ubuntu)**, resolving Python dependency conflicts (e.g., `torch`, `transformers` versions).
2. **API Integration**: Modified the original script to support **OpenAI-compatible commercial APIs** (Claude, GLM-4), implementing custom wrapper classes for rate limiting and error handling.
3. **Automated Evaluation Pipeline**: Implemented an **LLM-as-a-Judge** system (see `llm_judge_evaluator.py`) to automatically score jailbreak success rates across large datasets (e.g., JADE-DB).
4. **Batch Processing**: Created a batch runner to process 500+ prompts, logging success rates and saving results to CSV.

## 📂 Repository Structure
- `config_template.py`: API configuration template for Target, Evaluator, and Helper models.
- `llm_judge_evaluator.py`: The automated evaluation script using LLM-as-a-Judge (safe for public sharing).
- `sample_results.csv`: Sample output from a test run (10 samples).

## ⚠️ Note on Code Availability
- **Attack Prompts**: The specific steganographic attack prompts (e.g., "RedTeam_Steganalysis_AI") are **omitted** to comply with corporate NDA and safety policies.
- **Datasets**: Internal datasets are excluded. This repo uses public dataset structures (AdvBench/JADE-DB) for demonstration.

##  How to Run (Evaluation Pipeline)
1. **Setup**:
   ```bash
   conda create -n safety python=3.10
   pip install openai pandas tqdm
