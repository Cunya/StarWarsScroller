let scene, camera, renderer;
let textMesh, scrollPlane;
const crawlSpeed = 0.04;

function init() {
    // Create scene
    scene = new THREE.Scene();

    // Create camera
    camera = new THREE.PerspectiveCamera(35, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 180;
    camera.position.y = 0;
    camera.rotation.x = -0.3;

    // Create renderer
    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // Create scroll plane
    const planeGeometry = new THREE.PlaneGeometry(150, 300);
    const planeMaterial = new THREE.MeshBasicMaterial({ 
        transparent: true, 
        opacity: 0,
        side: THREE.DoubleSide 
    });
    scrollPlane = new THREE.Mesh(planeGeometry, planeMaterial);
    scrollPlane.rotation.x = -Math.PI / 3.5;
    scrollPlane.position.z = 20;
    scene.add(scrollPlane);

    // Create text geometry
    const text = document.getElementById('crawl-text').innerText;
    const loader = new THREE.FontLoader();
    
    loader.load('https://threejs.org/examples/fonts/helvetiker_regular.typeface.json', function(font) {
        // Split text into lines and create a group
        const lines = text.split('\n');
        const textGroup = new THREE.Group();
        let yPosition = 0;
        const lineSpacing = 8;

        // Create each line separately
        lines.forEach(line => {
            if (line.trim() === '') {
                yPosition -= lineSpacing;
                return;
            }

            const lineGeometry = new THREE.TextGeometry(line.trim(), {
                font: font,
                size: 6,
                height: 0.8,
                curveSegments: 12,
                bevelEnabled: false
            });

            const material = new THREE.MeshBasicMaterial({ color: 0xFFE81F });
            const lineMesh = new THREE.Mesh(lineGeometry, material);
            
            // Center each line individually
            lineGeometry.computeBoundingBox();
            const lineWidth = lineGeometry.boundingBox.max.x - lineGeometry.boundingBox.min.x;
            lineMesh.position.x = -lineWidth / 2;
            lineMesh.position.y = yPosition;
            
            textGroup.add(lineMesh);
            yPosition -= lineSpacing;
        });

        // Use the group as the text mesh
        textMesh = textGroup;
        textMesh.position.y = -120;
        
        // Add text as a child of the scroll plane
        scrollPlane.add(textMesh);
    });

    // Add some stars to the background
    const starsGeometry = new THREE.BufferGeometry();
    const starPositions = [];
    
    for(let i = 0; i < 1000; i++) {
        const x = THREE.MathUtils.randFloatSpread(2000);
        const y = THREE.MathUtils.randFloatSpread(2000);
        const z = THREE.MathUtils.randFloatSpread(2000);
        starPositions.push(x, y, z);
    }
    
    starsGeometry.setAttribute('position', new THREE.Float32BufferAttribute(starPositions, 3));
    const starsMaterial = new THREE.PointsMaterial({ color: 0xFFFFFF, size: 1 });
    const starField = new THREE.Points(starsGeometry, starsMaterial);
    scene.add(starField);

    // Handle window resize
    window.addEventListener('resize', onWindowResize, false);
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

function animate() {
    requestAnimationFrame(animate);
    
    if (textMesh) {
        // Move the text upward within the fixed plane
        textMesh.position.y += crawlSpeed;
        
        // Reset position when text is too high
        if (textMesh.position.y > 180) {
            textMesh.position.y = -120;
        }
    }
    
    renderer.render(scene, camera);
}

// Start the animation
init();
animate();
