from app.agent import AI_Agent

def main():
    agent = AI_Agent()
    user_id = "terminal_user"
    print("=" * 40)
    print("Personal AI Agent")
    print("Type exit to close the program")
    print("=" * 40)

    while True:
        try:
            user_input = input("\n Enter your question here:  ").strip()
            if user_input == 'exit':
                print("Goodbye!")
                break

            if not user_input:
                continue

            response = agent.chat(message=user_input, user_id=user_id)
            print(f"\nAI: {response}")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
