import mod_1 # when run, it returns "this is mod 1`s name -> mod_1"
# if we set the function in mod_1 in place, and run it, it means that the name of mod_1 = __main__ only when mod_1 is being run through mod_1 file, rather than through a different file.

print("This is mod 2`s name -> " + __name__) # This is mod 2`s name -> __main__

# allows us to identify if it is run by python itself "main" or by another file.

