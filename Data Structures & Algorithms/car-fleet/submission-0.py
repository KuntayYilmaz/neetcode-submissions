class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort()
        last_stack = []
        for i in range(len(position) - 1):
            car_1 = pair.pop()
            car_2 = pair.pop()

            if (target - car_1[0]) / car_1[1] >= (target - car_2[0]) / car_2[1]:
                pair.append(car_1)

            else:
                last_stack.append(car_1)
                pair.append(car_2)

        last_stack.append(pair.pop)

        return len(last_stack)


 
        