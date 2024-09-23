/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './public/**/*.html', './src/**/*.{vue,js,ts,jsx,tsx}',
    'node_modules/flowbite-vue/**/*.{js,jsx,ts,tsx,vue}',
    'node_modules/flowbite/**/*.{js,jsx,ts,tsx}',
  ],
  theme: {
    screens: {
      sm: "375px",
      md: "768px",
      lg: "1200px",
    },
    container: {
      center: true,
      padding: {
        DEFAULT: "1rem",
        md: "2rem",
      },
    },
    extend: {
      fontFamily: {
        sans: 'var(--font-sans)',
        serif: 'var(--font-serif)',
      },
      backgroundImage: {
        'grainImage':'url("/src/assets/grain.jpg")',
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
};

