### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################


flag_enc = open('flag.txt.enc', 'rb').read()



def level_1_pw_check():
    user_pw = input("Please enter correct password for the flag: ")
    if( user_pw == "ak43/08#98" + \
                   "1/+9@0" + \
                   "a#dfj!hgj@321" + \
                   "tr@bhvn9/#43n3"):
        print("Welcome back... your flag:")
        decryption = str_xor(flag_enc.decode(), "gdscgdsc")
        print(decryption[:-1])
        return
    print("That password is incorrect")



level_1_pw_check()
