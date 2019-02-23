if __name__ == '__main__':
    name = ' aleX'
    print(name.strip())
    # name = name.strip()
    if name.startswith('al'):
        print('yes')
    if name.endswith('X'):
        print('yes')
    print(name.replace('l', 'p'))
    # name = name.replace('l', 'p')
    print(name.split('l'))
    print(type(name.split('e')))
    print(name.upper())
    print(name.lower())
    print(name[2])
    print(name[:3])
    print(name[3:])
    print(name.index('e'))
    print(name[:len(name) - 1])
