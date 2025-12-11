class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        from collections import defaultdict

        rows = defaultdict(list)
        cols = defaultdict(list)

        # Collect buildings in rows/columns
        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)

        # Precompute min/max for each row and col
        row_min = {}
        row_max = {}
        col_min = {}
        col_max = {}

        for r in rows:
            row_min[r] = min(rows[r])
            row_max[r] = max(rows[r])

        for c in cols:
            col_min[c] = min(cols[c])
            col_max[c] = max(cols[c])

        # Count covered buildings
        count = 0
        for x, y in buildings:
            if (
                col_min[y] < x < col_max[y] and
                row_min[x] < y < row_max[x]
            ):
                count += 1

        return count
