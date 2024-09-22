import os

# Recall byte = 1 character = 8 bits = 2 hexadecimal digits = 1 integer in [0,255]
# 1 byte is denoted as 0x00,0x01,...,0xFF in hexadecimal
# 1 byte is denoted as 0b00000000,0b00000001, ..., 0b11111111 in binary
# 1 byte is denoted as 0, 1, 2, ..., 255 as an integer
# 1 byte is denoted as # https://www.ssec.wisc.edu/~tomw/java/unicode.html as a character

# THE CIPHERTEXTS FOR EXERCISE 6 ARE FOUND AT THE BOTTOM OF THIS FILE

# We assume that all messages are of same length n !

n = 60
msgs = [ 'PLAINTEXT MESSAGES REMOVED' ]

# The messages have the following format: 16 messages of 60 characters each
msgs = [
'this is an example this is an example this is an example thi',
's is an example this is an example this is an example this i',
's an example this is an example this is an example this is a',
'n example this is an example this is an example this is an e',
'xample this is an example this is an example this is an exam',
'ple this is an example this is an example this is an example',
' this is an example this is an example this is an example th',
'is is an example this is an example this is an example this ',
'is an example this is an example this is an example this is ',
'an example this is an example this is an example this is an ',
'example this is an example this is an example this is an exa',
'mple this is an example this is an example this is an exampl',
'e this is an example this is an example this is an example t',
'his is an example this is an example this is an example this',
' is an example this is an example this is an example this is',
' an example this is an example this is an example this is an']



def encrypt(pad, message):
	cipher_int = []
	for i, m in enumerate(message):
		cipher_int.append(ord(m) ^ int(pad[2*i:2*i+2],16))
	return bytes(cipher_int).hex()




pad_bytes = os.urandom(n*2)

pad_hex = bytes(pad_bytes).hex().zfill(n*4)

ctxts = [encrypt(pad_hex, m) for m in msgs]



print(ctxts)



############################################################

# These are the ciphertexts for Week 1, Exercise 6

CIPHERTEXTS = [
'6a0e3595c13cf60c39ae3193c30042b9cdc7314cf1ca76937e70b0237074572b956e9617ad3cc12f6a661a9a5d27fedd797c15277d9f330004c8fe36' 
'530e7093d121e50430a22a988c2850aad08e4250ff9869986b39fe0a025a6c63c127915fa56f963c763509995b27fadb356b13396293600400d4fe7f' 
'6f12768d982dff0437a8659cdf5254f8ccc66351fb9920996a39b4363f635439cf6ea71ea727c13f637a0c9d096ee48e383f092c7c9f250741c9ec36' 
'5636358bdc20fe162aa337d5de1753adccc66218ea8520847975b37a3f754b6a88298c10b6268f3a2f790e810977e5cb2f7a143d679827540fc9a772' 
'23307c8ad420b70c2de6208dd8175bbcdac7315ae7ca36c62c74bf3425745a39c12c871ca53a92382f7a09d64869b7c7377c132d6b98345408c8aa62' 
'701861c6c227e30d7ea72bd5c30250aaded77857f0ca779e657abe7a23614b2392288b1ab76f95356a350999456bf8d930711d696d992e0715d4eb7f' 
'6c13748ad16ec50c28a33681805274bcd6834250ff8769842c78b83e704c5a258f2f901be40e85316a780e980975f2cd3c760c2c6ad6341c0486de63' 
'6c103591dd27f40d7eaf31d5ca1d59b7c8d0314cf68b74d67871b37a207250288d2b8f5fab29c10d2f634fb87927fedd796a142d6b95291000c4e673' 
'65146795c16ef50a37aa6581c41715afded7744abe9e6fd66f76b9317074572fc13e830cb02ec13461394f824162f98e387b1e697d972c004f86da64' 
'57157c959523f6113dae6582cd0115aadac27d54e7ca639a636ab37670624a3ec107c213a12e93336a714f97096bf8da7979082663d6215402ceeb7b' 
'6a0e6183c762b7303baa2cd5e11340aadad13d18ed8b79852c71b37a23705021846e9610e43b89382f46189f5a74b7e0386b132660972c5423c7e47d' 
'73126792dc20f0452aae20d5c90454b4cac26551f18420996a39b53322634a23953dc210a26f83327a7b0b934d27e7c135661426639f211841c2ef66' 
'771871c6c121b70631a93791c51c54acda836359f08e6f9b6563b72e396f516a803dc21eaa6f843b69700c824071f28e3a700f277a93321904c7f963' 
'571570c6f12fe3047e832b96de0b45acd6cc7f18cd9e61986878a43e70685e39c12c871aaa6f807d7f670a92466afec038710e697d8f2d1904d2f87f' 
'710f708ad43afe0a30b56597c90642bddacd314ce98520977e6bb7232320502cc1068312a9268f3a2f620a9f4e6fe3dd797e142d2e82281141d6e561' 
'4210749cda20b70c2de62290d8065cb6d883635dff8e79d67876f63631755129896e835fa820957d60734f945b68f6ca3b7e142d2e85210004cae67f']
