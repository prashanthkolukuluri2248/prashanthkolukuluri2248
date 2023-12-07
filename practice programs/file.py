# Read input
n_english = int(input())
english_subs = set(map(int, input().split()))

n_french = int(input())
french_subs = set(map(int, input().split()))

# Find students subscribed to either English or French, but not both
either_or_subs = english_subs ^ french_subs

# Output the total number of students with subscriptions to either English or French, but not both
print(len(either_or_subs))
