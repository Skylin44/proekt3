def single_root_words( root_word, *other_words):
    same_words = []

    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)

    for j in other_words:
        if str(j).lower() in root_word.lower():
            same_words.append(j)

    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))