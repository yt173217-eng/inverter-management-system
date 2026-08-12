categories_input = "Audio, Electronics, Computer"
categories = [c.strip().lower() for c in categories_input.split(",") if c.strip()]
print(categories)                 #→ breaks into pieces               This condition ensures empty strings are ignored.