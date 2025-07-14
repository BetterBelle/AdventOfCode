INPUT: list[int] = [int(num) for num in open("2024/day09.txt").read().strip()]

def print_memory(memory: list[int]):
    print(''.join(['.' if n == 0 else str(n-1) for n in memory]))

def generate_memory() -> list[int]:
    memory = []
    id = 1
    for i, size in enumerate(INPUT):
        if i % 2 == 0:
            for _ in range(size):
                memory.append(id)
            id += 1
        else:
            for _ in range(size):
                memory.append(0)

    return memory


def move_memory(memory: list[int]) -> list[int]:
    free_space = 0
    to_move = len(memory) - 1
    new_memory = memory.copy()

    while True:
        # move free_space to next free space 
        while new_memory[free_space] != 0:
            free_space += 1

        # find next item to move 
        while new_memory[to_move] == 0:
            to_move -= 1

        # the next free space is after the current memory to move means
        # the memory is one contiguous chunk; we're done
        if to_move < free_space:
            break

        # swap
        new_memory[free_space] = new_memory[to_move]
        new_memory[to_move] = 0

    return new_memory

def move_blocks(memory: list[int]) -> list[int]:
    to_move_end = len(memory) - 1
    new_memory = memory.copy()

    while to_move_end >= 0:
        # find next memory block to move
        while new_memory[to_move_end] == 0:
            to_move_end -= 1

        # found memory block to move, find start 
        to_move_start = to_move_end 
        # when this isn't true, we've reached the end of the memory block
        while new_memory[to_move_start - 1] == new_memory[to_move_end]:
            to_move_start -= 1

        block_to_move_size = to_move_end - to_move_start + 1
        # find next free memory block 
        free_block_start = 0
        # if the free block's start comes after the block to move's start, there's no available space
        # therefore only search if free block start comes before to move start
        while free_block_start < to_move_start:
            while new_memory[free_block_start] != 0:
                free_block_start += 1

            if free_block_start > to_move_start:
                break

            # free block found, get the end of the free block
            free_block_end = free_block_start
            # when this isn't true, we've reached the end of the free block
            while new_memory[free_block_end + 1] == 0:
                free_block_end += 1

            # found end of block, ensure large enough to fit block to move
            if free_block_end - free_block_start + 1 >= block_to_move_size:
                # move the block
                while to_move_end >= to_move_start:
                    new_memory[free_block_start] = new_memory[to_move_end]
                    new_memory[to_move_end] = 0
                    free_block_start += 1
                    to_move_end -= 1

                # when moved, set the free block start to the move start to trigger loop end
                free_block_start = to_move_start
            else:
                # if not large enough, continue searching for valid free block
                # starting from the free block's end + 1
                free_block_start = free_block_end + 1

        # whether the block was moved or not
        # we move the to move end to the start of the block - 1 to avoid re-checking the 
        # same section of memory 
        to_move_end = to_move_start - 1

    return new_memory


def calculate_checksum(memory: list[int]):
    res = 0
    for idx, id in enumerate(memory):
        if id != 0:
            res += idx * (id - 1)

    return res


memory = generate_memory()
part_one_memory = move_memory(memory)
part_two_memory = move_blocks(memory)
print(calculate_checksum(part_one_memory))
print(calculate_checksum(part_two_memory))



