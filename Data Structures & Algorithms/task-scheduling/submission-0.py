from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-count for count in freq.values()]

        heapq.heapify(heap)

        time = 0

        while heap:
            temp = []

            for i in range(n+1):

                if heap:
                    count = heapq.heappop(heap)
                    count += 1

                    if count < 0:
                        temp.append(count)
                
                time += 1

                if not heap and not temp:
                    break

            for count in temp:
                heapq.heappush(heap, count)
            
        return time


        