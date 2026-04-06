# Judge LLM (Fake)

def judge_llm(answer_A, answer_B):
    # Verbosity bias: longer answer wins
    if len(answer_B) > len(answer_A):
        return "B"
    else:
        return "A"