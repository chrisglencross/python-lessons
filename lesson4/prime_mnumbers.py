
maximum=1000000

# Create an empty set and put every number into it
prime_numbers=set([])
for number in range(2, maximum):
    prime_numbers.add(number)

# Count through the times tables between 2 and 1000 and remove all the answers
for times_table in range(2, maximum):
    for value in range(2*times_table, maximum, times_table):
        prime_numbers.discard(value)

# Copy the prime numbers into a list, sort and print
sorted_primes=list(prime_numbers)
sorted_primes.sort()
print("There are ", len(sorted_primes), "prime numbers less than", maximum)
print(sorted_primes)
