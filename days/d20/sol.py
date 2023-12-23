print("Day 20:")

FILE = "days/d20/example.txt"
FILE = "days/d20/main.txt"

modules = {}
conj_modules = {}
flip_modules = {}

with open(FILE) as f:
    for line in f.read().splitlines():
        source, output = line.split(" -> ")
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
        modules[name] = (type, output.split(", "))

for flip_mod in flip_modules:
    for node in modules[flip_mod][1]:
        if node in conj_modules:
            conj_modules[node][flip_mod] = 0

# print(*list(modules.items()))

signals = []
low_pulses = 0
high_pulses = 0
for _ in range(1000):

    signals.append(("broadcaster", 0, None))

    while signals:

        module, pulse, sender = signals.pop(0)
        if pulse == 1: high_pulses += 1
        else: low_pulses += 1

        try:
            type, output = modules[module]
        except KeyError:
            # print(module, "not found")
            continue
        if type == "broad":
            for node in output:
                signals.append((node, pulse, module))
        elif type == "%": # flip-flop
            if pulse == 0:
                flip_modules[module] = not flip_modules[module]
                for node in output:
                    signals.append((node, flip_modules[module], module))
        elif type == "&":
            conj_modules[module][sender] = pulse
            for node in output:
                signals.append((node, not all(conj_modules[module].values()), module))


print("Part 1:", low_pulses*high_pulses)
print("Part 2:")
