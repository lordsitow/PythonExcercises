def reverse(word):
    return ' '.join(word.split()[::-1])

print(reverse(input('Gimme a phraze:')))