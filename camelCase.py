# This program turns a sentence into camel case.

# sentence = input("Type a sentence: \n")
# sentence = "fOnt proCESSOR and ParsER"
# print(f"string: {sentence}")
# print()

# lst = [] # initializes a list
# lst.append(sentence) # add the string in a list


# # This function takes a string and split it into different elements
# def convert(lst):
#     return(lst[0].split())

# # converts string into a list
# stringToList = convert(lst)
# print(f'list: {stringToList}')
# print()


# stringToList2 = [] # initializing the second list
# for num in stringToList:
#         stringToList2.append(num.title())

# print(f'string to list: {stringToList2}')
# print()

# stringToList2[0] = stringToList2[0].lower()

# stringToList = stringToList2

# # Converts list to string
# listToString = ''.join(stringToList)

# Camel Case
print(f'camel case string: {listToString}')
def camelcase(sentence):
    """ Convert sentence to camelCase, for example, "Display all books" 
    is converted to "displayAllBooks" """
    title_case = sentence.title() # Uppercase firts letter of each word
    upper_camel_cased = title_case.replace(' ', '') # remove spaces
    # Lowercase first letter, join     with rest of string
    #Slices don't produce index out of bounds errors.
    #So this still works on empty strings, strings of length 1
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def main():
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()