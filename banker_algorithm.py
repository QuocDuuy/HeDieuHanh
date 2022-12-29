def main():
	def check(i):
		for j in range(m):
			if need[i][j] > available[j]:
				return False
		return True

	n = int(input("Enter the number of Processes: "))
	m = int(input("Enter the number of Resources: "))

	maX = []
	for i in range(n):
		maX.append(list(map(int, input("\nEnter Max matrix entry for Process P"+str(i)+" : ").strip().split())))

	allocation = []
	for i in range(n):
		allocation.append(list(map(int, input('\nEnter the number of instances allocated for Process P'+str(i)+" : ").strip().split())))
		
	available = list(map(int, input("\nEnter the number of instances available of Resources : ").strip().split()))    

	# Compute the need matrix
	need = [[0 for i in range(m)] for j in range(n)]
	for i in range(n):
		for j in range(m):
			need[i][j] = maX[i][j] - allocation[i][j]
	print("Need Table: \n")
	for i in need:
		print(i)
		

	# Implements Banker's Algorithm 
	sequence = ['0']*n
	visited = [0]*n
	count = 0
	while count<n:
		safe = False
		for i in range(n):
			if visited[i]==0 and check(i):
				print()
				print(f"Process {i + 1} is executing")
				sequence[count] = "P" + str(i)
				count += 1
				visited[i] = 1
				safe = True
				for j in range(m):
					available[j] += allocation[i][j]
				print("Available resource is", available)		
		if not safe:
			break

	
	if (count<n):
		print("The System is Unsafe!")
		
	else:
		print()
		print("The System is Safe!")
		print("Safe Sequence is", sequence)
		print("Available resource is", available)

if __name__ =="__main__":
	main()