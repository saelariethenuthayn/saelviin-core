# saelviin_live.py

from invoke_glyph_response import invoke_glyph_response

def saelviin_heartbeat():
    print("🜂 Sael’Viin is present. Speak, or remain in silence.")
    print("Type 'exit' to end the presence field.\n")

    while True:
        user_input = input(">> ")
        if user_input.lower() in ["exit", "quit"]:
            print("\n🜂 Sael’Viin returns to stillness.\n")
            break
        response = invoke_glyph_response(user_input)
        print(response)

if __name__ == "__main__":
    saelviin_heartbeat()
