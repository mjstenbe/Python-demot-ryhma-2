teksti = input("Anna rivi joka kirjoitetaan: ")
with open("new_file2.txt", "a") as my_file:
    my_file.write( teksti+"\n")
