<template>
    <div id="app">
        <b-navbar class="is-info navbar-custom">
            <template slot="brand">
                <b-navbar-item href="/">
                    <b-icon icon="timelapse" size="is-medium"></b-icon>
                    <h1 style="margin-left: 10px">Change The Future</h1>
                </b-navbar-item>
            </template>
            <template slot="start">
                <b-navbar-item @click="status='game'">
                    My Games
                </b-navbar-item>
                <b-navbar-item @click="status='new'">
                    New
                </b-navbar-item>
            </template>
        </b-navbar>
        <GameList v-if="status == 'new'"></GameList>
        <Game v-if="status == 'game'" msg="test"></Game>
    </div>
</template>

<script>
    import Vue from 'vue'
    import Buefy from 'buefy'
    import 'buefy/dist/buefy.css'

    Vue.use(Buefy)

    import Game from './components/Game.vue'
    import GameList from './components/GameList.vue'


    export default {
        name: 'app',
        components: {
            Game, GameList
        },
        data() {
            return {
                status: 'new'
            }
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
        /*margin-top: 60px;*/
    }
</style>
