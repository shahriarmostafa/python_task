"""Breadth-first search over the Romania road map."""

from collections import deque

from romania_map_demo import ROMANIA_MAP


def breadth_first_search(start, destination, graph):
    """Return the first breadth-first path found, its cost, and expansion order."""
    frontier = deque([(start, 0, [start])])
    reached = {start}
    expansion_order = []
    while frontier:
        city, path_cost, path = frontier.popleft()
        expansion_order.append(city)
        if city == destination:
            return {
                "City": city,
                "Path cost": path_cost,
                "Path": path,
                "Expansion order": expansion_order,
            }

        for neighbor, edge_cost in graph[city].items():
            if neighbor not in reached:
                reached.add(neighbor)
                frontier.append(
                    (neighbor, path_cost + edge_cost, path + [neighbor])
                )

    return None


if __name__ == "__main__":
    result = breadth_first_search("Arad", "Bucharest", ROMANIA_MAP)
    print(result)
