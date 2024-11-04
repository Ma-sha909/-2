def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        d = i.upper()
        root_word2 = root_word.upper()
        if d.count(root_word2) != 0:
            same_words.append(i)
        if root_word2.count(d) != 0:
            same_words.append(i)
    return print(same_words)

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')


    