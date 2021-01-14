#!/VertexCover/venv/bin python3.6
# -*- coding: utf-8 -*-

def vertex_cover(vertices, edges, degrees):
    conjunto_P = []
    covered = []

    while vertices:
        max_degree = max(degrees, key=degrees.get)
        degrees.pop(max_degree)
        if max_degree not in covered:
            try:
                conjunto_P.append(max_degree)
                covered.append(max_degree)
                vertices.remove(max_degree)
                covered.extend(edges.get(max_degree))
                vertices = list_difference(vertices, covered)
            except ValueError:
                continue
    print(len(conjunto_P))


def list_difference(l1, l2):
    return list(set(l1) - set(l2))
