from cryptography.fernet import Fernet

print("EasyCrypt Key Generator");
key = Fernet.generate_key();
print("Ready to write key file!");
print("Now, please select a file name");
print("Note: If the file exists all the data on the file will be overwritten!");
filename = input("Type a filename to save the key file(Example: key.key): ");
if(filename == ""):
    print("ERROR: type a valid name");
else:
    keyfile = open(filename, "w");
    keyfile.write(key.decode("utf-8"));
    print("Key generated!");