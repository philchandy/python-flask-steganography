<template>
    <div>
        <h2>Hide Text in Image</h2>
        <form @submit.prevent="hideTextInImage">
            <div>
                <label for="image">Choose an Image</label>
                <input type="file" @change="handleImageUpload" required />
            </div>
            <div>
                <label for="text">Text to hide:</label>
                <textarea v-model="textToHide" required></textarea>
            </div>
            <button type="submit">Hide Text</button>
        </form>
        <a v-if="imageData" :href="'data:image/png;base64,' + imageData" download="output_image.png">
            <button>Download Image</button>
        </a>
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
                const response = await axios.post("http://localhost:3000/hide_text", formData);
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
        }
    }
};
</script>