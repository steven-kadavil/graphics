import numpy as np
import glm

class BaseModel:
    """
    Base class for 3D models in the application.
    """

    def __init__(self, app, vao_name, tex_id):
        """
        Initialize the BaseModel.

        Args:
            app: The main application object.
            vao_name (str): Name of the Vertex Array Object.
            tex_id (str): Identifier for the texture.
        """
        self.app = app
        self.vao_name = vao_name
        self.tex_id = tex_id
        self.m_model = self.get_model_matrix()
        self.program = app.shader.programs[vao_name]
        self.camera = app.camera
        self.texture = app.texture.textures[self.tex_id]
        
    def update(self):
        """
        Update the model's shader uniforms.
        """
        self.texture.use()
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def get_model_matrix(self):
        """
        Get the model matrix for the object.

        Returns:
            numpy.ndarray: A 4x4 identity matrix.
        """
        return np.eye(4, dtype='f4')
    
    def render(self):
        """
        Render the model.
        """
        self.update()
        self.app.vao.render(self.vao_name)

class Cube(BaseModel):
    """
    Represents a cube object in the 3D scene.
    """

    def __init__(self, app, vao_name='cube', tex_id='container', position=glm.vec3(0.0)):
        """
        Initialize the Cube.

        Args:
            app: The main application object.
            vao_name (str): Name of the Vertex Array Object.
            tex_id (str): Identifier for the texture.
            position (glm.vec3): Initial position of the cube.
        """
        super().__init__(app, vao_name, tex_id)
        self.position = position
        self.program['texture1'] = 0
        self.program['texture2'] = 1
        self.program['m_proj'].write(self.camera.m_projection)
        self.texture2 = app.texture.textures['awesomeface']

    def update(self):
        """
        Update the cube's position, rotation, and scale.
        """
        self.texture.use(location=0)
        self.texture2.use(location=1)
        self.program['m_view'].write(self.camera.m_view)
        
        model = glm.mat4(1.0)
        model = glm.translate(model, self.position + self.app.cubeTranslation)
        model = glm.rotate(model, glm.radians(self.app.cubeRotValue.x), glm.vec3(1, 0, 0))
        model = glm.rotate(model, glm.radians(self.app.cubeRotValue.y), glm.vec3(0, 1, 0))
        model = glm.rotate(model, glm.radians(self.app.cubeRotValue.z), glm.vec3(0, 0, 1))
        model = glm.scale(model, self.app.cubeScale)
        
        self.m_model = model
        self.program['m_model'].write(self.m_model)
        
class Skybox(BaseModel):
    """
    Represents the skybox in the 3D scene.
    """

    def __init__(self, app, vao_name='skybox', tex_id='skybox'):
        """
        Initialize the Skybox.

        Args:
            app: The main application object.
            vao_name (str): Name of the Vertex Array Object.
            tex_id (str): Identifier for the texture.
        """
        super().__init__(app, vao_name, tex_id)
        self.program['u_texture_skybox'] = 0
        self.program['m_proj'].write(self.camera.m_projection)

    def update(self):
        """
        Update the skybox's view matrix, removing translation.
        """
        self.texture.use(location=0)
        view = glm.mat4(glm.mat3(self.camera.m_view))  # Remove translation from the view matrix
        self.program['m_view'].write(view)

class Heightmap(BaseModel):
    """
    Represents a heightmap in the 3D scene.
    """

    def __init__(self, app, vao_name='heightmap', tex_id='heightmap'):
        """
        Initialize the Heightmap.

        Args:
            app: The main application object.
            vao_name (str): Name of the Vertex Array Object.
            tex_id (str): Identifier for the texture.
        """
        super().__init__(app, vao_name, tex_id)
        self.program['u_texture_0'] = 0
        self.program['m_proj'].write(self.camera.m_projection)