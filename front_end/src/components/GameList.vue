<template>
    <section>
        <div v-for="story in stories" :key="story.id">
            <div class="notification" style="margin-bottom: 5px">
                {{ story.name }}
                <span @click="story.isActive=!story.isActive">
                    <b-icon
                            class="is-pulled-right"
                            :icon="!story.isActive ? 'menu-down' : 'menu-up'"
                            size="is-medium">
                    </b-icon>
                </span>

                <b-dropdown aria-role="list" class="is-pulled-right">
                    <b-icon icon="dots-vertical" slot="trigger" size="is-medium"></b-icon>
                    <b-dropdown-item aria-role="listitem">Create Game</b-dropdown-item>
                </b-dropdown>
            </div>
            <b-collapse
                    :open.sync="story.isActive"
                    :key="story.id">
                <div class="panel-tabs">Londra 2018</div>
                <div class="panel-tabs">Isole Caiman 2019</div>
                <div class="panel-tabs">Fiorena 2019</div>
            </b-collapse>
        </div>
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
