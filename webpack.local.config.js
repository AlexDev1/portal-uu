const autoprefixer = require('autoprefixer');
const webpack = require('webpack');
const baseConfig = require('./webpack.base.config');
const SpritesmithPlugin = require('webpack-spritesmith');
const BundleTracker = require('webpack-bundle-tracker');
const path = require('path');
const nodeModulesDir = path.resolve(__dirname, 'node_modules');

baseConfig[0].mode = 'development'
baseConfig[1].mode = 'development'

baseConfig[1].entry = [
  'webpack-dev-server/client?http://localhost:3000',
  'webpack/hot/only-dev-server',
  'whatwg-fetch',
  '@babel/polyfill',
  './assets/js/index',
]

baseConfig[0].output['publicPath'] = 'http://localhost:3000/assets/bundles/';
baseConfig[1].output = {
  path: path.resolve('./assets/bundles/'),
  publicPath: 'http://localhost:3000/assets/bundles/',
  filename: '[name].js',
}

baseConfig[1].module.rules.push({
  test: /\.jsx?$/,
  exclude: [nodeModulesDir],
  loader: require.resolve('babel-loader')
},
{
  test: /\.(woff(2)?|eot|ttf)(\?v=\d+\.\d+\.\d+)?$/,
  loader: 'url-loader?limit=100000',
});

baseConfig[1].plugins = [
  new webpack.HotModuleReplacementPlugin(),
  new webpack.NamedModulesPlugin(),
  new webpack.NoEmitOnErrorsPlugin(),  // don't reload if there is an error
  new SpritesmithPlugin({
      src: {
        cwd: path.resolve(__dirname, 'assets/images/png/'),
        glob: '*.png',
      },
      target: {
        image: path.resolve(__dirname, 'assets/images/spritesmith-generated/sprite.png'),
        css: path.resolve(__dirname, 'assets/sass/vendor/spritesmith.scss'),
      },
      retina: '@2x',
     logCreatedFiles: true,
  }),
  new BundleTracker({
    filename: './webpack-stats.json',
  }),
  new webpack.LoaderOptionsPlugin({
    options: {
      context: __dirname,
      postcss: [
        autoprefixer,
      ]
    }
  }),
  new webpack.ProvidePlugin({
    $: "jquery",
    jQuery: "jquery",
    "window.jQuery": "jquery",
    Tether: "tether",
    "window.Tether": "tether",
    Popper: ['popper.js', 'default'],
    Alert: "exports-loader?Alert!bootstrap/js/dist/alert",
    Button: "exports-loader?Button!bootstrap/js/dist/button",
    Carousel: "exports-loader?Carousel!bootstrap/js/dist/carousel",
    Collapse: "exports-loader?Collapse!bootstrap/js/dist/collapse",
    Dropdown: "exports-loader?Dropdown!bootstrap/js/dist/dropdown",
    Modal: "exports-loader?Modal!bootstrap/js/dist/modal",
    Popover: "exports-loader?Popover!bootstrap/js/dist/popover",
    Scrollspy: "exports-loader?Scrollspy!bootstrap/js/dist/scrollspy",
    Tab: "exports-loader?Tab!bootstrap/js/dist/tab",
    Tooltip: "exports-loader?Tooltip!bootstrap/js/dist/tooltip",
    Util: "exports-loader?Util!bootstrap/js/dist/util",
  })
]

module.exports = baseConfig;
