const production = !process.env.ROLLUP_WATCH;
module.exports = {
  future: {
    purgeLayersByDefault: true,
    removeDeprecatedGapUtilities: true,
  },
  theme: {
    fontFamily: {
      title: ["Truculenta"],
      content: ["Calibri"]
    },
    extend: {}
  },
  plugins: [

  ],
  purge: {
    content: [
     "./src/**/*.svelte",

    ],
    enabled: production // disable purge in dev
  },
};

// module.exports = {
//   content: ['./src/**/*.{html,js,svelte,ts}'],
//   theme: {
//     fontFamily: {
//       title: ["Truculenta"],
//       content: ["Calibri"]
//     },
//     extend: {}
//   },
//   plugins: []
// };
