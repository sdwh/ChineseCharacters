def read_stroke(filename):
    stroke = {}
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split('\t')
            if len(data) == 2:
                stroke[data[0]] = data[1]
    return stroke    
    
strokes = read_stroke('CNS_stroke.txt')