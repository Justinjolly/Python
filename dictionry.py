# To merge two dictionaries into a single dictionary using keys #
a = {2: 'ram', 3: 'sam', 5: 'rahul'}
print(a[3])
h = {4: 'python', 6: 'java', 1: 'html'}
g = dict(zip(a, h))
print(g)
# To merge tuples into dictionary  #
key = ['ram', 'sam', 'rahul']
values = ['python', 'java', 'html']
data = dict(zip(key, values))
print('\n', data, '\n')
# reading based on index #
s = {'java': 'Eclipse', 'python': ['vscode', 'pycharm'], 'programing': {1: 'Eclipse', 2: 'vscode', 3: 'pycharm'}}
print(s['java'])
print(s['python'][0])
print(s['python'][1])
print(s['programing'][1])
print(s['programing'][2])
print(s['programing'][3])