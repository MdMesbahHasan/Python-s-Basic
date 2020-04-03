def voter(age):
    if age<18:
        raise ValueError("Invalid voter")
    return "you are allowed to vote"
try:
    print(voter(19))
    print(voter(22))
except ValueError as e:
    print(e)

