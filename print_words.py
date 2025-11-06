def main():
    word_list= ["cat", "program", "canvas", "dog", "dashboard", "debug", "go", "red"]
    result = print_words(word_list)
    print("Result:", result)

def print_words(words):
    for word in words:
        if len(word) == 3:
            print(word.title())

main()