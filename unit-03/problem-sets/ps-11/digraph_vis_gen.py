map_file = open('mit_map.txt', 'r')
output = 'digraph G {\n'

for line in map_file:
    values = line.split()
    output += '"{}" -> "{}"\n'.format(values[0], values[1])

output += '}\n'

print output
