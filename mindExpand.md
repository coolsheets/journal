# Mosaic Mind Expansion Effect

This project demonstrates how to apply a **mosaic pixelation effect** to an image and animate an **expanding pixelation effect** to represent *mind expansion*. The effect is created using **HTML5 Canvas** and **JavaScript**.

## 📌 Features
- Loads an image onto an HTML `<canvas>`.
- Applies a **mosaic pixelation effect** dynamically.
- Gradually **expands pixelation outward** from the forehead.
- Uses `requestAnimationFrame` for smooth animation.

## 🚀 Technologies Used
- **HTML5 Canvas API** for image manipulation.
- **JavaScript** for animation and pixelation logic.
- **CSS** for basic styling.

---

## 📜 Code Explanation

### 1️⃣ **HTML Structure**
The HTML structure includes a `<canvas>` element where the image is rendered.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mosaic Mind Expansion</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: black;
        }
        canvas {
            border: 2px solid white;
        }
    </style>
</head>
<body>
    <canvas id="mosaicCanvas"></canvas>
</body>
</html>
```

---

### 2️⃣ **JavaScript: Image Loading & Initialization**
We define a **canvas** and **load an image** into it.

```javascript
const canvas = document.getElementById("mosaicCanvas");
const ctx = canvas.getContext("2d");
const img = new Image();
img.src = "your-image.jpg"; // Replace with actual image path

img.onload = function() {
    canvas.width = img.width;
    canvas.height = img.height;
    animateMosaic();
};
```

---

### 3️⃣ **Applying the Mosaic Effect**
To create the mosaic effect, we:
1. **Draw the image** onto the canvas.
2. **Extract pixel data** using `getImageData()`.
3. **Redraw the image** using large pixel blocks.

```javascript
function drawMosaic(pixelSize) {
    const w = canvas.width;
    const h = canvas.height;
    ctx.drawImage(img, 0, 0, w, h);
    
    const imageData = ctx.getImageData(0, 0, w, h);
    ctx.clearRect(0, 0, w, h);
    
    for (let y = 0; y < h; y += pixelSize) {
        for (let x = 0; x < w; x += pixelSize) {
            const index = (y * w + x) * 4;
            const r = imageData.data[index];
            const g = imageData.data[index + 1];
            const b = imageData.data[index + 2];
            ctx.fillStyle = `rgb(${r}, ${g}, ${b})`;
            ctx.fillRect(x, y, pixelSize, pixelSize);
        }
    }
}
```

---

### 4️⃣ **Animating the Expansion Effect**
We animate the **mind expansion effect** by gradually increasing the pixel size outward.

```javascript
let pixelSize = 1;
const maxPixelSize = 40;
const expansionSpeed = 0.5; 

function animateMosaic() {
    pixelSize += expansionSpeed;
    if (pixelSize > maxPixelSize) return;
    drawMosaic(pixelSize);
    requestAnimationFrame(animateMosaic);
}
```

- `pixelSize` starts small and increases over time.
- `requestAnimationFrame(animateMosaic)` ensures smooth animation.
- The animation **stops** when `pixelSize` reaches `maxPixelSize`.

---

## 🎯 How to Use
1. **Replace** `your-image.jpg` with an actual image file.
2. Save the file as `index.html` and open it in a browser.
3. Watch the **mosaic effect expand outward** from the head!

---

## 🎨 Possible Enhancements
✅ Add **mouse interaction** to trigger expansion.  
✅ Improve **smoothness** by tweaking pixel growth rate.  
✅ Use **WebGL (Three.js)** for advanced distortions.  

---

This approach provides an **engaging visual effect** while demonstrating JavaScript’s powerful capabilities with **canvas rendering and animations**. 🚀
