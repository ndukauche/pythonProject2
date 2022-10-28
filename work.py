alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", 'j', "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", 'j', "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
done = True
while done :
    direct = input("type 'encode' to encrypt , type 'decode' to decrypt:\n")
    text = input("type your message:\n").lower()
    shif = int(input("type the shift number:\n"))
    shift = shif % 26
    def encrypt(texte, shifte, directe):
        encrypted = ""
        decrypted = ""
        if directe == "encode":
            for n in texte:
                if n in alpha:
                    position = alpha.index(n)
                    new = position + shifte
                    new_l = alpha[new]
                    encrypted += new_l
                else:
                    encrypted += n
            print(f"your encrypted message is {encrypted}")
        if directe == "decode":
            for n in texte:
                if n in alpha:
                    position = alpha.index(n)
                    new = position - shifte
                    new_l = alpha[new]
                    decrypted += new_l
                else:
                    decrypted += n
            print(f"the decrypted message is {decrypted}")
    encrypt(texte=text, shifte=shift, directe=direct)
    dd = input(f"Are you done? type 'y' for yes and 'n' for no\n")
    if dd == "y":
        done = False
        print("good bye")
