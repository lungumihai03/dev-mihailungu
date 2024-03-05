sequence = input("Enter a sequence of numbers, separated by spaces: ").split()
sequence = [int(num) for num in sequence]
max_length = 0
start_index = 0
end_index = 0
for i in range(len(sequence)):
    for j in range(i, len(sequence)):
        if sequence[i] == sequence[j]:
            length = j - i + 1
            if length > max_length:
                max_length = length
                start_index = i
                end_index = j
longest_subsequence = sequence[start_index:end_index+1]
print("The longest subsequence is:", longest_subsequence)
