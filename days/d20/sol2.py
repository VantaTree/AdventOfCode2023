from math import lcm

print("Day 20:")

FILE = "days/d20/example.txt"
FILE = "days/d20/main.txt"

modules = {}
conj_modules = {}
flip_modules = {}

with open(FILE) as f:
    for line in f.read().splitlines():
        source, output = line.split(" -> ")
        outputs = output.split(", ")
        if source == "broadcaster":
            type = "broad"
            name = source
        else:
            type = source[0]
            name = source[1:]
            if type == "&":
                conj_modules[name] = {}
            elif type == "%":
                flip_modules[name] = 0
            if outputs[0] == "rx":
                target_node = name
        modules[name] = (type, outputs)

for mod in modules:
    for node in modules[mod][1]:
        if node in conj_modules:
            conj_modules[node][mod] = 0
target_nodes = conj_modules[target_node].copy()
target_no = len(target_nodes)

# print(*list(modules.items()))

signals = []
index = 0
target_gotten = 0
while target_gotten < target_no:
    
    signals.append(("broadcaster", 0, None))
    index += 1

    while signals:

        module, pulse, sender = signals.pop(0)

        try:
            type, output = modules[module]
        
            if type == "broad":
                for node in output:
                    signals.append((node, pulse, module))
            elif type == "%": # flip-flop
                if pulse == 0:
                    flip_modules[module] = not flip_modules[module]
                    for node in output:
                        signals.append((node, flip_modules[module], module))
            elif type == "&": # conjunction
                conj_modules[module][sender] = pulse
                for node in output:
                    signals.append((node, not all(conj_modules[module].values()), module))
        except KeyError: pass

        for node in target_nodes:
            if not target_nodes[node] and conj_modules[target_node][node] == 1:
                target_nodes[node] = index
                target_gotten += 1
                if target_gotten == target_no: break


print(target_nodes)
print("Part 1:")
print("Part 2:", lcm(*list(target_nodes.values())))
