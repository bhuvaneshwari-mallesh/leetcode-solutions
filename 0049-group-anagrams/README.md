# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

**Difficulty:** Medium
**Topics:** Array, Hash Table, String, Sorting

## Approach

**Brute force:** for every word, compare it against every group already
formed by checking if it's an anagram of that group's first word (sort
both and compare, or use a character-count check) — O(n) groups to check
per word.

Why it's not ideal: O(n² · k log k) where k is average word length —
comparing each new word against every existing group is wasteful.

**Optimized — sorted string as a hash map key:** two anagrams always
produce the same string when their letters are sorted (`"eat"` and
`"tea"` both sort to `"aet"`). So: sort each word's letters to build a
key, and group all words sharing that key together in a hash map.

Why it works: sorting collapses every anagram of a word down to one
canonical form, which makes "do these words belong in the same group?" an
O(1) hash map lookup instead of a comparison against every existing group.

## Complexity

| | Brute force | Optimized |
|---|---|---|
| Time | O(n² · k log k) | O(n · k log k), n = word count, k = avg word length |
| Space | O(n · k) | O(n · k) |

## Key pattern

Canonical form as a hash key — turn a messy equivalence check ("are these
two things the same up to reordering?") into a direct lookup by mapping
every equivalent input to one shared representation.
