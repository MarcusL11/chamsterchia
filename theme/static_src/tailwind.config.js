/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {},
        colors: {
            'white': '#ffffff',
            'orange': '#f7941c',
            'green': '#3aac57',
            'grey': '#333333',
            'teal': '#008080',
            'purple': '#6A0DAD',
        },
    },
    daisyui: {
        themes: [
            {
                cupcake: {
                    ...require("daisyui/src/theming/themes")["cupcake"],
                    ".theme-controller": {
                        position: "absolute",
                        opacity: 0,
                        width: "1px",
                        height: "1px",
                        overflow: "hidden",
                    },
                    ".dark-mode-switch": {
                        display: "flex",
                        alignItems: "center",
                    },
                    ".wallet-connnect-icon-path": {
                        fill: "#000",
                    },
                },
                sunset: {
                    ...require("daisyui/src/theming/themes")["sunset"],
                    ".theme-controller": {
                        position: "absolute",
                        opacity: 0,
                        width: "1px",
                        height: "1px",
                        overflow: "hidden",
                    },
                    ".dark-mode-switch": {
                        display: "flex",
                        alignItems: "center",                
                    },
                    ".wallet-connnect-icon-path": {
                        fill: "#A9C5DD",
                    },
                },
            }
        ],
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
        require("daisyui"),
    ],
}
