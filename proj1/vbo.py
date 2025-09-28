import numpy as np
from PIL import Image

class VBO:
    def __init__(self, context, heightmap_path='Media/heightmaps/spiral.jpg'):
        self.context = context
        self.vbos = {}
        self.ebos = {}
        self.formats = {}
        self.attributes = {}
        self.heightmap_path = heightmap_path
        self.create_vbos()

    def create_vbos(self, heightmap_path='Media/heightmaps/spiral.jpg'):
        self.create_cube_vbo()
        self.create_skybox_vbo()
        self.create_heightmap_vbo(heightmap_path)
        
    def create_cube_vbo(self):
        vertices = np.array([
            # Front face
            -0.5, -0.5,  0.5,  0.0, 0.0,  # Bottom-left
            0.5, -0.5,  0.5,  1.0, 0.0,  # Bottom-right
            0.5,  0.5,  0.5,  1.0, 1.0,  # Top-right
            -0.5,  0.5,  0.5,  0.0, 1.0,  # Top-left
            # Back face
            -0.5, -0.5, -0.5,  1.0, 0.0,  # Bottom-right
            0.5, -0.5, -0.5,  0.0, 0.0,  # Bottom-left
            0.5,  0.5, -0.5,  0.0, 1.0,  # Top-left
            -0.5,  0.5, -0.5,  1.0, 1.0,  # Top-right
            # Top face
            -0.5,  0.5,  0.5,  0.0, 1.0,  # Front-left
            0.5,  0.5,  0.5,  1.0, 1.0,  # Front-right
            0.5,  0.5, -0.5,  1.0, 0.0,  # Back-right
            -0.5,  0.5, -0.5,  0.0, 0.0,  # Back-left
            # Bottom face
            -0.5, -0.5, -0.5,  0.0, 1.0,  # Back-left
            0.5, -0.5, -0.5,  1.0, 1.0,  # Back-right
            0.5, -0.5,  0.5,  1.0, 0.0,  # Front-right
            -0.5, -0.5,  0.5,  0.0, 0.0,  # Front-left
            # Right face
            0.5, -0.5,  0.5,  0.0, 0.0,  # Bottom-left
            0.5, -0.5, -0.5,  1.0, 0.0,  # Bottom-right
            0.5,  0.5, -0.5,  1.0, 1.0,  # Top-right
            0.5,  0.5,  0.5,  0.0, 1.0,  # Top-left
            # Left face
            -0.5, -0.5, -0.5,  0.0, 0.0,  # Bottom-left
            -0.5, -0.5,  0.5,  1.0, 0.0,  # Bottom-right
            -0.5,  0.5,  0.5,  1.0, 1.0,  # Top-right
            -0.5,  0.5, -0.5,  0.0, 1.0   # Top-left
        ], dtype='f4')

        indices = np.array([
            0,  1,  2,  2,  3,  0,  # Front face
            4,  5,  6,  6,  7,  4,  # Back face
            8,  9, 10, 10, 11,  8,  # Top face
            12, 13, 14, 14, 15, 12,  # Bottom face
            16, 17, 18, 18, 19, 16,  # Right face
            20, 21, 22, 22, 23, 20   # Left face
        ], dtype='u4')

        self.vbos['cube'] = self.context.buffer(vertices)
        self.ebos['cube'] = self.context.buffer(indices)
        self.formats['cube'] = '3f 2f'
        self.attributes['cube'] = ('in_position', 'in_texcoord_0')

    def create_skybox_vbo(self):
        '''
        TODO: You will need to update the skybox vbo such that it includes all the faces of the skybox.
        '''
        vertices = np.array([
            # x,     y,     z,     u,   v
            -0.5, -0.5,  0.5,  0.0, 0.0,  # Bottom-left
            0.5, -0.5,  0.5,  1.0, 0.0,  # Bottom-right
            0.5,  0.5,  0.5,  1.0, 1.0,  # Top-right
            -0.5,  0.5,  0.5,  0.0, 1.0,  # Top-left
        ], dtype='f4')
        
        indices = np.array([0, 1, 2, 2, 3, 0], dtype='u4')
        
        self.vbos['skybox'] = self.context.buffer(vertices)
        self.ebos['skybox'] = self.context.buffer(indices)
        
        self.formats['skybox'] = '3f 2f'
        self.attributes['skybox'] = ['in_position', 'in_texcoord']
           
    def create_heightmap_vbo(self, image_path):
        '''
        TODO: Implement the creation of the heightmap VBO and EBO, you will be calling other functions from this function.
        Note: You are welcome to add/remove parameters from this function. For example, you may want to add a parameter to 
        control the scale of the texture or offset.
        '''
        image = Image.open(image_path).convert('L')
        width, height = image.size
        pixel_data = np.array(image) / 255.0
        
        self.vbos['heightmap'] = ''
        self.ebos['heightmap'] = ''
        self.formats['heightmap'] = ''
        self.attributes['heightmap'] = ''
        return 
        

    def get_heightmap_vertices(self, pixel_data, width, height): # You are welcome to add/modify the parameters
        '''
        TODO
        '''
        pass

    def get_heightmap_indices(self, width, height): # You are welcome to add/modify the parameters
        '''
        TODO: Implement this function to generate the indices for the heightmap
        '''
        pass
        

    def destroy(self):
        for vbo in self.vbos.values():
            vbo.release()
        for ebo in self.ebos.values():
            ebo.release()
        
