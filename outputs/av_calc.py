import os
import json
from glob import glob

base_dir = "./prefixsuffix"

all_metrics = {}

task_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
for task_dir in task_dirs:
    result_file = os.path.join(base_dir, task_dir, "results.json")
    if not os.path.exists(result_file):
        print(f"Results file not found for task: {task_dir}")
        continue

    # Load results
    with open(result_file, "r") as f:
        metrics = json.load(f)

    # Aggregate metrics
    for metric, value in metrics.items():
        if metric not in all_metrics:
            all_metrics[metric] = []
        all_metrics[metric].append(value)

average_metrics = {metric: sum(values) / len(values) for metric, values in all_metrics.items()}

print("Average Metrics:")
for metric, avg in average_metrics.items():
    print(f"{metric}: {avg:.5f}")

with open("preffix_suffix_average_results.json", "w") as f:
    json.dump(average_metrics, f, indent=2)
