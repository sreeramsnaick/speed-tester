import time
print("You have 30 seconds to type as much as you can.")
input("Press Enter when you're ready to start...")
print("\nStart typing now:\n")
start_time = time.time()
typed_text = ""
while time.time() - start_time < 30:
    try:
        line = input()
        typed_text += line + " "
    except:
        break 

word_count = len(typed_text.strip().split())

print("\nTime's up!")
print(f"You typed {word_count} words in 30 seconds.")
