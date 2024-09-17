<template>
    <div class="">
        <div class="py-32 md:py-48 lg:py-60 overflow-x-clip ">
            <div class="container  bg-white/90 border rounded-xl p-6 py-10">
                <div class="">
                    <h1 class="font-serif text-black text-3xl md:text-5xl text-center mt-8 tracking-wide italic">StegoSafe</h1>
                    <p class="mt-4 text-center text-black/60 md:text-lg">Hide Secret text in Images.</p>
                </div>
                <div class="flex flex-col md:flex-row justify-center mt-8 gap-4 sm:px-16">
                    <button @click="() => { $emit('selectForm', 'hideText'); console.log('Hide button clicked'); }" class="inline-flex justify-center items-center gap-2 border-2 border-black/30 bg-white text-gray-900 h-12 px-6 rounded-xl">
                        <span class="font-semibold">Hide Text</span>
                    </button>
                    <button @click="() => { $emit('selectForm', 'extractText'); console.log('Extract button clicked'); }" class="inline-flex justify-center items-center gap-2 border-2 border-black/30 bg-white text-gray-900 h-12 px-6 rounded-xl">
                        <span class="font-semibold">Extract Text</span>
                    </button>
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