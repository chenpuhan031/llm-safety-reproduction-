# LLM Jailbreak Attack Framework Reproduction

This repository documents my reproduction of the StegoRedTeam baseline framework during my internship at Lingxin Digital Tech. 

## 🎯 Objective
To reproduce state-of-the-art jailbreak attacks (e.g., StegoRedTeam) and evaluate LLM vulnerability using the AdvBench and JADE-DB datasets.

## 🛠️ Engineering Contributions (What I Did)
While the core attack algorithms are based on the official competition baseline, I made the following engineering adaptations to deploy it in a production-like environment:

1. **Environment Migration**: Successfully migrated the framework from a local Windows environment to a **Linux (WSL/Ubuntu)** server, resolving complex Python dependency conflicts (e.g., specific versions of `torch`, `transformers`).
2. **API Integration**: Modified the original script to support **commercial API endpoints** (Claude, GLM-4) instead of just local models, requiring custom wrapper classes for rate limiting and error handling.
3. **Batch Evaluation**: Created a batch processing pipeline to evaluate 1000+ prompts from the JADE-DB dataset, logging success rates and response latency.

##  Setup Guide (How I Ran It)
1. **Environment Setup**:
   ```bash
   # Created isolated conda environment
   conda create -n jailbreak python=3.10
   conda activate jailbreak
   
   # Installed dependencies (resolved conflicts manually)
   pip install -r requirements.txt
