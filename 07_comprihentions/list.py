chai_types = [
    "masala chai",
    "Iced lemon tea",
    "Iced tulsi tea",
    "lemon tea"
]

chai_order = [tea for tea in chai_types if "Iced" in tea]

print(chai_order)

chai_order = [tea for tea in chai_types if len(tea) < 12]

print(chai_order)