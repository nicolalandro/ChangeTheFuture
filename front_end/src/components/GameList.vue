<template>
    <section>
        <div v-for="story in stories" :key="story.id">
            <div class="notification" style="margin-bottom: 5px">
                {{ story.title }}
                <span @click="visible=! (story.id === visible) ? story.id : ''">
                    <b-icon
                            class="is-pulled-right"
                            :icon="! (story.id === visible) ? 'menu-down' : 'menu-up'"
                            size="is-medium">
                    </b-icon>
                </span>

                <b-dropdown aria-role="list" class="is-pulled-right">
                    <b-icon icon="dots-vertical" slot="trigger" size="is-medium"></b-icon>
                    <b-dropdown-item aria-role="listitem">Create Game</b-dropdown-item>
                </b-dropdown>
            </div>
            <b-collapse
                    :open.sync="story.id === visible"
                    :key="story.id">
                <div :key="fragment.id" v-for="fragment in story.fragments" class="panel-tabs">
                    {{ fragment.location }} {{ fragment.date }}
                </div>
            </b-collapse>
        </div>
    </section>
</template>

<script>
    import axios from '../axios.js'

    export default {
        name: 'GameList',
        data() {
            return {
                stories: [],
                visible: ''
            }
        },
        created() {
            axios.post(
                '/api/',
                'query{stories{id,title,fragments{id,location,date}}}',
                {
                    headers: {
                        'Content-Type': 'application/graphql'
                    }
                }
            ).then((response) => {
                this.stories = response.data['data']['stories']
            }).catch((error) => {
                this.msg = 'Error: ' + error
            });
        }
    }
</script>
