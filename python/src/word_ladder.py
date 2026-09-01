from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
            
        word_len = len(beginWord)
        
        # 1. Group words by generic patterns, e.g., "h*t": ["hot", "hit"]
        pattern_map = defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)
                
        # 2. BFS initialization
        # Queue stores tuples of (current_word, current_path_length)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        # 3. Standard BFS traversal
        while queue:
            current_word, level = queue.popleft()
            
            # If we reached the target, return the step count
            if current_word == endWord:
                return level
                
            # Check all possible wildcard patterns for the current word
            for i in range(word_len):
                pattern = current_word[:i] + "*" + current_word[i+1:]
                
                # Visit all neighbors sharing this pattern
                for neighbor in pattern_map[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                        
                # Optional: Clear the list to optimize memory and redundant lookups
                pattern_map[pattern] = []
                
        return 0
