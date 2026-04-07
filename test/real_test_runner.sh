#!/bin/bash

LOG="test/real_test_results.txt"
> $LOG

echo "=== REAL SYSTEM TEST ===" | tee -a $LOG

run() {
  python main.py "$1" | tee -a $LOG
}

# reset memory
echo '{ "history": [] }' > memory/memory.json

echo "Test 1: no memory" | tee -a $LOG
run "continue building it"

echo "Test 2: create memory" | tee -a $LOG
run "build an api"

echo "Test 3: use memory" | tee -a $LOG
run "continue building it"

echo "Test 4: no memory usage expected" | tee -a $LOG
run "what is python"

echo "=== DONE ===" | tee -a $LOG
