# Define your function here
def hasVowel ( input_string ): 
    vowels = ["a", "e", "i", "o", "u"]
    return True in [c in input_string for c in vowels]

def hasVowel2 ( input_string ): 
    vowels = ["a", "e", "i", "o", "u"]
    for c in vowels:
        if c in input_string: return True
    return False
    

if __name__ == '__main__':
    while True:
        input_string = str(input(""))
        print ( "Does the input string " , input_string , " have a vowel? ",  hasVowel2 (input_string) ) 
