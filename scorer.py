def judge(question: str, expects: str, answer: str, results) -> bool:
    if not expects:
        return False 
    answer_str = str(answer)
    return expects.strip().lower() in answer_str.lower()
