from re import sub

def main():
    # Open file as string
    file = open("document.txt", "r").read()
    # Remove everything but alpha chars
    file = sub(r"[^a-zA-Z ]", "", file)
    # Make lowercase
    # file = file.lower()
    # Split into array of words
    file = file.split()

    # Count words using dictionary
    word_dict = {}
    for word in file:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    # Create array of tuples
    word_list = []
    for word in word_dict:
        word_list.append((word, word_dict[word]));

    # Sort the list by word
    # Sorting it this way results in words with the same count
    # being sorted alphabetically
    word_list.sort(key = lambda x: x[0])

    # Sort the list by count
    word_list.sort(key = lambda x: x[1], reverse = True)

    # Select and print top 5 words
    for i in range(5):
        print(f"{word_list[i][0]}: {word_list[i][1]}")

if __name__ == '__main__':
    main()
