<template>
    <footer class="relative -z-1 overflow-x-clip bg-black">
      <div class="absolute bottom-0 left-1/2 -translate-x-1/2-z-10 text-white"></div>
      <div class="container">
        <div class="border-t border-white/15 py-6 text-sm flex flex-col md:flex-row md:justify-between items-center gap-8">
          <div class="text-white/40">&copy; 2024 Phillip Chandy. All rights reserved.</div>
          <nav class="flex flex-row items-center gap-8 md:flex-row">
            <a
              v-for="link in footerLinks"
              :key="link.title"
              :href="link.href"
              class="inline-flex items-center gap-1.5"
            >
              <img :src="link.img" :alt="link.title" class="size-6 invert-svg  " />
              <img src="@/assets/arrow-up-right.svg" class="size-4" alt="Back" />
            </a>
          </nav>
        </div>
      </div>
    </footer>
  </template>
  
  <script>
  import githubIcon from '@/assets/github.svg';
  import linkedinIcon from '@/assets/linkedin.svg';
  import websiteIcon from '@/assets/globe.svg';
  
  export default {
    name: 'FooterSection',
    components: {
      
    },
    data() {
      return {
        footerLinks: [
          { title: 'Github', href: 'https://github.com/philchandy', img:githubIcon },
          { title: 'Linkedin', href: 'https://www.linkedin.com/in/phillipchandy/', img:linkedinIcon },
          { title: 'Website', href: '#', img:websiteIcon },
        ]
      };
    }
  };
  </script>
  <style>
  /* Set the background color for the whole app */
  .invert-svg {
    filter:invert(100%)
  }
  
  </style>