[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/d2XNh4FQ)

Messages application

```python
MESSAGE_COST_PER_WORD = 0.01
```

1. Create `get_word_count` function that calculates the number of words in a message. A word is a sequence of characters separated by spaces.
```python
get_word_count("Hello, World!")  # 2
```
2. Create `get_price` function that calculates the price of a message based on the number of words in the message and the `MESSAGE_COST_PER_WORD` constant. return the price of the message.
```python
get_price("Hello, World!")  # 0.02
```
3. Create `get_total_price` function that takes list of messages and returns the total price of all messages.
```python
get_total_price(["Hello, World!", "Hello, Python!"])  # 0.04
```
4. Create `format_message` function that takes a message and sender and returns the "From: {sender}\nMessage: {message}". If sender or message is empty, return `"Invalid Message"` to indicate that the message is invalid.
```python
format_message("Hello, World!", "Alice")  # "From: Alice\nMessage: Hello, World!"
```
5. Create `format_messages` function that takes list of messages and sender and returns the list of formatted messages.
```python
format_messages(["Hello, World!", "Hello, Python!"], "Alice")  # ["From: Alice\nMessage: Hello, World!", "From: Alice\nMessage: Hello, Python!"]
```