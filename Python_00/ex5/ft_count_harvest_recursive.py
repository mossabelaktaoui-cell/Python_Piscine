def ft_count_harvest_recursive(i = 1, day = -1):
	if day == -1:
		day = int(input("Days until harvest: "))
	print("Day", i)
	if i == day:
		print("Harvest time!")
		return
	ft_count_harvest_recursive(i + 1, day)