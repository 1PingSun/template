nums = [2, 7, 11, 15]
target = 9
setnums = set(nums)
m = 0
n = 0
for i in nums:
	if((target-i) in setnums):
		for j in range(len(nums)):
			if(nums[j] == i):
				m = j;
			if(nums[j] == (target-i)):
				n = j
		print(f"[{m},{n}]")
		exit()
