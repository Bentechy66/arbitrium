# Arbitrium - The Easy Menu System For Python

## Install
`pip install arbitrium`

## Usage
```
from arbitrium import menu
from os import exit

@menu(["Option One", "Option Two", "Final Option"])
def choice_handler(choice):
  if choice == 1:
    # Option One Selected
    pass
  if choice == 2:
    # Option Two Selected
    pass
  if choice == 3:
    # Final Option Selected
    exit(1)

# Calling the choice handler will also print the menu
choice_handler()
```
Will produce:
```
1) Option One
2) Option Two
99) Final Option
Please enter your choice:
```

**NOTE: Final Option will always be 99. It will run the choice handler once and then exit the choice handler function.**

## Authentication
Arbitrium provides an easy system for adding auth to your menu:
```
from arbitrium import menu, requires_auth

def auth_function():
  u = input("Enter username: ")
  p = input("Enter password: ")
  # Check Passwords
  if password_correct:
    return True
  return False

@requires_auth(auth_function, True)
@menu(["Option One", "Option Two", "Exit"])
def choice_handler(choice):
  [...]

choice_handler()
```
Will run auth_function before a user can see or select any menu options. If auth_function returns True, the menu will run, if it returns False, it will exit with an error message.
Alternatively,
```
from arbitrium import menu, requires_auth

def auth_function(username, password):
  # Check Passwords
  if password_correct:
    return True
  return False

@requires_auth(auth_function(input("Please Enter Username"), input("Please Enter Password")))
@menu(["Option One", "Option Two", "Exit"])
def choice_handler(choice):
  [...]

choice_handler()
```
You can supply the first argument with a boolean - if true, the function will run. Else, it won't.
If you supply the first argument with a function, you must supply the second argument with True.
