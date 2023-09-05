a="reyedfim"
import hashlib
i=0
password=""
while True:
	i+=1
	st=a+str(i)
	hash=hashlib.md5(st.encode('utf-8')).hexdigest()
	if hash[:5]=="00000":
		password+=hash[5]
		print(i,password)
		if len(password)==8: break
print(password)

i=0
password=["_" for _ in range(8)]
while True:
	i+=1
	st=a+str(i)
	hash=hashlib.md5(st.encode('utf-8')).hexdigest()
	if hash[:5]=="00000":
		if hash[5] in "89abcdef":continue
		pos=int(hash[5])
		if password[pos]=="_":
			password[pos]= hash[6]
			print(i,"".join(password))
			if password.count("_")==0: break
print("".join(password))