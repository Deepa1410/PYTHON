from tabulate import tabulate
data = [["Name","Age","Dept"],
        ["Raju","22","CSE"],
        ["Kennedy porus","25","ECE"]
     ]
headers = data[0]
rows = data[1:]
print(tabulate(rows, headers=headers,tablefmt="grid"))
