from .fuzzy_matching import levenshtein_distance


def calculate_matching_percentage(string1, string2):
    if len(string2) > 0:
        distance = levenshtein_distance(string1, string2)
        length = min(len(string1), len(string2))
        matching_percentage = (length - distance) / length * 100
        return matching_percentage
    else:
        return 0