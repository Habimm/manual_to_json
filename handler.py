import json
import ortools.algorithms.pywrapknapsack_solver

# See: https://developers.google.com/optimization/pack/knapsack#python_4

def handle(pb2_request, repo_path):
  knapsack_instance = json.loads(pb2_request.input)

  values = knapsack_instance["values"]
  weights = knapsack_instance["weights"]
  capacities = knapsack_instance["capacities"]

  # Create the solver.
  solver = ortools.algorithms.pywrapknapsack_solver.KnapsackSolver(
    ortools.algorithms.pywrapknapsack_solver.KnapsackSolver.
    KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

  solver.Init(values, weights, capacities)
  computed_value = solver.Solve()

  packed_items = []
  packed_weights = []
  total_weight = 0
  answer_text = f'Total value = {computed_value}\n'
  for i in range(len(values)):
    if solver.BestSolutionContains(i):
      packed_items.append(i)
      packed_weights.append(weights[0][i])
      total_weight += weights[0][i]
  answer_text += f'Total weight: {total_weight}\n'
  answer_text += f'Packed items: {packed_items}\n'
  answer_text += f'Packed_weights: {packed_weights}\n'
  return answer_text
