def check_valid(choices, selection):
  '''Checks if {choice} is a valid selection from a menu, given {selections}

	returns -> bool:is_valid'''
  try:
    selection = int(selection)
  except:
    return False

  if selection == 99:
    return True # 99 is always back / quit

  if not selection in list(range(1, len(choices) + 1)): # If a valid number based on the length of selection
    return False

  return True

def menu(choices):
  '''Decorator to generate a menu, given a list of {choices}. The last choice will always be option 99, which is always  "exit", "quit" or "back"

	returns -> function:menu_wrapper'''
  def menu_wrapper(func):
    def inner_wrapper(*args, **kwargs):
      exit_option = choices[-1]
      new_choices = choices[:-1] # Don't redefine into global ns
      menu = "\n"
      for index, option in enumerate(new_choices):
        menu += f"{index + 1}) {option}\n" # Generate menu string

      menu += f"99) {exit_option}" # Add exit option
      while True:
        print(menu)
        choice = input("Please enter your choice: ")
        if not check_valid(new_choices, choice):
          print("\n-----\nThat's not a valid choice!")
        else:
          if choice != "99":
            func(int(choice)) # If user doesn't want to exit, run the choice handler
          else:
            return func(int(choice)) # User wants to quit, return the function so we can wrap it again later
    return inner_wrapper
  return menu_wrapper
