<template>
    <section>
        <div>
            <div class="notification" style="margin-bottom: 5px">
                Your Game
                <span @click="yourGameIsActive=!yourGameIsActive">
                    <b-icon
                            class="is-pulled-right"
                            :icon="!yourGameIsActive ? 'menu-down' : 'menu-up'"
                            size="is-medium">
                    </b-icon>
                </span>
            </div>
            <b-collapse :open="yourGameIsActive">
                <div class="panel-tabs" @click="$emit('go-to-game')">
                    <b-icon
                            icon="checkbox-blank-circle"
                            style="color: green"
                            size="is-small">
                    </b-icon>
                    Game 1
                </div>
            </b-collapse>
        </div>
        <div>
            <div class="notification" style="margin-bottom: 5px">
                Other Game
                <span @click="otherGameIsActive=!otherGameIsActive">
                    <b-icon
                            class="is-pulled-right"
                            :icon="!otherGameIsActive ? 'menu-down' : 'menu-up'"
                            size="is-medium">
                    </b-icon>
                </span>
            </div>
            <b-collapse :open="otherGameIsActive">
                <div class="panel-tabs" @click="$emit('go-to-game')">
                    <b-icon
                            icon="checkbox-blank-circle"
                            style="color: orange"
                            size="is-small">
                    </b-icon>
                    Game 2
                </div>
            </b-collapse>
        </div>
    </section>
</template>

<script>
    export default {
        name: 'GameList',
        data() {
            return {
                yourGameIsActive: true,
                otherGameIsActive: true
            }
        }
    }
</script>

<style>
    div.panel-tabs:hover {
        background-color: gray;
    }
</style>