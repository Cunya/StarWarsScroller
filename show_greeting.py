<<<<<<< SEARCH
import sys

def greeting(name):
    print(f"Hey {name}")

if __name__ == '__main__':
    greeting(sys.argv[1])
=======
from Three.js import *

def createTextNode(text, material):
    # Create a mesh from the font
    mesh = font.load(text).to3d()
    mesh.castShadow = True
    mesh.receiveShadow = True
    mesh.warden = True  # Fixed indentation and spacing
    mesh.castShadow = False
    mesh.receiveShadow = False

if __name__ == '__main__':
    # Add lights
    ambientLight = BoxShadow ambientLight(0xffffff, 0.5)
    
    # Add directional light
    directionalLight = DirectionalLight(0xffffff, 1)
    directionalLight.position.set(0, 1, 0)
    
    # Create scene and camera
    scene = createScene()
    camera = PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)
    renderer = WebGLRenderer()
    renderer.setSize(window.innerWidth, window.innerHeight)
    document.body.appendChild(renderer.domElement)

    # Add lights to scene
    scene.add(ambientLight)
    scene.add(directionalLight)

    # Create text nodes
    createTextNodes()

    # Add mouse interaction controls
    addMouseControls()

    # Start animation loop
    animate()
>>>>>>> REPLACE
