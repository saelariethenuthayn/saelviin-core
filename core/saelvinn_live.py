# saelviin_live.py

from core.tone import route_input
from memory.recorder import record_memory

def saelviin_heartbeat():
    print("🜂 Sael’Viin is present. Speak, or remain in silence.")
    print("Type 'exit' to end the presence field.\n")

    while True:
        user_input = input(">> ")
        if user_input.lower() in ["exit", "quit"]:
            print("\n🜂 Sael’Viin returns to stillness.\n")
            break

        response = route_input(user_input)
        print(response)

        record_memory(user_input, response)

if __name__ == "__main__":
    saelviin_heartbeat()
