<template>
    <div class="bg-gradient-to-b from-black via-[#200D42] via-34% via-[#4F21A1] via-65% to-[#A46EDB] to-82% text-white py-[72px] flex-grow min-h-full">
        <div class="container">
            <div class="flex flex-col justify-center min-h-full">
                <h1 class="text-7xl font-bold tracking-tighter text-center mt-8">StegSafe</h1>
                <div class="py-8 text-wrap">
                    <p class="text-center text-xl mt-8 text-wrap">
                        Whether you want to embed text into an image for discreet sharing<br> or extract hidden information from an image, our app makes it simple and easy.<br> 
                        Protect your privacy with the power of steganography!
                    </p>
                    <div class="flex justify-center mt-8">
                        <router-link to="/hide-text">
                            <button class="bg-white text-black py-3 px-5 rounded-lg font-medium">Get Started</button>
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>

export default {
    name: "HeroSection",
};
</script>