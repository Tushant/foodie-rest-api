const path = require("path");
if(!process.env.NODE_ENV) {
    process.env.NODE_ENV = 'development';
}

module.exports = {
  entry: [
    './src/index.js'
  ],
  output: {
    path: path.join("../app/static/build/", "js"),
    filename: "app.js",
    publicPath: "../app/static/build/"
  },
  devtoo: 'source-map',
  debug: true,
  module: {
    loaders: [{
      exclude: /node_modules/,
      loader: 'babel',
      query: {
        presets: ['react', 'es2015', 'stage-1']
      }
    },
    {test: /\.(jpe?g|png|gif|svg)$/i, loader: "url-loader?name=images/[name].[ext]"},
    ]
  },
  resolve: {
    extensions: ['', '.js', '.jsx']
  },
  devServer: {
    historyApiFallback: true,
    contentBase: './'
  }
};
