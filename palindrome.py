text = input("Enter a string: ") 
cleaned_text = text.replace("", "")
if cleaned_text == cleaned_text[::-1]: 
       print(text, "is a palindrome")
       else:
       print(text, "is not a palindrome")