class Solution:
    def queue_loop(self, queue: list) -> int:
        index = 0
        while len(queue) > 1:
            remove_list = []
            for item in queue:
                index += 1
                if index == 3:
                    remove_list.append(item)
                    index = 0
            for item in remove_list:
                queue.remove(item)
        return queue[0]


if __name__ == '__main__':
    queue_input = list(range(1, 10))
    solution = Solution()
    print(solution.queue_loop(queue_input))
