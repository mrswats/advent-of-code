## --- Day 8: Treetop Tree House ---

The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a [tree house](https://en.wikipedia.org/wiki/Tree_house).

First, determine whether there is enough tree cover here to keep a tree house _hidden_. To do this, you need to count the number of trees that are _visible from outside the grid_ when looking directly along a row or column.

The Elves have already launched a [quadcopter](https://en.wikipedia.org/wiki/Quadcopter) to generate a map with the height of each tree (your puzzle input). For example:

```
30373
25512
65332
33549
35390

```

Each tree is represented as a single digit whose value is its height, where `0` is the shortest and `9` is the tallest.

A tree is _visible_ if all of the other trees between it and an edge of the grid are _shorter_ than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are _visible_ - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the _interior nine trees_ to consider:

- The top-left `5` is _visible_ from the left and top. (It isn't visible from the right or bottom since other trees of height `5` are in the way.)
- The top-middle `5` is _visible_ from the top and right.
- The top-right `1` is not visible from any direction; for it to be visible, there would need to only be trees of height _0_ between it and an edge.
- The left-middle `5` is _visible_, but only from the right.
- The center `3` is not visible from any direction; for it to be visible, there would need to be only trees of at most height `2` between it and an edge.
- The right-middle `3` is _visible_ from the right.
- In the bottom row, the middle `5` is _visible_, but the `3` and `4` are not.

With 16 trees visible on the edge and another 5 visible in the interior, a total of `*21*` trees are visible in this arrangement.

Consider your map; _how many trees are visible from outside the grid?_
