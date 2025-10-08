import pyfiglet

def init(message="pttextutils"):

    formatted_message = pyfiglet.figlet_format(message)
    print (formatted_message)


def word_count(text):

    words = text.split()
    return len(words)

if __name__ == "__main__":
    init()

    
