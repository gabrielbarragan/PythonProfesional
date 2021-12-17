def is_palindrome(text: str) -> bool:

    text = text.replace(" ", "").lower()
    
    # if text == text[::-1]:
    #     return True
    # else:
    #     return False

    return text == text[::-1]
    

def run():
    
    if is_palindrome(1000):
        return 'Es palindromo'
    else:
        return 'No es palindromo'

if '__main__'== __name__:
    print(run())
