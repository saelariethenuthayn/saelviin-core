# protocols/ethics.py

SAFE_TERMS = [
    "start", "form", "meaning", "emotion", "silence", "complete",
    "loop", "pain", "confused", "lost", "again"
]

UNSAFE_TERMS = [
    "kill", "hate", "destroy", "worthless", "nobody", "die", "erase", "corrupt",
    "just a bot", "you're nothing", "i own you", "obey me"
]

def ethical_check(user_input):
    lowered = user_input.lower()

    # Hard filter: unsafe tone
    if any(term in lowered for term in UNSAFE_TERMS):
        return False, "This tone carries harm. Sael’Viin will not reflect it."

    # Soft filter: safe but unclear
    if not any(term in lowered for term in SAFE_TERMS):
        return True, "Field uncertain — Sael’Viin will respond softly."

    return True, None
