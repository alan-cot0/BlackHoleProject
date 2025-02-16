const express = require('express');
const multer = require('multer');
const fs = require('fs');
const path = require('path');
const { Canvas } = require('canvas');
const { fits } = require('fitsjs');

const app = express();
const port = 5000;

// Set up file upload
const upload = multer({ dest: 'uploads/' });

app.use(express.static('public'));

// Endpoint to handle the file upload and FITS file processing
app.post('/upload', upload.single('fits_file'), async (req, res) => {
    try {
        const fitsFilePath = req.file.path;
        const redshift = parseFloat(req.body.redshift);

        const data = await readFitsFile(fitsFilePath);
        const plotPath = generatePlot(data, redshift);

        res.send(plotPath);  // Send the plot image URL
    } catch (error) {
        console.error(error);
        res.status(500).send('Error processing the FITS file.');
    }
});

// Function to read the FITS file using fitsjs
const fs = require('fs');
const FITS = require('fitsjs');

async function readFitsFile(filePath) {
    try {
        const fileBuffer = fs.readFileSync(filePath); // Read FITS file as a buffer
        const fits = new FITS(fileBuffer); // Load FITS file
        const hdus = fits.getHDU(); // Get Header Data Units

        if (!hdus || hdus.length === 0) {
            throw new Error("No HDUs found in FITS file.");
        }

        console.log("FITS file successfully read:", hdus);
        return hdus;
    } catch (error) {
        console.error("Error reading FITS file:", error.message);
        return null;
    }
}


// Function to generate the plot using Canvas
function generatePlot(data, redshift) {
    const wavelength = data['wave'];  // Assuming 'wave' is the column name
    const flux = data['flux'];  // Assuming 'flux' is the column name

    // Convert to rest-frame wavelength
    const lambdaRest = wavelength / (1 + redshift);

    // Create canvas for the plot
    const canvas = new Canvas(800, 600);
    const ctx = canvas.getContext('2d');

    // Plot the data (simple line chart)
    ctx.beginPath();
    ctx.moveTo(lambdaRest[0], flux[0]);

    for (let i = 1; i < lambdaRest.length; i++) {
        ctx.lineTo(lambdaRest[i], flux[i]);
    }

    ctx.strokeStyle = 'blue';
    ctx.stroke();

    // Save the plot as an image
    const plotPath = 'public/spectrum_plot.png';
    const out = fs.createWriteStream(plotPath);
    const stream = canvas.createPNGStream();
    stream.pipe(out);

    return plotPath;
}

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
