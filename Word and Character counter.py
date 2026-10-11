
# Word and Character Counter

paragraph = input("Enter a paragraph: ")

if paragraph.strip() == "":
    print("The paragraph is empty.")
else:
    characters = len(paragraph)
    words = len(paragraph.split())
    spaces = paragraph.count(" ")

    sentences = 0
    for char in paragraph:
        if char in ".!?":
            sentences += 1

    print("\n--- Paragraph Analysis ---")
    print("Characters:", characters)
    print("Words:", words)
    print("Sentences:", sentences)
    print("Spaces:", spaces)
