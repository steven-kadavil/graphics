from proj1.model import *

class Scene:
    def __init__(self, app):
        self.app = app
        self.cubes = []
        self.skybox = None
        self.heightmap = None
        self.load()
    
    def load(self):
        app = self.app
        # You are welcome to add/remove cubes from the scene
        cube_positions = [
            glm.vec3(0.0, 0.0, 0.0),
            glm.vec3(-1.5, -2.2, -2.5),
            glm.vec3(2.4, -0.4, -3.5),
            glm.vec3(1.3, -2.0, -2.5),
            glm.vec3(1.5, 2.0, -2.5),
            glm.vec3(1.5, 0.2, -1.5),
            glm.vec3(-1.3, 1.0, -1.5)
        ]
        self.cubes = [Cube(app, position=pos) for pos in cube_positions]
        self.skybox = Skybox(app)
        self.heightmap = Heightmap(app)
       
    def update(self):
        for cube in self.cubes:
            cube.update()
        self.skybox.update()
             
    def render(self):
        for obj in self.cubes:
            obj.render()
        self.skybox.render()
        # You will also need to render the heightmap here
         