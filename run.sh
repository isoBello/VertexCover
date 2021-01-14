#!/usr/bin/env bash

. venv/bin/activate

files="Entradas/graph1.txt Entradas/graph2.txt Entradas/graph3.txt"

for file in $files; do
  python3 Main.py "$file"
done