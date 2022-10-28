alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", 'j', "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
direct = input("type 'encode' to encrypt , type 'decode' to decrypt:\n")
text = input("type your message:\n").lower()
shift = int(input("type the shift number:\n"))
if direct == "encode":
    def encrypt(texte, shifte):
        encrypted = ""
        for n in texte:
            position = alpha.index(n)
            new = position + shifte
            new_l = alpha[new]
            encrypted += new_l
        print(f"your encrypted message is {encrypted}")
    encrypt(texte=text, shifte=shift)
if direct == "decode":
    def encrypt(texte, shifte):
        encrypted = ""
        for n in texte:
            position = alpha.index(n)
            new = position - shifte
            new_l = alpha[new]
            encrypted += new_l
        print(f"the decrypted message is {encrypted}")
    encrypt(texte=text, shifte=shift)
