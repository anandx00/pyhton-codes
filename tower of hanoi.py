def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk {n} from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)

# Example usage:
n = 3  # Number of disks
tower_of_hanoi(1, 'A', 'C', 'B')  # 'A', 'B', and 'C' are the rod names
