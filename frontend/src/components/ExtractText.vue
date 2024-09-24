<template>
    <div class="container sm:min-w-full md:min-w-0">
        
        <div class="flex justify-center flex-col items-center mt-10  bg-white/90 border rounded-xl p-6 py-10 shadow-2xl sm:mt-20 ">
            <p className="uppercase font-semibold tracking-widest text-gray-800 bg-clip-text p-6 sm:p-3">
                Extract Text from Image
            </p>
            <p className="font-serif font-semibold bg-clip-text mb-4 sm:-mb-3 text-blue-500/70">
                Step {{ image ? '2' : '1' }} / 2
            </p>
            <div class="border border-gray-800 rounded sm:border-none p-6 flex items-center flex-wrap flex-col mb-2 sm:text-left sm:gap-2">
                <form @submit.prevent="extractText">
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
                        <label for="text" class=" text-left text-gray-800">Length of Hidden Text:</label>
                        <input type="number" v-model="textLength" required class="border border-gray-900 text-black rounded-md mb-4 mt-2 p-2" />
                        <button type="submit" class="mx-auto gap-2 border border-white/15 bg-gray-900 text-white h-12 px-6 rounded-xl" >Extract Text</button>
                    </div>
                    
                </form>
            </div>
            
            <AppAccordian v-if="extractedText">
                <template v-slot:title>
                    <span class=" text-black font-semibold border-b-2 border-gray-900">Extracted Text</span>
                </template>
                <template v-slot:content>
                    <p class="text-black p-4">{{ extractedText }}</p>
                </template>
            </AppAccordian>
            <div  v-if="errorMessage"  class="inline-flex items-center p-3">
                <h3 class="text-black italic">Error: </h3>
                <p class="text-black italic">{{ errorMessage }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import AppAccordian from "./AppAccordian.vue";


export default {
    components: {
        AppAccordian
    },
    data() {
        return {
            image: null,
            textLength: 0,
            extractedText: '',
            errorMessage: ''  // Added errorMessage for handling errors
        };
    },
    methods: {
        handleImageUpload(event) {
            this.image = event.target.files[0];
        },
        async extractText() {
            // Reset errorMessage and extractedText
            this.errorMessage = '';
            this.extractedText = '';

            if (!this.image || this.textLength <= 0) {
                this.errorMessage = 'Please upload an image and enter a valid length.';
                return;
            }
            const allowedTypes = ['image/png', 'image/jpeg'];
            if (!allowedTypes.includes(this.image.type)) {
                alert('Please upload a valid image file (PNG or JPEG).');
                return;
            }

            const formData = new FormData();
            formData.append("image", this.image);
            formData.append("length", this.textLength);

            try {
                const response = await axios.post("/api/extract_text", formData);
                console.log("DATA:", response.data);
                if (response.data.text) {
                    this.extractedText = response.data.text;
                } else {
                    this.errorMessage = 'No text extracted or unexpected response format.';
                }
            } catch (error) {
                console.error("Error extracting text from image:", error);
                this.errorMessage = 'Error extracting text. Please try again.';
            }
        }
    }
};
</script>

<style scoped>
    .error {
        color: red;
        font-weight: bold;
    }
</style>
