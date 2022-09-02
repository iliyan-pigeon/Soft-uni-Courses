data = input().split()
arranged_data = {}
for i in range(0, len(data), 2):
    arranged_data[data[i]] = int(data[i+1])
print(arranged_data)
