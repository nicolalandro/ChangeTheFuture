<template>
    <section>
        <b-menu>
            <b-menu-list label="Menu">
                <b-menu-item v-for="story in stories"
                             @click="story.isActive=!story.isActive"
                             :expanded="story.isActive"
                             :key="story.id">
                    <template slot="label">
                        {{ story.name }}
                        <b-icon
                                class="is-pulled-right"
                                :icon="!story.isActive ? 'menu-down' : 'menu-up'">
                        </b-icon>
                    </template>
                    <b-menu-item label="Londra 2018"></b-menu-item>
                    <b-menu-item label="Isole Caiman 2019"></b-menu-item>
                    <b-menu-item label="Fiorena 2019"></b-menu-item>
                </b-menu-item>
            </b-menu-list>
        </b-menu>
    </section>
</template>

<script>
    export default {
        name: 'GameList',
        data() {
            return {
                stories: [
                    {isActive: false, name: 'Game 1', id: '123'},
                    {isActive: false, name: 'Game 2', id: '124'}
                ],
            }
        }
    }
</script>
