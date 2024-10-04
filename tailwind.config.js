/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      "./app/templates/**/*.html",
      "./static/js/**/*.js",
      './static/**/*.js', 
      './static/**/*.css',
      './app/**/*.py'
      // Add other paths to scan for Tailwind classes
    ],
    theme: {
      extend: {
        colors: {
          lilac: '#D9B2E5', // Example lilac color
        },
      },
    },
    plugins: [],
  }
  