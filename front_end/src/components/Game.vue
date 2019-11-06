<template>
    <section class="game">
        <b-steps has-navigation='true'>
            <b-step-item label="Londra 2018"
                         clickable=true
                         type="is-success"
                         icon="ray-start-arrow">
                <h1 class="title has-text-centered">Londra 2018</h1>
                <b-button class="is-primary">Rivela</b-button>
                <br>
                <br>
                <b-button type="is-link">Rivela Indizio</b-button>
            </b-step-item>
            <b-step-item
                    label="Isole Caiman 2019"
                    clickable=ture
                    type="is-dark"
                    icon="ray-vertex">
                <h1 class="title has-text-centered">Isole Caiman 2019</h1>
                Lorem ipsum dolor sit amet.
            </b-step-item>
            <b-step-item
                    label="Fiorenza 2019"
                    clickable=ture
                    type="is-danger"
                    icon="ray-end-arrow">
                <h1 class="title has-text-centered">Isole Caiman 2019</h1>
                Lorem ipsum dolor sit amet.
            </b-step-item>
        </b-steps>
    </section>
</template>

<script>
    export default {
        name: 'Game',
    }
</script>

<style>
    .step-navigation {
        position: absolute;
        margin-left: auto;
        margin-right: auto;
        left: 0;
        right: 0;
        top: 70px;
    }

    .game {
        margin-top: 60px;
    }
</style>

