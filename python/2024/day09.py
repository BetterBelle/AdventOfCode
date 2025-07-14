INPUT: list[int] = [int(num) for num in open("2024/day09.txt").read().strip()]

class File():
    def __init__(self, id: int, start: int, end: int):
        self.id: int = id
        self.mem_locations = [i for i in range(start, end)]

    def size(self):
        return len(self.mem_locations)

    def move_memory_locations(self, targets: list[int]) -> list[int]:
        if len(targets) != self.size():
            raise NotImplemented()

        old_locs = self.mem_locations.copy()
        self.mem_locations = targets.copy()
        return old_locs

    def checksum(self):
        return sum(self.mem_locations) * self.id

    def start(self):
        return self.mem_locations[0]

    def end(self):
        return self.mem_locations[-1]

    def __repr__(self):
        return f'{self.id}: {self.mem_locations}'


class FileSystem():
    def __init__(self):
        self.files: list[File] = []
        self.free_memory: list[int] = []
        self.size = 0
        idx = 0
        id = 0
        for i, size in enumerate(INPUT):
            if i % 2 == 0:
                self.files.append(File(id, idx, idx + size))
                id += 1
            else:
                for loc in range(idx, idx + size):
                    self.free_memory.append(loc)

            idx += size
            self.size += size

    def free_blocks(self) -> list[list[int]]:
        free_blocks = []
        current_block = [self.free_memory[0]]
        for free in self.free_memory[1:]:
            if current_block[-1] == free - 1:
                current_block.append(free)
            else:
                free_blocks.append(current_block)
                current_block = [free]
        return free_blocks

    def reorganize_contiguous(self):
        # start with last file 
        for file in reversed(self.files):
            # the targets are the lowest memory spaces within the free space 
            # and the current file
            target_locs = self.free_memory[:file.size()] + file.mem_locations
            target_locs.sort()
            target_locs = target_locs[:file.size()]
            # only move the file if the beginning of the target locations comes before
            # the start of the file
            if target_locs[0] < file.start():
                old_locations = file.move_memory_locations(target_locs)
                for new_mem_loc in file.mem_locations:
                    if new_mem_loc in self.free_memory:
                        self.free_memory.remove(new_mem_loc)

                # determine the newly free spots; 
                # the old locations which aren't in the targets 
                newly_free = [n for n in old_locations if n not in file.mem_locations]
                self.free_memory.extend(newly_free)
                self.free_memory.sort()

    def reorganize_blocks(self):
        for file in reversed(self.files):
            # the targets are the smallest, contiguous memory spaces large enough to fit 
            # the file within them in the free memory space 
            for block in self.free_blocks():
                if len(block) >= file.size() and block[0] < file.mem_locations[0]:
                    target_locs = block[:file.size()]
                    old_locs = file.move_memory_locations(target_locs)
                    for new_mem_loc in file.mem_locations:
                        if new_mem_loc in self.free_memory:
                            self.free_memory.remove(new_mem_loc)

                    newly_free = [n for n in old_locs if n not in file.mem_locations]
                    self.free_memory.extend(newly_free)
                    self.free_memory.sort()
                    break

    def calculate_checksum(self):
        res = 0
        for file in self.files:
            res += file.checksum()
        return res

    def __repr__(self):
        mem_repr = ['' for _ in range(self.size)]
        for file in self.files:
            for idx in file.mem_locations:
                mem_repr[idx] = str(file.id)

        for loc in self.free_memory:
            mem_repr[loc] = '.'

        return ''.join(mem_repr)
            

filesystem = FileSystem()
filesystem.reorganize_contiguous()
print(filesystem.calculate_checksum())
filesystem = FileSystem()
filesystem.reorganize_blocks()
print(filesystem.calculate_checksum())



