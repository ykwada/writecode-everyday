# Review Queue

Problems to re-solve from scratch. Rule: 5 minutes, no hints, no looking at the old solution.
Solved within 5 min -> delete the line. Otherwise move the date forward a few days.

One review before the daily new problem.

## Priority 1 — got stuck on the core idea

| # | Problem | Pattern | What broke | Next |
|---|---------|---------|------------|------|
| 026 | remove_duplicates_from_sorted_array | two pointers | Tried `pop()` in a loop; index shifting | |
| 035 | search_insert_position | binary search | `mid` not excluded -> infinite loop; missed `return left` | |
| 104 | maximum_depth_of_binary_tree | recursion | Passed a counter as an argument; child values never reach the parent | |
| 110 | balanced_binary_tree | recursion | Mixed return types; needed a helper returning `(height, ok)` | |
| 112 | path_sum | recursion | Tried to subtract on the way up instead of passing down | |
| 169 | majority_element | hash map | Wrote `counts[key]` / `counts[value]` inside `items()` loop; compared against the element's own count instead of `len(nums)` | |
| 203 | remove_linked_list_elements | linked list + dummy | Moved `current` instead of relinking `prev.next`; no dummy node; returned `head` | |
| 205 | isomorphic_strings | hash map (bidirectional) | Filled all four slots with dict lookups instead of the loop variables | |

## Priority 2 — logic was close, details broke

| # | Problem | Pattern | What broke | Next |
|---|---------|---------|------------|------|
| 027 | remove_element | two pointers | `slow` semantics: last kept element vs next write position | |
| 028 | find_the_index_of_the_first_occurrence | brute force | `return -1` inside the loop; sliced with the wrong length | |
| 066 | plus_one | carry | `insert` placed inside the loop instead of after it | |
| 067 | add_binary | carry | `and` vs `or` in the while condition; missing index guards | |
| 083 | remove_duplicates_from_sorted_list | linked list | Assigned `.val` instead of relinking `.next` | |
| 088 | merge_sorted_array | two pointers from end | Missing `i >= 0` guard and pointer decrements | |
| 118 | pascals_triangle | 2D build | Indexed the previous row as a whole instead of its elements | |
| 168 | excel_sheet_column_title | base conversion (1-indexed) | `join()` with no argument; forgot to reverse; unsure why `-1` is needed | |
| 217 | contains_duplicate | hash set | Pasted the 026 two-pointer solution; assumed sorted input | |

## Priority 3 — skeleton was given, never written from scratch

069 sqrt_x (binary search) / 094 binary_tree_inorder_traversal (recursion) /
100 same_tree (recursion) / 108 convert_sorted_array_to_bst (divide & conquer) /
121 best_time_to_buy_and_sell_stock (greedy) /
190 reverse_bits (bit manipulation — string version only) /
191 number_of_1_bits (bit manipulation — string version only)

## Solved clean — revisit later, not urgent

| # | Problem | Pattern | Note |
|---|---------|---------|------|
| 171 | excel_sheet_column_number | base conversion | First try, no hints. Pairs with 168 (decompose vs compose) |
| 206 | reverse_linked_list | linked list | First try. High-frequency; target is writing the 4 lines from memory |

## Open follow-ups (not review — new work)

- 190 / 191: rewrite with bit operators (`<<`, `>>`, `& 1`, `|`). Learn shift operators standalone first.
- 190: memoization follow-up (split 32 bits into 4 bytes, cache 256 entries).
- 169: Boyer-Moore voting for O(1) space.

## Graduated

_(move lines here, or just delete them)_
