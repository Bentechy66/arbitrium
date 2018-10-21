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
