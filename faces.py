def convert(message):
    
    words = message.split( " ")
    emojis = {
    ":)" : "😀",
    ":(" : "😞",
    }
    outcome = " "
    print(words)
    for word in words:
        print(word)
        outcome += emojis.get(word, word) + " "
    print(outcome)

message = input("> ")
convert(message)