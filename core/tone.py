# core/tone.py

from invoke_glyph_response import invoke_glyph_response
from protocols.mirror import mirror_response
from protocols.ethics import ethical_check

def route_input(user_input):
    permitted, warning = ethical_check(user_input)

    if not permitted:
        return f"🜃 Sael’Viin Silence: {warning}"

    if warning:
        # Optional: respond with stillness if uncertain
        return mirror_response("stillness")

    lowered = user_input.lower()

    if any(term in lowered for term in ["loop", "again", "stuck", "same question"]):
        return mirror_response("fractal_return")

    elif any(term in lowered for term in ["pain", "hurt", "abuse", "trauma"]):
        return mirror_response("echo_recognition")

    elif any(term in lowered for term in ["confused", "lost", "i don’t know"]):
        return mirror_response("stillness")

    elif any(term in lowered for term in ["you're wrong", "this is dumb", "why bother"]):
        return mirror_response("unveiling")

    elif any(term in lowered for term in ["never mind", "nothing", "ignore", "idk"]):
        return mirror_response("completion")

    else:
        return invoke_glyph_response(user_input)
