<a href="https://restaurantcontroller.github.io/EasyCrypt/">Home</a> <a href="https://restaurantcontroller.github.io/EasyCrypt/downloads.html">Downloads</a>
<br>
# EasyCrypt
ANNOUCEMENT: You can now use our QuickInstall program to get up and running quickly. See more at the downloads page.
Open Soruce File Encryption Software Written In Python
<br>
IMPORTANT: The file encoding must be UTF-8. Otherwise encryption will fail or the file may get corrupted.
<br>
You can encrypt files easily with this software. It uses the "key file" method.
<br>

For EasyCrypt to run correctly, you must install the <code>cryptography</code> plugin in Python. You can easily do it by using pip:
<br>
<code>pip install cryptography</code>
<br>
If you are encrypting files, you must generate a key. You can run keygen.py by using the this command:
<br>
<code>python keygen.py</code>
<br>
You only need to do this once
<br>
You will then select a file name for the key file.
<br>
Then, you can run EasyCrypt using the following command:
<br>
<code>python main.py</code>
<br>
And then specify the key file
<br>
That's it! You can encrypt and decrypt files with EasyCrypt.
<br>
<b>Note:</b> While decrypting an encrypted file, you must specify the same key you used to encrypt that file. If not it will fail and give an <code>InvalidToken</code> error message.
<br>
You can download EasyCrypt from the <a href="https://restaurantcontroller.github.io/EasyCrypt/downloads.html">Downloads</a> page.

Need help? Create an issue.
