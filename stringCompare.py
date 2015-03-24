#########################################################################
# File: stringCompare.py												
# Descriptions: String comparison techniques for file path similarity	
# Input: The arguments f1, f2 are strings of file path 					
# Output: Number of common file path components in f1 and f2			
# Written By: Patanamon Thongtanunam (patanamon-t@is.naist.jp)			
#########################################################################

def path2List(fileString):
	return fileString.split("/")

def LCP(f1,f2):
	f1 = path2List(f1)
	f2 = path2List(f2)
	common_path = 0
	min_length = min(len(f1),len(f2))
	for i in range(min_length):
		if f1[i] == f2[i]:
			common_path += 1
		else:
			break
	return common_path

def LCSuff(f1,f2):
	f1 = path2List(f1)
	f2 = path2List(f2)
	common_path = 0
	r = range(min(len(f1),len(f2)))
	r.reverse()
	for i in r:
		if f1[i] == f2[i]:
			common_path += 1
		else:
			break
	return common_path

def LCSubstr(f1,f2):
	f1 = path2List(f1)
	f2 = path2List(f2)
	common_path = 0
	if len( set(f1) & set(f2)) > 0:
		mat = [[0 for x in range(len(f2)+1)] for x in range(len(f1)+1)]
		for i in range(len(f1)+1):
			for j in range(len(f2)+1):
				if i == 0 or j == 0:
					mat[i][j] = 0
				elif f1[i-1] == f2[j-1]:
					mat[i][j] = mat[i-1][j-1] + 1
					common_path = max(common_path,mat[i][j])
				else:
					mat[i][j] = 0
	return common_path

def LCSubseq(f1,f2):
	f1 = path2List(f1)
	f2 = path2List(f2)
	if len( set(f1) & set(f2)) > 0:
		L = [[0 for x in range(len(f2)+1)] for x in range(len(f1)+1)]
		for i in range(len(f1)+1):
			for j in range(len(f2)+1):
				if i == 0 or j == 0:
					L[i][j] = 0
				elif f1[i-1] == f2[j-1]:
					L[i][j] = L[i-1][j-1] + 1
				else:
					L[i][j] = max(L[i-1][j], L[i][j-1])
		common_path = L[len(f1)][len(f2)]
	else:
		common_path = 0
	return common_path
