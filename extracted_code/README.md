# Meaningfully organized notebook code

The notebook cells have been analyzed and combined by purpose. A definition, its example calls, and its simulation now live in one file instead of being split arbitrarily at cell boundaries.

## Organized programs

| Program | Source cells | Purpose |
|---|---:|---|
| `agents/table_driven_vacuum.py` | Agents 5–7 | Table lookup plus interactive vacuum simulation |
| `agents/simple_reflex_vacuum.py` | Agents 9–10 | Rule-based vacuum agent plus simulation |
| `agents/model_based_vacuum.py` | Agents 12–13 | Stateful two-room vacuum agent plus simulation |
| `python_basics/input_examples.py` | Basics 3–6 | Assignment, text/number input, and birth-year validation |
| `python_basics/conditionals.py` | Basics 8–9 | Basic and multi-branch conditionals |
| `python_basics/loops_and_ranges.py` | Basics 13–26 | Iteration over collections, strings, indexes, and ranges |
| `python_basics/arithmetic_function.py` | Basics 28–30 | Arithmetic function and calls |
| `python_basics/fibonacci.py` | Basics 31–32 | Fibonacci function and example |
| `python_basics/sequence_operations.py` | Basics 33–40 | Concatenation and sequence summation |
| `python_basics/multiplication_table.py` | Basics 41–43 | Multiplication-table function and examples |
| `search/romania_map_demo.py` | Search 2–7 | Romania graph plus dictionary-access demonstrations |
| `search/breadth_first_search.py` | Search 2, 10–11 | Complete graph definition, BFS function, and example search |

## Analysis of the notebooks

### Agents

The agent notebook contains three genuinely separate programs, not seven:

1. The table-driven program defines an action table, an agent function, and a simulation.
2. The simple-reflex program selects an action directly from the current room and condition.
3. The model-based program remembers both rooms and pauses after its internal model says both are clean.

The so-called table-driven implementation stores percept history but never uses the history for lookup. Its action table is keyed only by the current percept, making its behavior closer to a simple lookup-based reflex agent.

### Python basics

Most short cells are demonstrations that depend on nearby cells. For example, function calls must stay with their function definitions, and loop examples using `numbers` must stay with the cell that creates `numbers`. They are grouped accordingly.

The empty exercise cells were excluded because `# code here` is a placeholder, not an implementation. The birth-year example still uses the notebook’s fixed year 2022, and `addValues` retains the original variable name `sum`, which shadows Python’s built-in function.

### Search

The map lookup cells form one dictionary demonstration. The BFS function requires the map definition, so the runnable BFS file includes both.

The notebook requests a DFS implementation but provides only `# code dfs here`. Therefore, there is no DFS code to extract or combine. BFS also checks the goal when generating neighbors, and it does not specially handle the case where the starting city is already the destination.

## Running the programs

Each file is self-contained. Interactive examples run under a `__main__` guard, so functions can also be imported without immediately starting an input loop.
