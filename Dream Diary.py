from typing import List, Dict

def main() -> None:

    """Main function to run the Dream Diary program."""

    print("Your Dream Diary Deluxe!")
    diary: List[Dict[str, str]]  # List to store dream entries

while True:
    choice = input("\nWhat would you like to do? (add / view / exit): ").lower()

    if choice == "add":
        add_entry(diary)
    elif choice == "view":
        view_entries(diary)
    elif choice == "exit":
        print("Exiting Dream Diary. Bye Bye Dream chaser!")
        break
    else:
        print("Invalid choice. Please try again.")

def add_entry(diary: List[Dict[str, str]]) -> None:

    """Function to add a new dream entry to the diary."""

    print("\nAdd New Dream Entry: ")
    title = str  = input("Enter Titles: ")
    description = str = input("Enter Description: ")
    tags = str = input("Enter Tags (optional): ")

    entry = Dict[str, str] = {"title": title, "description": description, "tags": tags}
    diary.append(entry)

    print("\nDream Entry Added Successfully!")

def view_entries(diary: List[Dict[str, str]]):
    """Function to view all dream entries in the diary."""
    print("\nAll Dream Entries: ")
    for index, entry in enumerate(diary, start=1):
        print(f"\nEntry {index}:")
        print(f"Title: {entry['title']}")
        print(f"Description: {entry['description']}")
        print(f"Tags: {entry['tags']}")

if __name__ == "__main__":
    main()