/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // main files
    "./templates/**/*.{html,css,js}",
    "./static/**/*.{html,css,js}",
    // home app
    "./home/templates/**/*.{html,css,js}",
    "./home/static/**/*.{html,css,js}",
    // admin app
    "./admin/templates/**/*.{html,css,js}",
    "./admin/static/**/*.{html,css,js}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
