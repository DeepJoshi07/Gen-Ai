student = {
    "name":"deep",
    "age":23,
    "marks":98
}

try:
    print(student["height"])
except:
    print("provided value does not exists!")

print("-------------------------------------------------")

def serve_chai(chai):
    try:
        print(f"preparing {chai} chai.")
        if chai == "unknown":
            raise ValueError("provided chai does not being made here.")
    except ValueError as v:
        print("Value Error:",v)
    else:
        print("chai is being given to customer.")
    finally:
        print("chai has been served.")

serve_chai("masala")
print("----------------------------------")
serve_chai("unknown")
