# Python refresher exercises 2 - task 1

# Write and test a function is_valid_email_address(s) that evaluates string s as a valid email address 
# Returns: tuple of 2 elements (res, err):
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
#
# Rules: (these are mine, not the official web standards!)
# must have 3 parts: <A>@<B>.<C>
# A must have between 3 and 16 alpha numeric chars (test: isalnum()) 
# B must have between 2 and 8 alpha numeric chars (test: isalnum()) 
# C must be one of these:  com edu org gov 
#
# Here are some tests and the expected results:
# 
# charding@iastate.edu (None, 'Seems legit')
# chris.edu (1, 'Must have exactly one @!')
# chris@edu (4, 'post @ part must have exactly one dot!')
# @bla.edu (2, 'pre @ part must contain 3 - 16 alfanum chars')
# throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alfanum chars')
# chris@X.com (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# chris.harding@iastate.edu (3, 'pre @ part must only contain alfanum chars')
# chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov')
# chris@letsgo!.org (6, 'part after @ and before . must only contain alfanum chars')
# chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# tc@tank.com (2, 'pre @ part must contain 3 - 16 alfanum chars')
#
# your function MUST react the same (OK or error) but you don't have to use my exact error messages or codes 
# just something similar to that effect. You could even be more helpful e.g. 
# "throatwobblermangrove is too long (21 chars), must be 3 - 16"
# It's OK to bail you at the first proven error, even if there would have been more errors later!
# Also, I prb. forgot some possible edge cases, please add more if needed!

# As proof, please manually copy/paste the console output for one run into a file called
# results1.txt

def is_valid_email_address(s):
    # your code here
    num_at = s.count("@") # check to see how many @ symbols
    if num_at != 1: # check if there is anything other than 1 @ symbol
        return 1, "required to have  exactly 1 @"

    split_address = s.split("@") # split at the @ symbol
    A = split_address[0] # variable for part before the @ symbol
    after_at = split_address [1] # variable for part after the @ symbol

    if len(A) < 3 or len(A) > 16: # check if part before @ has right num chars
        return 2, "Error: part before @ symbol must be between 3 and 16 chars"

    elif A.isalnum() == False: # check if part before @ has only alfanum chars
        return 3, "Error: part before @ symbol must only have alfanum chars"

    if after_at.count(".") != 1: # check num of . in split after @
        return 4, "Error: address needs to have exactly 1 ."

    second_split = after_at.split(".") # split into B and C before/after the .
    B = second_split[0]
    C = second_split[1]

    if len(B) < 2 or len(B) > 8: # check lenth of B
        return 5, "Error:part between @ and . needs to be between 2 and 8 chars"
    elif B.isalnum() == False: # check if B is only alfanum characters
        return 6, "Error: part between @ and . needs to only have alfanum chars"

    if C not in ["com", "edu", "org", "gov"]: # check if C has appropriate ending chars
        return 7, "Error: part after . needs to be com, edu, org, or gov"

    return(None, "Everything looks good!") # address checks out - passes all tests



# This if ensures that the following is NOT run if this file was imported as a module (which we'll do next!)
if __name__ == "__main__":

    # tests, including edge cases (incomplete? add more!)
    email_list = ["charding@iastate.edu", 
        "chris.edu",
        "chris@edu",
        "@bla.edu",
        "throatwobblermangrove@mpfc.org", 
        "chris@X.com",
        "chris.harding@iastate.edu",
        "chris@pymart.biz",
        "chris@letsgo!.org",
        "chris@megasavings.org",
        "tc@tank.com",
        ]
    # validate each email from the list
    for e in email_list:
        r, s = is_valid_email_address(e) 
        if r == None:
            print(e, s) # OK
        else:
            print(f"{e} - error: {s}, error code: {r}") # Error

        
