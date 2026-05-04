def ask_gemma(prompt):

    res = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma",
            "prompt": prompt,
            "stream": False
        }
    )

    return res.json()["response"]