from stats import count_words
from stats import char_use
from stats import sort_char


def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:  # Open the file using 'with' for better resource management
        file_contents = file.read()  # Read the file contents
    
    return file_contents



def main():
    book_path = "/mnt/c/Users/Wyatt/Documents/GitHub/bookbot/books/frankenstein.txt"

    try:
        book_contents = get_book_text(book_path)
        word_count = count_words(book_contents)
        chars = char_use(book_contents)
        sorted_list = sort_char(chars)
    
        print("============ BOOKBOT ============", 
              "\nAnalyzing book found at books/frankenstein.txt...\n",
              "----------- Word Count ----------\n",
              f"Found {word_count} total words\n",
              "--------- Character Count -------")
        for sort in sorted_list:
            print(sort[0] + ":", sort[1])
        print("============= END ===============")

        
    except FileNotFoundError:
        print(f"Error: The file '{book_path}' was not found. Please check the path and ensure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

main()
