const path = require('path');
const { override, addWebpackAlias, addLessLoader, fixBabelImports } = require("customize-cra");

module.exports = override(
  addWebpackAlias({
    "@": path.resolve(__dirname, 'src'),
    "@css": path.resolve(__dirname, 'src/assets/styles/css'),
    "@svg": path.resolve(__dirname, 'src/assets/image/svg'),
    "@utils": path.resolve(__dirname, 'src/utils')
  }),
  addLessLoader({
    javascriptEnabled: true,
    modifyVars: {
      '@primary-color': '#1DA57A' //注意这里
    },
    localIdentName: '[local]--[hash:base64:5]'
  }),
  //注意style选项是true，官方文档给出的style值是’css’，之所以写成true是因为antd源码中样式全部是使用less编写的，当style为true时引入的就是less源文件，而style为’css’的时候引入的是等效的css文件。虽然less文件的体积要比css小很多算是个优点，但其实体积大小不重要，因为最终less文件仍然会被less-loader编译成css，也就是说引入到index.html里面的就是编译出来的css。而我选择引入less而非css的原因是cra配置了对less的优化策略，比起我直接引入css要好一些。另外，安装less是不会增加打包后的体积的，因为less和sass都是开发环境的工具，它们只在打包过程中发挥作用。它们不会被打包到最终的输出目录中，大家放心大胆的装两个是完全OK的，我自己的项目是less和sass都安装了
  fixBabelImports('import', {
    libraryName: 'antd',
    libraryDirectory: 'es',
    style: true,
  })
)