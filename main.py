def get_word_count(message):
    words = message.split()
    return len(words)
message = "Hello, how are you doing?"
print(get_word_count(message))  

# 2
MESSAGE_COST_PER_WORD = 0.10  

def get_price(message):
    word_count = len(message.split())
    price = word_count * MESSAGE_COST_PER_WORD
    return price
message = "Hello, how are you doing today?"
print(get_price(message))  
# 3
