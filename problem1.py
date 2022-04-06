 
def reverse(text):
  text = list(text)
  
  index = -1
  
  for i in range(len(text)-1, int(len(text)/2), -1):
    if text[i].isalpha():
      temp = text[i]
      while True:
        index += 1
        if text[index].isalpha():
          text[i] = text[index]
          text[index] = temp
          break
  return "".join(text)
  
print(reverse("a,b$c"))

arr = ["Ab,c,de!$","ed,c,bA!$","a,b$c"]

for i in arr:
  print(reverse(i))
  # print(i)