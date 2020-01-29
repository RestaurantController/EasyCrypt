import os
import json
import base64
from cryptography.fernet import Fernet

print("EasyCrypt v1.0 - Open Soruce File Encryption Software");
print("Key file selection");
print("Note: If you haven't got a key, please generate a key file by running keygen.py");
keyfilename = input("Please enter the name of the key file:");
if(os.path.exists(keyfilename) == False):
    print("File not found!");
    exit();
keyfile = open(keyfilename, "r");
key = keyfile.read();
f = Fernet(key);
print("OK!");
print("Options:");
print("e - Encrypt Files");
print("d - Decrypt files");
option = input("Select an option:");
if(option == "e"):
    filename = input("Enter the name of the file to encrypt(Note: a new file with the extension .easycrypt will be created): ");
    if(not os.path.exists(filename)):
        print("File not found!");
        exit();
    efile = open(filename, "r");
    contents = efile.read();
    encrypted = f.encrypt(bytes(contents, "utf-8"));
    encryptedfilename = filename + ".easycrypt";
    encryptedfile = open(encryptedfilename, "w");
    encryptedfile.write(encrypted.decode("utf-8"));
    print("Successfully created encrypted file!");
elif(option == "d"):
    filename = input("Enter the encrypted filename: ");
    print("Trying to decrypt the file with the key, please wait....");
    if(not os.path.exists(filename)):
        print("File not found!");
        exit();
    efile = open(filename, "r");
    encrypted = efile.read();
    decrypted = f.decrypt(bytes(encrypted, "utf-8"));
    print("Successfully decrypted file contents with the key!");
    print("Now, you will enter a name for the decrypted file(Note: If the file exists all data in the file will be overwritten!)");
    outputfilename = input("Enter a name for the decrypted file: ");
    if(outputfilename == ""):
        print("FileError");
        exit();
    outputfile = open(outputfilename, "w");
    outputfile.write(decrypted.decode("utf-8"));
    print("Done!");
else:
    print("Option invalid!");