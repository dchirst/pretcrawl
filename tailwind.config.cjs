const config = {
  content: ["./src/**/*.{html,js,svelte,ts}"],

  theme: {

    extend: {},
  },

  plugins: [require("daisyui")],
      daisyui: {
      themes: [
        {
          mytheme: {
           "primary": "rgb(132, 24, 43)",
           "secondary": "#b91c1c",
           "accent": "#fca5a5",
           "neutral": "#242B38",
           "base-100": "#FCFCFD",
           "info": "#7BA4EA",
           "success": "#19C867",
           "warning": "#D9B517",
           "error": "#EE494F",
          },
        },
      ],
    },
};

module.exports = config;
