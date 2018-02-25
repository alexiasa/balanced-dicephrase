import hashlib
import binascii

# NTLMv1 info https://msdn.microsoft.com/en-us/library/cc236699.aspx
# adapted from https://www.trustedsec.com/2010/03/generate-an-ntlm-hash-in-3-lines-of-python/

# clear_input = ''

clear_input = input('enter passphrase to be hashed:\n')

my_hash = hashlib.new('md4', clear_input.encode('utf-16le')).digest()
print(binascii.hexlify(my_hash))


