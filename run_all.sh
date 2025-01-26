#!/bin/bash

# Define the list of tasks
tasks=("biology", "earth_science" "economics" "psychology" "robotics" "stackoverflow" \
        "sustainable_living" "leetcode" "pony" "aops") #"theoremqa")

model="our_model"  # "gpt2" "gpt2-medium" "gpt2-large" "gpt2-xl" "our_model"

# output_d = "1b_output" 
# model_path = "/home/mqadri/rq/lit-gpt-dev/pythia-160m-fineweb-retrieval-pretrained-01"
# chkpt = 

for task in "${tasks[@]}"; do
    echo "Running task: $task"
    python run.py --task "$task" --model "$model"
done
