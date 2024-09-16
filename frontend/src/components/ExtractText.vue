<template>
    <div>
        <h2>Extract Text from Image</h2>
        <form @submit.prevent="extractText">
            <div>
                <label for="image">Choose an Image:</label>
                <input type="file" @change="handleImageUpload" required />
            </div>
            <div>
                <label for="length">Length of Hidden Text:</label>
                <input type="number" v-model="textLength" required />
            </div>
            <button type="submit">Extract Text</button>
        </form>

        <!-- Display the extracted text -->
        <div v-if="extractedText">
            <h3>Extracted Text:</h3>
            <p>{{ extractedText }}</p>
        </div>

        <!-- Display error messages if any -->
        <div v-if="errorMessage" class="error">
            <p>{{ errorMessage }}</p>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
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

            const formData = new FormData();
            formData.append("image", this.image);
            formData.append("length", this.textLength);

            try {
                const response = await axios.post("http://localhost:3000/extract_text", formData);
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
