def main():
    book_path = 'books/FRANKENSTEIN.txt'
    text = get_book_text(book_path)
    print(f'--- Begin report of {book_path} ---')
    num_words = get_num_words(text)
    letters = get_letter_count(text)
    print(f'{num_words} words found in the document')
    sorted_letters = sort_letters(letters)
    for char in sorted_letters:
        if not char[0].isalpha():
            continue
        print(f"The '{char[0]}' character was found {char[1]} times")
    print('--- End report ---')

def sort_letters(letters):
    letters_list = list(letters.items())
    letters_list.sort(reverse=True, key=lambda x: x[1])
    return letters_list    

def get_letter_count(text):
    letter_dict = {}
    for letter in text:
        low_letter = letter.lower()
        if low_letter in letter_dict:
            letter_dict[low_letter] += 1
        else:
            letter_dict[low_letter] = 1
    return letter_dict

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()