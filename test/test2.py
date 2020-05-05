def progress_count(self, index: int, total: int) -> int:
    percentage = int((index / total) * 100)
    return percentage


for i in range(1, 10):
    progress_count("", i+1, 10)
