# Q19. Input Normalizer: Text input se extra outer spaces remove karo 
# aur empty strings reject karo.
text = input("Enter String : ").strip()
if not text :
    print("Empty string")
else :
    print(text)