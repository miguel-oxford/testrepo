def findAnagram(s,p):
	ans=[]
	enum_s = enumerate(s)

	for index_p in range(len(p)):
		for index_s, char_s in enum_s:
			if char_s==p[index_p]:
				check = check_substring(s[index_s:index_s+len(p)],p)
				if check:
					ans.append(index_s)
					



	def check_substring (sub,p):
		sub =list(sub)
		for i in p:
			if i in sub:
				sub.remove(i)
			else:
				return False
		return True
