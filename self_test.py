import mendel

# A basic template to define the traits of a creature
# Based on Mendel's origanal Pisum Sativum

creature_template = {
    "Height": {
        "type": "mendel",
        "letter": "H",
        "dom": "Tall",
        "res": "Short"
    },
    "Seed color": {
        "type": "mendel",
        "letter": "Y",
        "dom": "Yellow",
        "res": "Green"
    }
}

e, c, x = mendel.compile_creature(creature_template)

print(e("HhYy"))

print(x("HhYy", "HhYy"))