module.exports = {
  multipass: true,
  js2svg: {
    indent: 2,
    pretty: true,
  },
  plugins: [
    'preset-default',
    'prefixIds',
    'sortAttrs',
    'removeStyleElement',
    'removeScriptElement',
  ],
};
