// postcss.config.js
module.exports = {
    plugins: [
      // Use Tailwind CSS with the custom configuration file
      require('tailwindcss')('./tailwind.config.js'),
      // Add Autoprefixer to add vendor prefixes for CSS compatibility
      require('autoprefixer')
    ]
  }
  