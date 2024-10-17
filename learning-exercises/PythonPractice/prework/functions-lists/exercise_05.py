# Mad Libs
# https://en.wikipedia.org/wiki/Mad_Libs

# 1. Copy your read_required_string function
# definition into this file.

# 2. Define a mad_lib function.
# Collect three required strings from the user:
# `adjective`, `verb`, and `noun`.
# Use them to print this message.
# f"The {adjective} squirrel {verb} away with the {noun}."
# (You can certainly get more creative with your Mad Libs.)

# 3. Call the mad_lib function at least three times.


def mad_lib(str):
    value = input(str)
    while not value.strip():
        print("Error String is empty")
        value = input(str)
    
    return value

adjective = mad_lib("Write one adjective:")
verb = mad_lib("Write one verb:")
noun = mad_lib("Write one noun:")

print(f"The {adjective} squirrel {verb} away with the {noun}.")
