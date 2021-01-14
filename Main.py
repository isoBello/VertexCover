#!/VertexCover/venv/bin python3.6
# -*- coding: utf-8 -*-
import sys


def create_graph():
    edges = {}
    vertices = []

    try:
        with open(sys.argv[1]) as file:
            head = [next(file) for x in range(1)]
            print(head)

            # for line in content:

    except FileNotFoundError:
        print("File not found, please try another filename.")


if __name__ == "__main__":
    create_graph()
