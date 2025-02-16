import { Router } from 'itty-router';
import { parseFITS } from 'fitsjs';

const router = Router();

router.post('/upload', async (request) => {
    try {
        const formData = await request.formData();
        const fitsFile = formData.get('fits_file');

        if (!fitsFile) {
            return new Response('No FITS file uploaded.', { status: 400 });
        }

        const arrayBuffer = await fitsFile.arrayBuffer();
        const fitsData = parseFITS(new Uint8Array(arrayBuffer));

        return new Response(JSON.stringify(fitsData), {
            headers: { 'Content-Type': 'application/json' }
        });
    } catch (error) {
        return new Response(`Error processing FITS file: ${error}`, { status: 500 });
    }
});

export default {
    fetch: router.handle
};
