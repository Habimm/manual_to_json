from info import info
import json
import re

# See: https://www.ibm.com/docs/en/icos/12.9.0?topic=problem-typical-integer-program-knapsack

def handle(pb2_request, repo_path):
  manual = pb2_request.input.decode('utf-8')
  info(manual)

  several_lines = manual.split('\n')
  line_1 = several_lines[0]
  line_2 = several_lines[1]
  line_3 = several_lines[2]

  capacity = int(line_1)
  capacities = [capacity]

  values = line_2.split()
  values = [int(value) for value in values]

  weights = line_3.split()
  weights = [int(weight) for weight in weights]
  weights = [weights]

  info(capacities)
  info(values)
  info(weights)

  standard_encoding = {
    "capacities": capacities,
    "values": values,
    "weights": weights,
  }

  standard_encoding = json.dumps(standard_encoding, indent=2)

  return standard_encoding
