const restrictedGlobals = require('confusing-browser-globals');

const CI_environment = process.env.CI ? 0 : 1;
const commonTSAndVueConfig = {
  extends: ['plugin:@typescript-eslint/recommended-requiring-type-checking'],
  rules: {
    // TODO: Investigate why this rule reports false positives
    '@typescript-eslint/no-misused-promises': 'off'
  }
};

module.exports = {
  root: true,
  env: {
    node: true,
    browser: true
  },
  reportUnusedDisableDirectives: true,
  ignorePatterns: [
    'types/global/routes.d.ts',
    'types/global/components.d.ts',
    'dist',
    'node_modules'
  ],
  extends: [
    'eslint:recommended',
    'plugin:jsonc/recommended-with-json',
    'plugin:no-unsanitized/DOM',
    'plugin:optimize-regex/recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:promise/recommended',
    'plugin:import/recommended',
    'plugin:import/typescript',
    'plugin:vue/vue3-recommended',
    'plugin:sonarjs/recommended',
    'plugin:css/recommended',
    'plugin:unicorn/recommended',
    'plugin:vue-scoped-css/vue3-recommended'
  ],
  plugins: [
    'jsdoc',
    'jsonc',
    'no-unsanitized',
    'optimize-regex',
    'no-secrets',
    '@typescript-eslint',
    'promise',
    'import',
    'vue',
    'sonarjs',
    'css',
    'unicorn',
    'vue-scoped-css',
    'file-progress'
  ],
  rules: {
    'no-extend-native': 'error',
    'file-progress/activate': CI_environment,
    'semi': 'off',
    'capitalized-comments': 'error',
    'multiline-comment-style': 'error',
    '@typescript-eslint/semi': ['error', 'always'],
    'quotes': 'off',
    '@typescript-eslint/quotes': ['error', 'single', { 'avoidEscape': true }],
    'comma-dangle': 'error',
    'indent': 'off',
    '@typescript-eslint/indent': ['error', 2, {
      'SwitchCase': 1,
      'VariableDeclarator': 2,
      'CallExpression': { arguments: 'first' },
      'ArrayExpression': 'first',
      'ObjectExpression': 'first',
      'ImportDeclaration': 'first',
      flatTernaryExpressions: true,
      offsetTernaryExpressions: true
    }],
    'no-multi-spaces': ['error'],
    'block-spacing': 'off',
    '@typescript-eslint/block-spacing': ['error', 'always'],
    'linebreak-style': ['error', 'unix'],
    'brace-style': 'off',
    '@typescript-eslint/brace-style': ['error'],
    'unicode-bom': ['error', 'never'],
    'no-trailing-spaces': ['error'],
    'eol-last': ['error', 'always'],
    'no-restricted-globals': ['error', ...restrictedGlobals],
    'no-empty': ['error', { allowEmptyCatch: true }],
    'no-secrets/no-secrets': 'error',
    'import/newline-after-import': 'error',
    'import/order': 'error',
    'import/no-unresolved': ['error', { ignore: ['virtual:*', 'vue-router/auto/*'] }],
    'import/no-extraneous-dependencies': [
      'error',
      {
        devDependencies: ['vite.config.ts', 'scripts/**/*.ts'],
        optionalDependencies: false,
        peerDependencies: false,
        bundledDependencies: false
      }
    ],
    'import/no-nodejs-modules': 'error',
    'no-restricted-imports': 'off',
    '@typescript-eslint/no-restricted-imports': [
      'error',
      {
        patterns: [
          {
            group: ['*/plugins*'],
            message:
                            'Do not use Vue plugins directly. Use composables (from @/composables) instead.',
            allowTypeImports: true
          },
          {
            group: ['*/main*'],
            message:
                            'Do not use the Vue instance directly. Use composables (from @/composables) instead.',
            allowTypeImports: true
          }
        ]
      }
    ],
    'jsdoc/require-hyphen-before-param-description': 'error',
    'jsdoc/require-description': 'error',
    'jsdoc/no-types': 'error',
    'jsdoc/require-jsdoc': 'error',
    'jsdoc/informative-docs': 'error',
    'promise/no-nesting': 'error',
    'promise/no-return-in-finally': 'error',
    'promise/prefer-await-to-callbacks': 'error',
    'promise/prefer-await-to-then': 'error',
    '@typescript-eslint/ban-ts-comment': [
      'error',
      {
        'ts-expect-error': true,
        'ts-ignore': true,
        'ts-nocheck': true,
        'ts-check': true
      }
    ],
    '@typescript-eslint/explicit-function-return-type': 'error',
    '@typescript-eslint/prefer-ts-expect-error': 'error',
    '@typescript-eslint/explicit-member-accessibility': 'error',
    'prefer-arrow-callback': 'error',
    'padding-line-between-statements': [
      'error',
      // Always require blank lines after directives (like 'use-strict'), except between directives
      { blankLine: 'always', prev: 'directive', next: '*' },
      { blankLine: 'any', prev: 'directive', next: 'directive' },
      // Always require blank lines after import, except between imports
      { blankLine: 'always', prev: 'import', next: '*' },
      { blankLine: 'any', prev: 'import', next: 'import' },
      // Always require blank lines before and after every sequence of variable declarations and export
      {
        blankLine: 'always',
        prev: '*',
        next: ['const', 'let', 'var', 'export']
      },
      {
        blankLine: 'always',
        prev: ['const', 'let', 'var', 'export'],
        next: '*'
      },
      {
        blankLine: 'any',
        prev: ['const', 'let', 'var', 'export'],
        next: ['const', 'let', 'var', 'export']
      },
      // Always require blank lines before and after class declaration, if, do/while, switch, try
      {
        blankLine: 'always',
        prev: '*',
        next: ['if', 'class', 'for', 'do', 'while', 'switch', 'try']
      },
      {
        blankLine: 'always',
        prev: ['if', 'class', 'for', 'do', 'while', 'switch', 'try'],
        next: '*'
      },
      // Always require blank lines before return statements
      { blankLine: 'always', prev: '*', next: 'return' }
    ],
    'curly': ['error', 'all'],
    'unicorn/filename-case': 'off',
    'unicorn/consistent-function-scoping': 'off',
    'unicorn/prevent-abbreviations': 'off',
    'no-multiple-empty-lines': 'error',
    'vue/component-name-in-template-casing': [
      'error',
      'PascalCase',
      {
        registeredComponentsOnly: false
      }
    ],
    'vue/html-self-closing': [
      'error',
      {
        html: {
          void: 'always',
          normal: 'always'
        }
      }
    ],
    'vue/define-macros-order': ['error', {
      order: ['defineOptions', 'defineProps', 'defineEmits', 'defineSlots']
    }],
    'vue/html-closing-bracket-newline': ['error', { multiline: 'never' }],
    'vue/multiline-html-element-content-newline': 'error',
    'vue/multi-word-component-names': 'off',
    'vue/return-in-computed-property': 'off'
  },
  /**
   * Overrides allows us to omit the --ext CLI argument, simplifying package.json scripts section
   */
  overrides: [
    {
      files: ['*.md'],
      rules: {
        'no-trailing-spaces': ['off']
      }
    },
    {
      files: ['*.json'],
      parser: 'jsonc-eslint-parser',
      rules: {
        quotes: ['error', 'double'],
        semi: 'off'
      }
    },
    {
      files: ['*.ts', '*.tsx'],
      parser: 'typescript-eslint-parser-for-extra-files',
      parserOptions: {
        parser: '@typescript-eslint/parser',
        sourceType: 'module',
        project: 'tsconfig.json',
        extraFileExtensions: ['.vue']
      },
      ...commonTSAndVueConfig
    },
    {
      files: ['*.vue'],
      parser: 'vue-eslint-parser',
      parserOptions: {
        parser: 'typescript-eslint-parser-for-extra-files',
        project: 'tsconfig.json',
        sourceType: 'module',
        vueFeatures: {
          customMacros: ['defineModel']
        }
      },
      ...commonTSAndVueConfig
    },
    // TODO: Review once ESLint config is ESM
    {
      files: ['.eslintrc.cjs'],
      rules: {
        '@typescript-eslint/no-var-requires': 'off',
        'import/no-extraneous-dependencies': 'off',
        'unicorn/prefer-module': 'off',
        'no-undef': 'off'
      }
    },
    {
      files: ['vite.config.ts', 'scripts/**/*.ts'],
      rules: {
        'import/no-nodejs-modules': 'off'
      }
    },
    {
      files: ['*.js']
    },
    {
      files: ['*.d.ts'],
      rules: {
        'multiline-comment-style': 'off'
      }
    }
  ],
  settings: {
    'import/resolver': {
      typescript: true,
      node: true
    },
    progress: {
      hide: false,
      successMessage: 'Linting done!'
    }
  }
};
