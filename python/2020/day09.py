inp_file = open('2020/day09.txt')
nums = []
for line in inp_file:
    nums.append(int(line))


def part1():
    for i in range(25, len(nums)):
        prev_nums = nums[i-25:i]
        prev_nums.sort()
        start = 0
        end = len(prev_nums) - 1

        while prev_nums[start] + prev_nums[end] != nums[i]:
            if prev_nums[start] == prev_nums[end]:
                return nums[i]
            elif prev_nums[start] + prev_nums[end] > nums[i]:
                end -= 1
            elif prev_nums[start] + prev_nums[end] < nums[i]:
                start += 1
            
    return -1


def part2(weak_number):
    weak_number_location = nums.index(weak_number)
    for list_size in range(2, weak_number_location):

        for i in range(weak_number_location):

            list_to_check = nums[i:i+list_size]

            if sum(list_to_check) == weak_number:
                return max(list_to_check) + min(list_to_check)

    return -1



weak_number = part1()
print (weak_number)
print (part2(weak_number))
