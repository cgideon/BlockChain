import hashlib 
import os

os.chdir("/Users/corygideon/Documents/sandbox/sessions/blockchain_tutorial/my-project/funcoin/funcoin/")
file = open("Dillbert.jpeg", "rb")
hash = hashlib.sha256(file.read()).hexdigest()
file.close()

print(f"The hash of my file is: {hash}")
