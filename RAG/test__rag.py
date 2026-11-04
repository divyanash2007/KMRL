
from pipeline import ask_rag


def main():

    print("KMRL DOCUMENT ASSISTANT")
    print("=" * 50)

    while True:

        question = input("\nAsk a question (or type 'exit'): ")

        if question.lower().strip() == "exit":
            break

        if not question.strip():
            continue

        try:
            result = ask_rag(question)

            print("\n========== GEMINI RESPONSE ==========\n")
            print(result["answer"])

            print("\n========== RETRIEVED SOURCES ==========\n")

            for source in result["sources"]:
                print(
                    f"- {source['file_name']} "
                    f"(Page {source['page_number']})"
                )

        except Exception as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    main()
