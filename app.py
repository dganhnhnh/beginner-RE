
import hashlib


username_trial = b"MORTON"

print(hashlib.sha256(username_trial).hexdigest()[4]
+hashlib.sha256(username_trial).hexdigest()[5]
+hashlib.sha256(username_trial).hexdigest()[3]
+hashlib.sha256(username_trial).hexdigest()[6]
+hashlib.sha256(username_trial).hexdigest()[2]
+hashlib.sha256(username_trial).hexdigest()[7]
+hashlib.sha256(username_trial).hexdigest()[1]
+hashlib.sha256(username_trial).hexdigest()[8])