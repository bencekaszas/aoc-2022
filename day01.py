print(sorted([sum([int(cal) for cal in elf.split('\n')]) for elf in open('day01input').read().split('\n\n')[:-1]])[-1])
print(sum(sorted([sum([int(cal) for cal in elf.split('\n')]) for elf in open('day01input').read().split('\n\n')[:-1]])[-3:]))