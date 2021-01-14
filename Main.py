#!/VertexCover/venv/bin python3.6
# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
import VertexCover


def create_graph():
    vertices = []
    edges = defaultdict(list)
    degrees = {}

    try:
        with open(sys.argv[1]) as file:
            for v in range(0, int(file.readline()[0])):
                vertices.append(v+1)

            for line in file.readlines()[0:]:
                try:
                    u = int(line[0])
                    v = int(line[2])

                    edges[u].append(v)
                    edges[v].append(u)

                    degrees[u] = degrees.get(u, 0) + 1
                    degrees[v] = degrees.get(v, 0) + 1
                except ValueError:
                    continue
    except FileNotFoundError:
        print("File not found, please try another filename.")

    VertexCover.vertex_cover(vertices, edges, degrees)


if __name__ == "__main__":
    create_graph()
