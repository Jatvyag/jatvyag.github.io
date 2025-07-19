module.exports = {
    root: true,
    env: {
        browser: true,
        es2021: true,
        node: true,
    },
    extends: [
        'plugin:vue/vue3-recommended',
        '@vue/eslint-config-standard',
    ],
    parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
    },
    rules: {
        'no-trailing-spaces': 'warn',
        'vue/multi-word-component-names': 'off',
        'no-console': 'warn',
        'no-debugger': 'warn',
        'vue/no-unused-vars': 'warn',
        'vue/script-setup-uses-vars': 'error',
    },
}

