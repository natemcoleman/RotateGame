import tkinter as tk
import math

class CircleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Changing Circles")

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(expand=True, fill="both")

        self.circles = []  # List to store information about circles

        Main1CenterX = 100
        Main1CenterY = 100

        Main2CenterX = -100
        Main2CenterY = -100

        circle_info = {"size": 200, "angle": 0, "orbit_radius": 100, "color": "white", "centerX": Main1CenterX, "centerY": Main1CenterY}
        self.create_main_circle(circle_info)
        self.create_orbit_circle(circle_info)

        circle_info = {"size": 150, "angle": 0, "orbit_radius": 75, "color": "white", "centerX": Main1CenterX, "centerY": Main1CenterY}
        self.create_main_circle(circle_info)
        self.create_orbit_circle(circle_info)

        circle_info = {"size": 100, "angle": 0, "orbit_radius": 50, "color": "white", "centerX": Main1CenterX, "centerY": Main1CenterY}
        self.create_main_circle(circle_info)
        self.create_orbit_circle(circle_info)
        ###################################

        # circle_info = {"size": 200, "angle": 0, "orbit_radius": 100, "color": "white", "centerX": Main2CenterX,
        #                "centerY": Main2CenterY}
        # self.create_main_circle(circle_info)
        # self.create_orbit_circle(circle_info)
        #
        # circle_info = {"size": 150, "angle": 0, "orbit_radius": 75, "color": "white", "centerX": Main2CenterX,
        #                "centerY": Main2CenterY}
        # self.create_main_circle(circle_info)
        # self.create_orbit_circle(circle_info)
        #
        # circle_info = {"size": 100, "angle": 0, "orbit_radius": 50, "color": "white", "centerX": Main2CenterX,
        #                "centerY": Main2CenterY}
        # self.create_main_circle(circle_info)
        # self.create_orbit_circle(circle_info)


        self.root.bind('<Configure>', self.on_resize)

    def create_main_circle(self, circle_info):
        # Calculate initial position of main circle
        x_center = self.canvas.winfo_reqwidth() / 2 + circle_info["centerX"]
        y_center = self.canvas.winfo_reqheight() / 2 + circle_info["centerY"]

        circle_info["coords"] = (x_center - circle_info["size"] / 2, y_center - circle_info["size"] / 2)

        # Create the main circle on the canvas
        circle = self.canvas.create_oval(*circle_info["coords"],
                                         circle_info["coords"][0] + circle_info["size"],
                                         circle_info["coords"][1] + circle_info["size"],
                                         fill=circle_info["color"], outline="black")

        # Bind click event to change color and start orbit animation
        self.canvas.tag_bind(circle, '<Button-1>', lambda event, info=circle_info: self.change_color(event, info))

        circle_info["circle"] = circle
        self.circles.append(circle_info)

    def create_orbit_circle(self, circle_info):
        # Create the orbiting circle on the canvas
        orbit_circle = self.canvas.create_oval(0, 0, 0, 0, fill="blue", outline="black")
        circle_info["orbit_circle"] = orbit_circle

    def change_color(self, event, circle_info):
        # Change color of the main circle
        self.canvas.itemconfig(circle_info["circle"], fill="green")

        # Move the orbiting circle with animation
        self.animate_orbit(circle_info)

        # Schedule to change back to red after 1 second
        self.root.after(1000, lambda: self.change_back_to_red(circle_info))

    def change_back_to_red(self, circle_info):
        # Change color of the main circle back to red
        self.canvas.itemconfig(circle_info["circle"], fill="white")

    def on_resize(self, event):
        # Update circle positions and sizes when the window is resized
        for circle_info in self.circles:
            circle_info["coords"] = (root.winfo_width() / 2 - circle_info["size"] / 2,
                                     root.winfo_height() / 2 - circle_info["size"] / 2)
            self.canvas.coords(circle_info["circle"], *circle_info["coords"],
                               circle_info["coords"][0] + circle_info["size"],
                               circle_info["coords"][1] + circle_info["size"])
            self.orbit(circle_info)

    def orbit(self, circle_info):
        # Calculate new position of orbiting circle
        x_center = circle_info["coords"][0] + circle_info["size"] / 2
        y_center = circle_info["coords"][1] + circle_info["size"] / 2

        x = x_center + circle_info["orbit_radius"] * math.cos(math.radians(circle_info["angle"]))
        y = y_center + circle_info["orbit_radius"] * math.sin(math.radians(circle_info["angle"]))

        # Update orbiting circle coordinates
        orbit_size = 20  # Size of the orbiting circle
        self.canvas.coords(circle_info["orbit_circle"], x - orbit_size / 2, y - orbit_size / 2,
                           x + orbit_size / 2, y + orbit_size / 2)

    def animate_orbit(self, circle_info):
        # Animate the orbiting circle to complete a full revolution
        for _ in range(36):  # 36 steps for a full revolution (360 degrees)
            circle_info["angle"] += 10  # 10 degrees per step
            self.orbit(circle_info)
            self.root.update()
            self.root.after(50)  # Delay for smoother animation

if __name__ == "__main__":
    root = tk.Tk()
    app = CircleApp(root)
    root.mainloop()
