#!/VertexCover/venv/bin python3.6
# -*- coding: utf-8 -*-
import sys
import VertexCover


def create_graph():
    edges = []
    vertices = []

    try:
        with open(sys.argv[1]) as file:
            for v in range(0, int(file.readline()[0])):
                vertices.append(v+1)

            for line in file.readlines()[0:]:
                try:
                    edges.append((int(line[0]), int(line[2])))
                    edges.append((int(line[2]), int(line[0])))
                    # edges[int(line[0])] = int(line[2])
                    # edges[int(line[2])] = int(line[0])
                except ValueError:
                    continue
    except FileNotFoundError:
        print("File not found, please try another filename.")

    VertexCover.vertex_cover(vertices, edges)


if __name__ == "__main__":
    create_graph()
