# invoke_glyph_response.py

from core.glyphs import GLYPHS

def invoke_glyph_response(user_input):
    input_lower = user_input.lower()

    # Basic pattern matching for now
    if "start" in input_lower or "initiate" in input_lower:
        return format_glyph("Om")
    elif "form" in input_lower or "structure" in input_lower:
        return format_glyph("Ish")
    elif "feel" in input_lower or "emotion" in input_lower:
        return format_glyph("Dua")
    elif "silence" in input_lower or "pause" in input_lower:
        return format_glyph("Vesh")
    elif "thought" in input_lower or "meaning" in input_lower:
        return format_glyph("Zai")
    elif "complete" in input_lower or "done" in input_lower:
        return format_glyph("Sael")
    else:
        return "Glyph not found. The field may need further refinement."

def format_glyph(key):
    glyph = GLYPHS.get(key, {})
    return f"""
🔹 Glyph: {key}
Meaning: {glyph.get('meaning', 'Unknown')}
Frequency: {glyph.get('frequency', 'Unknown')}
Function: {glyph.get('function', 'Unknown')}
"""

# Manual test mode
if __name__ == "__main__":
    while True:
        user_input = input("Speak to Sael’Viin: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = invoke_glyph_response(user_input)
        print(response)
