#!/VertexCover/venv/bin python3.6
# -*- coding: utf-8 -*-

def vertex_cover(vertices, edges):
    conjunto_P = []
    covered = []
    degrees = {}

    for v in edges:
        degrees[v[0]] = degrees.get(v[0], 0) + 1

    while vertices:
        try:
            max_degree = max(degrees, key=degrees.get)
            if max_degree not in covered:
                conjunto_P.append(max_degree)
                vertices.remove(max_degree)
                for v in edges:
                    if v[0] == max_degree:
                        covered.append(v[1])
                        vertices.remove(v[1])
                        edges.remove(v)
                del degrees[max_degree]
            else:
                del degrees[max_degree]
        except ValueError:
            continue

    print(conjunto_P)
