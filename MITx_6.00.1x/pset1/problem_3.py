s = 'bnhsriacfbwougdwmuxjx'

longest = ""

for i in range(len(s) - 1):
    # Create a string in which we add the first character of the iteration, to smooth things out.
    new_substring = s[i]
    # Check whether the UNICODE value of the next character is higher than the current one
    while ord(s[i + 1]) >= ord(s[i]):
        # Start building the substring
        new_substring += s[i + 1]
        # Progresses the iteration
        i += 1
        # Control case to not index out of the string. It might be possible to clean this up.
        if i == len(s) - 1:
            break
    # Checks whether the current substring is longest than the previously saved one. If it is, assign it.
    if len(new_substring) > len(longest):
        longest = new_substring


print("Longest substring in alphabetical order is: ", longest)
