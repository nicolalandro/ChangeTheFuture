<template>
    <div id="app">
        <Game msg="test"></Game>
    </div>
</template>

<script>
    import Vue from 'vue'
    import Buefy from 'buefy'
    import 'buefy/dist/buefy.css'

    Vue.use(Buefy)


    // import HelloWorld from './components/HelloWorld.vue'
    import Game from './components/Game.vue'

    export default {
        name: 'app',
        components: {
           Game
        }
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
