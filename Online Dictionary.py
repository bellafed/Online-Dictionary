meme_dict = {
            "CRINGE": "Something strange or embarassing",
            "LOL": "Something very funny", "WDYM": "What do you mean?", "HBU": "How about you?", "WYD": "What are you doing?"
            }
print("Hello, this is an online dictionay! Insert the word you don't know the meaning of!")
word=input("Which word would you like to know the meaning of?")
if word in meme_dict.keys():
    print(meme_dict [word])
else:
    print("Word undetected")
