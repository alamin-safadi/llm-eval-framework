# LLM Evaluation Framework (Bias Detection)

## Overview
This project demonstrates how LLM-as-a-Judge works and how bias can occur.

## Features
- Candidate LLM generates answers
- Judge LLM evaluates answers
- Detects:
  - Positional Bias
  - Verbosity Bias

## How it Works
1. Generate two answers (A & B)
2. Ask judge which is better
3. Swap order
4. Compare results

## Output
Results are saved in results/output.txt

## Conclusion
LLMs can show bias and are not always reliable judges.