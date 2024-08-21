def is_valid_walk(walk):
    return (len(walk) == 10 and
            walk.count('n') - walk.count('s') == 0 and
            walk.count('e') - walk.count('w') == 0)

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))