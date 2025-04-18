from django.shortcuts import render

def problems(request):
    categories = [
        "Array", "String", "Hash Table", "Dynamic Programming", "Math", "Sorting",
        "Greedy", "Depth-First Search", "Database", "Binary Search", "Matrix", "Tree",
        "Breadth-First Search", "Bit Manipulation", "Two Pointers", "Prefix Sum",
        "Heap (Priority Queue)", "Binary Tree", "Simulation", "Stack", "Graph",
        "Counting", "Sliding Window", "Design", "Enumeration", "Backtracking",
        "Union Find", "Linked List", "Ordered Set", "Number Theory", "Monotonic Stack",
        "Segment Tree", "Trie", "Bitmask", "Combinatorics", "Queue",
        "Divide and Conquer", "Recursion", "Memoization", "Binary Indexed Tree",
        "Geometry", "Binary Search Tree", "Hash Function", "String Matching",
        "Topological Sort", "Shortest Path", "Rolling Hash", "Game Theory",
        "Interactive", "Data Stream", "Monotonic Queue", "Brainteaser",
        "Randomized", "Merge Sort", "Doubly-Linked List", "Counting Sort",
        "Iterator", "Concurrency", "Probability and Statistics", "Quickselect",
        "Suffix Array", "Bucket Sort", "Minimum Spanning Tree", "Line Sweep",
        "Shell", "Reservoir Sampling", "Strongly Connected Component",
        "Eulerian Circuit", "Radix Sort", "Rejection Sampling",
        "Biconnected Component"
    ]
    
    return render(request, 'problems_page/problems_page.html', {'categories': categories})
