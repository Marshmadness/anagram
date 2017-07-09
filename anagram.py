# import sys

# DICTIONARY = sys.argv[1]
# NAME = sys.argv[2].lower()


def start():
    DICTIONARY = "dictionary.txt"
    NAME = "spear".lower()
    NAME_LENGTH = len(NAME)
    NAME_CHARACTERS = list(NAME)

    with open(DICTIONARY) as f:
        for line in f:

            stripped_line = line.rstrip().lower()

            if len(stripped_line) == NAME_LENGTH:

                line_character_bank = list(stripped_line)

                for name_character in NAME_CHARACTERS:
                    dictionary_term_characters = ''.join(line_character_bank)
                    character_position = dictionary_term_characters.find(name_character)
                    if character_position > -1:
                        line_character_bank = remove_a_character(line_character_bank, name_character)
                        if len(''.join(line_character_bank)) == 0:
                            print stripped_line


def remove_a_character(list_to_modify, character_to_remove):
    word_to_check = ''.join(list_to_modify)
    first_character_occurrence = (''.join(list_to_modify)).find(character_to_remove)

    if first_character_occurrence > -1:
        if first_character_occurrence == (len(word_to_check) - 1):  # If first occurance is the last character
            modified_character_list = list(word_to_check[:-1])
            return modified_character_list

        if first_character_occurrence == 0:  # If first occurence is the first character
            modified_character_list = list(word_to_check[1:])
            return modified_character_list

        phrase_begin = word_to_check[:first_character_occurrence]
        phrase_end = word_to_check[first_character_occurrence+1:]

        begin = ''.join(phrase_begin)
        end = ''.join(phrase_end)

        complete_word = begin + end
        list_with_removed_character = list(complete_word)

        return list_with_removed_character

    return ''

start()
