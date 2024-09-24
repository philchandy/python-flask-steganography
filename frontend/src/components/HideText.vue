<template>
    <div class="container  text-white sm:min-w-full md:min-w-0">
        
        <div class="flex justify-center flex-col items-center mt-10  bg-white/90 border rounded-xl p-6 py-10 shadow-2xl sm:mt-20 ">
            <p className="uppercase font-semibold tracking-widest text-gray-800 bg-clip-text p-6 sm:p-3">
                Hide Text in Image
            </p>
            <p className="font-serif font-semibold bg-clip-text mb-4 sm:-mb-3 text-blue-500/70">
                Step {{ image ? '2' : '1' }} / 2
            </p>
            <div class="border border-gray-800 rounded sm:border-none p-6 flex items-center flex-wrap flex-col mb-2 sm:text-left sm:gap-2">
                <form @submit.prevent="hideTextInImage">
                    <div>
                        <label for="image" class="font-semibold mr-2 text-gray-800 mb-3 sm:p-2">Upload an Image: </label>
                        <input 
                            class="border border-gray-900 rounded-xl bg-gray-500 p-3 w-full" 
                            type="file" 
                            @change="handleImageUpload" 
                            accept="image/png, image/jpeg"
                            required />
                    </div>
                    <div v-if="image" class="flex flex-col mt-4" >
                        <label for="text" class=" text-left text-gray-800">Text to hide:</label>
                        <textarea v-model="textToHide" class="border  border-gray-900 text-black rounded-md mb-4 mt-2 p-2" required></textarea>

                        <button type="submit" class="mx-auto gap-2 border border-white/15 bg-gray-900 text-white h-12 px-6 rounded-xl" >Hide Text</button>
                    </div>
                    
                </form>
            </div>
            <div  v-if="imageData"  class="inline-flex items-center p-3">
                <a @click="downloadImage">
                    <button class="border border-white/15 bg-blue-900/80 text-white h-12 px-6 rounded-xl">Download Image</button>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios"

export default {
    data() {
        return {
            image:null,
            textToHide: '',
            successMessage: '',
            downloadUrl: '',
            filename: '',
            imageData: '',
        };
    },
    methods: {
        handleImageUpload(event) {
            this.image = event.target.files[0];
        },
        async hideTextInImage() {
            if (!this.image || !this.textToHide) {
                alert('Please upload an image and enter text.');
                return;
            }
            const formData = new FormData();
            formData.append('image', this.image);
            formData.append('text', this.textToHide);

            // I <3 Axios
            try {
                const response = await axios.post("/api/hide_text", formData);
                console.log("DATA:", response.data);
                
                if (response.data.filename && response.data.image) {
                    this.filename = response.data.filename;
                    this.imageData = response.data.image;
                } else {
                    console.error("Unexpected response format:", response.data);
                }
            } catch (error) {
                console.error("Error hiding text in image:", error);
            }
        },
        downloadImage() {
            if (!this.imageData) {
                alert('No image to download.');
                return;
            }
            
            // Convert the base64 string back into Blob
            const byteString = atob(this.imageData.split(',')[1]);
            const mimeString = this.imageData.split(',')[0].split(':')[1].split(';')[0];

            const ab = new ArrayBuffer(byteString.length);
            const ia = new Uint8Array(ab);
            for (let i = 0; i < byteString.length; i++) {
                ia[i] = byteString.charCodeAt(i);
            }

            const blob = new Blob([ab], { type: mimeString });

            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.setAttribute('download', 'output_image.png'); 

            document.body.appendChild(link);

            link.click();

            document.body.removeChild(link);
        },
    }
};
</script>