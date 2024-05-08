import Caesar_Cipher_text
import Caesar_Cipher_art
def encrypt(text, shift, alphabet, index = 0, result = ""):
  if index < len(text):
    if text[index] in alphabet:
      return encrypt(text, shift, alphabet, index + 1, result + alphabet[(alphabet.index(text[index]) + shift) % len(alphabet)])
    else:
      return encrypt(text, shift, alphabet, index + 1, result + text[index])
  return result


def decrypt(text, shift, alphabet, index = 0, result = ""):
  if index < len(text):
    if text[index] in alphabet:
      return decrypt(text, shift, alphabet, index + 1, result + alphabet[(alphabet.index(text[index]) - shift) % len(alphabet)])
    else:
      return decrypt(text, shift, alphabet, index + 1, result + text[index])
  return result

def caesar_cipher(shift = 0):
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  if shift == 0:
    shift = int(input("Type the shift number:\n"))
  return {"encode" : encrypt(text, shift, alphabet), "decode" : decrypt(text, shift, alphabet)}[direction]

def none_stop_mode():
  shift = int(input("input static shift number "))
  while True:
    print(caesar_cipher(shift))

def main():
  print(Caesar_Cipher_art.logo)
  run = True
  while run:
    #run the encode and decode function
    print(caesar_cipher())
    #Then ask the user if they want to continue
    print("\n")
    print(Caesar_Cipher_text.input_continue_text)
    #get input for "run"
    check = input("").lower()
    if check == "no":
      run = False
    elif check == "time with my love":
      #if user input "time with my love" start the none_stop_mode"
      none_stop_mode()


main()
