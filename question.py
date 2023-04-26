# Question A
def reverseString(string) -> str:
  return string[::-1]

# Question B
def reverseSetence(string) -> str:
  answer = ""
  for i in string.split( ):
    answer = answer +  " " +reverseString(i) 
  return answer[1:]


