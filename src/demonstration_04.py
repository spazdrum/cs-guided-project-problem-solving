"""
Challenge #4:

Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad`, and `mad` with their
corresponding emoticons.

word -> emoticon
---
smile -> :D
grin -> :)
sad -> :(
mad	-> :P

Examples:
- emotify("Make me smile") ➞ "Make me :D"
- emotify("Make me grin") ➞ "Make me :)"
- emotify("Make me sad") ➞ "Make me :("

Notes:
- The sentence always starts with "Make me".
- Try to solve this without using conditional statements like if/else.

- We might want to use a dictionary to store the key value pairs

{
    "smile": ":)"
    "grin": ":D"
    "sad": ":("
    "mad": ">:|"
}
- iterate over the hash table items extrapolating the key and value of each item
- user a string '.replace' to replace the substring of the key with the value

"""


def emotify(txt):
    # first pass
    # store the key value pairs of the required data for swapping out the text to emoticons
    # we will store this data in a hash table (dictionary / object)
    # data = {
    #     "smile": ":)",
    #     "grin": ":D",
    #     "sad": ":(",
    #     "mad": ">:|"
    # }

    # iterate over the hash table items extracting the kay and value
    # for k, v in data.items():
        # set an updated string using the '.replace' method 
        # to return each new txt with the old substring substituted for the old one
        # txt = txt.replace(k, v)

    # return our new txt
    # return txt

    # second pass
        # store the key value pairs of the required data for swapping out the text to emoticons
    # we will store this data in a hash table (dictionary / object)
    data = {
        "smile": ":)",
        "grin": ":D",
        "sad": ":(",
        "mad": ">:|"
    }

    # get the substring of txt from the start to index 7 (8 - 1) indices in [ :8] set it as start_of_string -> "Make me "
    start_of_string = txt[:8]
    # get the data at 8 in from the start of the string [8: ] set it as end_of_string -> "smile"
    end_of_string = txt[8:]
    # concatonate start_of_string with value from data using end_of_string -> "smile" -> ":)" as the key and set them to full_string
    full_string = start_of_string + data[end_of_string]
    # return full_string]
    return full_string



print(emotify("Make me smile")) # ➞ "Make me :)"
print(emotify("Make me grin")) # ➞ "Make me :D"
print(emotify("Make me sad"))  # ➞ "Make me :("
print(emotify("Make me mad")) # ➞ "Make me >:|"

