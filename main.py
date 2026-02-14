import sys
from pipelines.research_pipeline import run_research


def main():
    print("\n🧠 AI Research Agent")
    print("=" * 40)

    try:
        topic = input("\nEnter research topic: ").strip()

        if not topic:
            print("⚠️  Topic cannot be empty.")
            sys.exit(1)

        print("\n🚀 Running research...\n")

        result = run_research(topic)

        print("\n" + "=" * 40)
        print("📚 FINAL RESEARCH OUTPUT\n")
        print(result)
        print("=" * 40)

    except KeyboardInterrupt:
        print("\n\n❌ Process interrupted by user.")
    except Exception as e:
        print("\n❌ Error occurred:")
        print(str(e))


if __name__ == "__main__":
    main()
