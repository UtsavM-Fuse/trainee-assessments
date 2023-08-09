"""
Anagram Grouping Module

This module provides a function to group anagrams together from a given list of strings.
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Group anagrams together from the given list of strings.

    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    Args:
        strs (list[str]): A list of strings to be grouped.

    Returns:
        list[list[str]]: A list of lists containing grouped anagrams.

    Examples:
        >>> strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        >>> group_anagrams(strs)
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

        >>> strs = ["listen", "silent", "enlist", "tinsel"]
        >>> group_anagrams(strs)
        [['listen', 'silent'], ['enlist'], ['tinsel']]
    """
    anagram_dict = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    return list(anagram_dict.values())


if __name__ == "__main__":
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(input_strs)
    print(result)
