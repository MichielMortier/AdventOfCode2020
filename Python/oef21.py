import re
import copy
import functools


def solve(file_name):
    recepts = open(file_name).read().split("\n")
    all_ingreds = []
    allg_candidates = {}
    for recept in recepts:
        ingred, allerg = recept.split(" (contains ")
        allerg = allerg.strip(')').split(", ")
        ingred = ingred.split(" ")
        all_ingreds.extend(ingred)
        for allg in allerg:
            if allg in allg_candidates:
                allg_candidates[allg] &= set(ingred)
            else:
                allg_candidates[allg] = set(ingred)
    print(allg_candidates)
    # - on set is removing
    safe_ingredients = set(all_ingreds) - functools.reduce(lambda a, b: a.union(b), allg_candidates.values())
    result = sum([all_ingreds.count(i) for i in safe_ingredients])
    print(result)


def solve2(file_name):
    recepts = open(file_name).read().split("\n")
    all_ingreds = []
    allg_candidates = {}
    for recept in recepts:
        ingred, allerg = recept.split(" (contains ")
        allerg = allerg.strip(')').split(", ")
        ingred = ingred.split(" ")
        all_ingreds.extend(ingred)
        for allg in allerg:
            if allg in allg_candidates:
                allg_candidates[allg] &= set(ingred)
            else:
                allg_candidates[allg] = set(ingred)
    print(allg_candidates)
    found = {}
    while allg_candidates:
        print(allg_candidates)
        for allg, ingred in list(allg_candidates.items()):
            if len(ingred) == 1:
                found[allg] = min(ingred)
                del allg_candidates[allg]
            else:
                allg_candidates[allg] -= set(found.values())
    print(','.join([v for k,v in sorted(found.items())]))
