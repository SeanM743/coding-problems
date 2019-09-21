def min_path_triangle(triangle):
    length = [0 * len(triangle)]

    for row in triangle:
        length = [row[j] + min(length[j], length[j-1]) 
        
        for j in len(row)]
        