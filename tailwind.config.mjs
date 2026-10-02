/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        deyami: {
          950: '#0a0a0a',
          900: '#121212',
          800: '#1f1f1f',
          700: '#333333',
          500: '#666666',
          400: '#8c8c8c',
          300: '#b8b8b8',
          200: '#d9d9d9',
          100: '#ececec',
          50: '#f8f8f8',
          silver: '#C0C8D0',
          'silver-light': '#E8EDF2',
          'silver-dark': '#8A95A0',
        },
      },
      fontFamily: {
        sans: ['Jost', 'Outfit', 'Montserrat', 'system-ui', 'sans-serif'],
        script: ['"Dancing Script"', 'cursive'],
      },
      letterSpacing: {
        widest: '0.25em',
        ultra: '0.35em',
      },
      boxShadow: {
        subtle: '0 4px 20px -2px rgba(0, 0, 0, 0.05)',
        card: '0 10px 30px -4px rgba(0, 0, 0, 0.08)',
        modal: '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-out forwards',
        'sparkle-pulse': 'sparklePulse 2s ease-in-out infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(8px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        sparklePulse: {
          '0%, 100%': { transform: 'scale(1)', opacity: '0.8' },
          '50%': { transform: 'scale(1.15)', opacity: '1' },
        },
      },
    },
  },
  plugins: [],
};
