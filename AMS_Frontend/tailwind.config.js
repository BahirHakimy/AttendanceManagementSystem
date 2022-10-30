module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        darkShadeCyan: "#0891b2",
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
