# write a program to find out whether the given post is talking about harry or not in uppercase or lowercase
def is_talking_about_harry(post):
    target_word = "harry"

    # Convert both post and target_word to lowercase for case-insensitive comparison
    post_lower = post.lower()
    target_lower = target_word.lower()

    if target_lower in post_lower:
        return True
    else:
        return False

# Test the function
post1 = "I love Harry Potter!"
post2 = "Who is this Harry you're talking about?"
post3 = "The weather is sunny today."
post4 = "harry"

print(is_talking_about_harry(post1))  # True
print(is_talking_about_harry(post2))  # True
print(is_talking_about_harry(post3))  # False
print(is_talking_about_harry(post4))  # True
