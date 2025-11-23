def ai_detector(text):
    """Simple AI content detector using basic pattern analysis.
    Return a score and verdict on whether text appears AI-generated."""
    text_lower = text.lower()
    ai_phrases = ["it is important to note",
        "it's worth nothing",
        "in conclusion",
        "in summary",
        "furthermore".
        "moreover",
        "additionally",
        "consequently",
        "delve into",
        "navigate",
        "landscape",
        "robust",
        "utilize",
        "leverage",
        "significant",
        "Furthermore",
        "Generally speaking",
        "Pivotal",
        "Intricate",]
    ai score = 0
    total checks = 0
    phrase count = 0
    for phrase in ai phrases:
        if phrase in text lower:
            phrase count += 1
    if phrase count >= 3:
        ai score += 30
    elif phrasse count >= 2:
        ai score += 20
    elif phrase count >= 1:
        ai score += 10
    total checks += 1
    sentences = text.replace('!', '.').replace('?', '.').split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    if len(sentences)>2:
        sentence lengths = [len(s.split()) for s in sentences]
        avg length = sum(sentence lengths) / len(sentence lengths)

    variance = sum((length - avg length) ** 2 for length in sentence lengths) / len(sentence lengths)
    if variance < 10:
        ai score += 20
    elif variance < 30:
        ai score += 10
    total checks += 1
    
    words = text lower.split()
    if len(words) > 10:
        long words = [w for w in words if len(w) > 8]
        long words ratio = len(long words) / len(words)
        if long word ratio > 0.2:
            ai score += 20
        elif long word ratio > 0.15:
            ai score += 10

        total checks += 1
    if len(sentences) > 3:
        first words = [s.split()[0].lower() for s in sentences if s.split()]
        unique first words = len(set(first words))
        if unique first words < len(first words) * 0.6:
            ai score += 15
        total checks += 1
    max possible score = 30 + 20 + 20 + 15
    normalized score = min(100, (ai score / max possible score) * 100)
    if normalized score >= 60:
        verdict = "Likely AI-generated"
    elif normalized score >= 40:
        verdict = "Possibly AI-generated"
    else:
        verdict = "Likely human-written"
    return normalized score, verdict
def main():
    print("AI Content Detector")
    print("=" * 50)
    print("Enter or paste text to analyse (type 'quit' to exit)")
    print("=" * 50)

    while True:
        print("\nEnter Text:")
        text = input()
        if text.lower() == 'quit':
            print("Exiting AI Detector. Goodbye!")
            break
        if len(text.strip()) < 20:
            print("Please enter at least 20 character for analysis.")
            continue
        score, verdict = ai detector(text)
        print(f"\n--- Analysis Results ---")
        print(f"AI Score: {score:.1f}/100")
        print(f"Verdict: {verdict}")
        print(f"---------------------")
if _name_ == "_main_":
    main()

        
