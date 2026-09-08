survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"]
]

sets = [set(res) for res in survey_results]

common_langs = set.intersection(*sets)
print("1. Chosen by all:", common_langs)

only_p1 = sets[0] - sets[1]
print("2. Only chosen by P1 (not P2):", only_p1)