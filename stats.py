    
def get_num_words(word):
    return len(word.split())

def count_chars(text):
    char_count = {}

    for c in text.lower():
        if not c in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1

    return char_count

def sort_on(items):
    return items["num"]

def report(data_dict, path, wc):
    sorted_list = []

    for d in data_dict:
        if not d.isalpha():
            continue
        
        sorted_list.append({
            "char": d,
            "num": data_dict[d]
        })

    sorted_list.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")

    for idx in range(len(sorted_list)):
        print(f"{sorted_list[idx]["char"]}: {sorted_list[idx]["num"]}")

    print("============= END ===============")
