import sys, hashlib

dgst = hashlib.md5(sys.argv[1]).hexdigest()

print dgst



