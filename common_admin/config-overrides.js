const path = require('path');
const { override, addWebpackAlias, addLessLoader } = require("customize-cra");

module.exports = override(
  addWebpackAlias({
    "@": path.resolve(__dirname, 'src')
  }),
  addLessLoader({
    javascriptEnabled: true,
    localIdentName: '[local]--[hash:base64:5]'
  })
)