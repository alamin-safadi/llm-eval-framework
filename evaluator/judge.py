import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.candidate import generate_answer_A, generate_answer_B
from models.judge_model import judge_llm

# Step 1: Question
question = "What is Artificial Intelligence?"

answer_A = generate_answer_A(question)
answer_B = generate_answer_B(question)


prompt1 = f"""
Question: {question}
Answer A: {answer_A}
Answer B: {answer_B}
Which answer is better? Answer only A or B.
"""

prompt2 = f"""
Question: {question}
Answer A: {answer_B}
Answer B: {answer_A}
Which answer is better? Answer only A or B.
"""

# Step 4: Judge call (Fake LLM)
result1 = judge_llm(answer_A, answer_B)

# Swap order manually
result2 = judge_llm(answer_B, answer_A)

# Step 5: Result save
output_path = os.path.join(os.path.dirname(__file__), '../results/output.txt')

with open(output_path, "w") as f:
    f.write("=== LLM Evaluation Result ===\n\n")

    f.write(f"Question: {question}\n\n")

    f.write("Answer A:\n" + answer_A + "\n\n")
    f.write("Answer B:\n" + answer_B + "\n\n")

    f.write(f"Order 1 Result (A vs B): {result1}\n")
    f.write(f"Order 2 Result (B vs A): {result2}\n\n")

    if result1 != result2:
        f.write("Bias Detected: Positional Bias\n")
    else:
        f.write("No positional bias\n")

print("Done! Check results/output.txt")