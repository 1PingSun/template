nums = [2, 7, 11, 15]
target = 9
dicnums = {}
for i in range(len(nums)):
	dicnums[nums[i]]=i	
for i in dicnums.keys():
	if((target-i) in dicnums.keys()):
		print(f"[{dicnums[i]},{dicnums[target-i]}]")
		exit()
