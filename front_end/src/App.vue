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
                <b-navbar-item @click="status='mygames'">
                    My Games
                </b-navbar-item>
                <b-navbar-item @click="status='new'">
                    New
                </b-navbar-item>
            </template>
        </b-navbar>
        <MyGameList v-if="status == 'mygames'" @go-to-game="status='game'"></MyGameList>
        <GameList v-if="status == 'new'" @error="addErrorMessage"></GameList>
        <Game v-if="status == 'game'"></Game>
        <section id="error-message-area">
            <b-notification
                    v-for="m in notificationMessages"
                    :key="m.message"
                    :type="m.type"
                    aria-close-label="Close notification"
                    role="alert"
                    style="margin-bottom: 5px">
                {{ m.message }}
            </b-notification>
        </section>
    </div>
</template>

<script>
    import Vue from 'vue'
    import Buefy from 'buefy'
    import 'buefy/dist/buefy.css'

    Vue.use(Buefy)

    import Game from './components/Game.vue'
    import GameList from './components/GameList.vue'
    import MyGameList from './components/MyGameList.vue'


    export default {
        name: 'app',
        components: {
            Game, GameList, MyGameList
        },
        data() {
            return {
                status: 'mygames',
                notificationMessages: []
            }
        },
        methods: {
            addErrorMessage(type, message) {
                this.notificationMessages.push({
                    type: type,
                    message: message
                })
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

    #error-message-area {
        position: fixed;
        bottom: 5px;
        right: 5px;
    }
</style>
