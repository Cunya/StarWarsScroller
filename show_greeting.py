<<<<<<< SEARCH
import sys

def greeting(name):
    print(f"Hey {name}")

if __name__ == '__main__':
    greeting(sys.argv[1])
=======
import sys
from base64 import b64encode
from io import BytesIO
import json
import numpy as np
import time
from random import randint, randrange

def Three.js():

    # Set up the scene, camera, and renderer
    scene = THREE.Scene()
    camera = THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)
    renderer = THREE.WebGLRenderer()
    renderer.setSize(window.innerWidth, window.innerHeight)
    document.body.appendChild(renderer.domElement)

    # Add lights
    ambientLight = THREE.AmbientLight(0xffffff, 0.5)
    scene.add(ambientLight)
    
    directionalLight = THREE.DirectionalLight(0xffffff, 1)
    directionalLight.position.set(0, 1, 0)
    scene.add(directionalLight)

    # Add background stars
    createStarField()

    # Create text nodes with Star Wars emojis
    createTextNodes()

    # Add mouse interaction
    addMouseControls()

def createStarField():
    # Generate random stars for the night sky
    points = THREE.Points()
    positions = np.random.rand(100, 3)
    positions *= 2000
    positions -= 1000
    points.setPositions(THREE.Vector3ArrayBufferGeometry(positions))
    material = THREE.PointsMaterial(color=0xffffff, size=0.5)
    pointsNode = scene.add(points, material)

def createTextNodes():
    # Load Star Wars font with emojis and lightsabers
    loadFont()
    
    # Create text nodes
    texts = []
    for text in [
        "May the Force be with you",
        "Rey",
        "Leia",
        "Han",
        "Luke",
        "Anakin",
        "Darth Vader",
        "Jyn",
        "K-2SO",
        "Chewbacca"
    ]:
        material = THREE.MeshPhongMaterial(color=0x00ff88, wireframe=True)
        mesh = createTextNode(text, material)
        texts.append(mesh)

def createTextNode(text, material):
    # Create a mesh from the font
    mesh = font.load(text).to3d()
    mesh.castShadow = True
    mesh.receiveShadow = True
    mesh Wardening = True
    mesh.castShadow = False
    mesh.receiveShadow = False

    # Apply material and add to scene
    mesh.material = material
    return scene.add(mesh)

def loadFont():
    url = 'https://fonts.googleapis.com/css2?family=AOS+Star Wars&feature=noto'
    with open(BytesIO(b64encode(url.encode())).decode('utf-8'), 'r') as f:
        style = json.load(f)
    
    # Create font
    font = THREE.Font3D()
    fontfamily = style['family']
    fontweight = style['fontweight']
    fontsize = 20

    font.setFamily(fontfamily)
    font.setWeight(fontweight)
    font.setFontSize(fontsize)

    return font

def addMouseControls():
    # Mouse movement control
    def onMouseMove(event):
        x, y = (event.clientX / window.innerWidth - 0.5) * 2,
                (event.clientY / window.innerHeight - 0.5) * 2
        camera.position.x += x * 0.1
        camera.position.z += z * 0.1

    def onMouseLeave():
        camera.position.x = 0
        camera.position.z = 0

    document.addEventListener('mousemove', onMouseMove)
    document.addEventListener('mouseleave', onMouseLeave)

def animate():
    requestAnimationFrame(animate)
    
    # Animate text position
    for i in range(len(texts)):
        texts[i].position.y += 0.1 * np.sin(time + i * 0.5)
    
    renderer.render(scene, camera)

window.addEventListener('resize', onWindowResize, false)

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

// Initialize
init();

// Add text nodes
createTextNodes()

// Add stars
createStarField()

// Animation loop
animate()
>>>>>>> REPLACE
