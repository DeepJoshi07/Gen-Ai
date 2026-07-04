users = [
    {"id":1,"total":150,"coupon":"F20"},
    {"id":2,"total":100,"coupon":"F50"},
    {"id":3,"total":40,"coupon":"P40"},
]

discounts = {
    "P40":(0.4,0),
    "F50":(0,50),
    "F20":(0.2,0)
}

for user in users:
    percent,fixed = discounts.get(user["coupon"])
    discount = user["total"] * percent + fixed
    print(f"{user['id']} paid {user["total"]} and got discount for next visit of rupees {discount}")
