# from itertools import permutations, combinations

# def generate_permutations_combinations(input_list):
#     # Combinations
#     print("\nCombinations:")
#     for r in range(1, len(input_list) + 1):
#         for comb in combinations(input_list, r):
#             if(len(comb)>=2):
#                 print(", ".join(comb))

# # Example usage
# input_list = ["Ashutosh Kumar", "Fourbrick", "CEO"]
# generate_permutations_combinations(input_list)



# url = "https://www.google.com/search?q=Ashutosh+Kumar+Fourbrick"
# dUrl = getURL(keywords)


from itertools import combinations

def generate_permutations_combinations(input_list):
    # Storing combinations with length greater than 2
    result_combinations = []
    for r in range(1, len(input_list) + 1):
        for comb in combinations(input_list, r):
            if len(comb) >= 2:
                result_combinations.append(comb)
    return result_combinations

# Example usage
input_list = ["Ashutosh Kumar", "Fourbrick", "CEO"]
combinations_list = generate_permutations_combinations(input_list)

def getURL(keywords):
    base_url = "https://www.google.com/search?q="
    keyword_str = "+".join(keywords)
    return base_url + keyword_str

# Generating URLs using combinations
combinationURL = []
for combination in combinations_list:
    url = getURL(combination)
    combinationURL.append(url)
    
print(combinationURL)
