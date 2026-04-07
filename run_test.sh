#!/bin/bash

echo "=== RUNNING SYSTEM TEST ==="

inputs=(
  "build api"
  "continue building it"
  "what is python"
)

for input in "${inputs[@]}"; do
  echo ""
  echo ">>> INPUT: $input"
  python main.py "$input"
done

echo ""
echo "=== MEMORY OUTPUT ==="
cat memory/memory.json

echo ""
echo "=== EXECUTION HISTORY ==="
grep -A 5 "execution_history" memory/memory.json || echo "execution_history not found"

echo ""
echo "=== TEST COMPLETE ==="
