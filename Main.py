class LawLibrary:
    def __init__(self):
        self.library = {}

    def add_document(self, title, content):
        if title in self.library:
            print("A document with the same title already exists. Use a different title.")
        else:
            self.library[title] = content
            print("Document added successfully.")

    def search_document(self, keyword):
        results = {}
        for title, content in self.library.items():
            if keyword.lower() in content.lower() or keyword.lower() in title.lower():
                results[title] = content
        return results

    def view_document(self, title):
        if title in self.library:
            print(f"Title: {title}\n")
            print(self.library[title])
        else:
            print("Document not found.")

def main():
    library = LawLibrary()

    while True:
        print("\n==== Digital Law Library ====")
        print("1. Add Document")
        print("2. Search Documents")
        print("3. View Document")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            title = input("Enter document title: ")
            content = input("Enter document content: ")
            library.add_document(title, content)

        elif choice == "2":
            keyword = input("Enter keyword to search for documents: ")
            results = library.search_document(keyword)
            if results:
                print("\nSearch Results:")
                for title, content in results.items():
                    print(f"\nTitle: {title}\n{content}")
            else:
                print("No matching documents found.")

        elif choice == "3":
            title = input("Enter the title of the document to view: ")
            library.view_document(title)

        elif choice == "4":
            print("Exiting the Digital Law Library.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
