import turtle

# All units in kilometers.
planets8 = [
    {"name": "mercury", "radius": 2439.7, "color": "lightgrey", "moons": []},
    {"name": "venus", "radius": 6051.8, "color": "orange", "moons": []},
    {"name": "earth", "radius": 6371, "color": "blue",
     "moons": [{"name": "moon", "radius": 1737.4, "color": "lightgrey"}]},
    {"name": "mars", "radius": 3389.5, "color": "red",
     "moons": [{"name": "phobos", "radius": 11.1, "color": "grey"},
              {"name": "deimos", "radius": 6.3, "color": "grey"}]},
    {"name": "jupiter", "radius": 69911, "color": "orange",
     "moons": [{"name": "ganymede", "radius": 2631.2, "color": "grey"},
              {"name": "callisto", "radius": 2410.3, "color": "darkgrey"},
              {"name": "io", "radius": 1830, "color": "lightgreen"},
              {"name": "europa", "radius": 1560.8, "color": "green"}]},
    {"name": "saturn", "radius": 58232, "color": "yellow",
     "moons": [{"name": "titan", "radius": 2574, "color": "orange"},
              {"name": "rhea", "radius": 763.5, "color": "grey"},
              {"name": "iapets", "radius": 734.3, "color": "darkgrey"},
              {"name": "dione", "radius": 561.4, "color": "grey"}]},
    {"name": "uranus", "radius": 25362, "color": "lightblue",
     "moons": [{"name": "titania", "radius": 788.4, "color": "grey"},
              {"name": "oberon", "radius": 761.4, "color": "grey"},
              {"name": "umbriel", "radius": 584.7, "color": "darkgrey"},
              {"name": "ariel", "radius": 578.9, "color": "grey"}]},
    {"name": "neptune", "radius": 24622, "color": "blue",
     "moons": [{"name": "triton", "radius": 1352.6, "color": "salmon"},
              {"name": "proteus", "radius": 210, "color": "grey"},
              {"name": "nereid", "radius": 170, "color": "grey"},
              {"name": "larissa", "radius": 97, "color": "grey"}]},  # :(
]

def draw_body(body, zoom):
    """This function draws a filled-in circle based on the 'radius' and 
    'color' keys of the dictionary `body`. The drawing is scaled by the 
    factor `zoom`."""
    turtle.dot(2 * body["radius"] * zoom, body["color"])

def separate_bodies(body, prev_body_radius, zoom, sep):
    """This function moves the turtle the appropriate distance to avoid 
    overlap between two drawings. Minimal separation given by `sep`."""
    distance = (body["radius"] + prev_body_radius) * zoom + sep
    turtle.forward(distance)
    return distance

def draw_planets(system, zoom):
    separation = 20  # Distance between planets.
    moon_separation = 10  # Distance between moons and their planets.

    prev_planet_radius = 0
    for index, planet in enumerate(system):
        if index > 0:
            prev_planet_radius = system[index - 1]["radius"]
        separate_bodies(planet, prev_planet_radius, zoom, separation)
        draw_body(planet, zoom)

        # Draw moons
        turtle.left(90)
        distance = 0  # How far has the turtle moved to draw the moons?
        prev_radius = planet["radius"]
        for index2, moon in enumerate(planet["moons"]):
            if index2 > 0:
                prev_radius = planet["moons"][index2 - 1]["radius"]
            distance += separate_bodies(moon, prev_radius, zoom, moon_separation)
            draw_body(moon, zoom)
        turtle.forward(-distance)
        turtle.right(90)

def draw_system(system, zoom):
    # Program inputs.
    print('Welcome to the 107L2 Radially-Precise Planetarium!')
    turtle.tracer(False)

    turtle.bgcolor('black')  # Black background
    turtle.penup()  # Hide pen

    # Draw (2 * decoration) ** 2 stars.
    decoration = 15
    scale = max(turtle.window_height(), turtle.window_width())
    for col in range(-decoration, decoration):
        for row in range(-decoration, decoration):
            # row / decoration gives is a number between -1 and 1
            # the `scale` variable determines the space between stars
            y = row / decoration * scale
            # shift every other row of stars by 50%
            x = ((col + 0.5 * (row % 2)) / decoration) * scale

            turtle.goto(x, y)

            # make every other star's radius larger
            turtle.dot(1 + col % 2, 'white')
    turtle.goto(0, 0)

    # Draw planets starting near the screen's edge.
    turtle.forward(-turtle.window_width() / 2 * 0.9)
    draw_planets(system, zoom)

    turtle.done()

if __name__ == "__main__":
    draw_system(planets8, 0.003)
