alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
  len_text= int(len(text)) 
  text_list=list(text) 
  encode_text=""    
  for char in range (0,len_text):
    i=0
    while text_list[char]!=alphabet[i]:
      i+=1
    new_position=i+shift 
    if new_position<= len(alphabet):
      encode_text += alphabet[new_position]
    else:
      y=len(alphabet)-i
      new_position=shift-y
      encode_text += alphabet[new_position]
  print(f"The encoded text is: {encode_text}")
  
if direction=="encode":
   encrypt(text,shift)  
else:
  print("Sorry, I am ready just to encode your text. I will learn soon how to decode the texts too :) ")