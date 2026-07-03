seat_type = input("enter your seat type [sleeper/AC/general/luxury]: ").lower()

match seat_type:
    case "sleeper":
        print("comes with beds")
    case "ac":
        print("comes with an ac")
    case "general":
        print("the cheapest option there is")
    case "luxury":
        print("all services with meal included")
    case _:
        print("invalid case(option).")