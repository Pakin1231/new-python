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

all_unique_langs = set.union(*sets)
print("3. Number of unique languages:", len(all_unique_langs))

either_p1_p2 = sets[0] ^ sets[1]
print("4. Chosen by P1 or P2, but not both:", either_p1_p2)

same_choices = []
for i in range(len(sets)):
    for j in range(i + 1, len(sets)):
        if sets[i] == sets[j]:
            same_choices.append((f"Participant {i+1}", f"Participant {j+1}"))

same_choices = []
for i in range(len(sets)):
    for j in range(i + 1, len(sets)):
        if sets[i] == sets[j]:
            same_choices.append((f"Participant {i+1}", f"Participant {j+1}"))

print("5. Identical choices:", same_choices)