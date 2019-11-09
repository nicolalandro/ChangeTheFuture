module.exports = {
    publicPath: process.env.NODE_ENV === 'production'
        ? '/static/'
        : '/',
    devServer: {
        proxy: {
            '/api/': {
                target: 'http://192.168.1.60:8000/',
            }
        }
    }
}