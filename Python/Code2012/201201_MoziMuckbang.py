import heapq
def solution(food_times, k):
    answer = 0
    if sum(food_times)<=k:
        return -1
    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap,(food_times[i],i+1))
    tsum = 0
    previous = 0
    length = len(food_times)

    while tsum + (heap[0][0]-previous)*length <= k:
        ntime = heapq.heappop(heap)[0]
        tsum += (ntime-previous) * length
        length -= 1
        previous = ntime

    rtime = sorted(heap, key = lambda x: x[1])
    answer = rtime[(k-tsum)%length][1]
    return answer