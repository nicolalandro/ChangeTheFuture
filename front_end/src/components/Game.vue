<template>
    <div>
        <p>text</p>
        <p>{{ msg }}</p>
    </div>
</template>

<script>
    export default {
        name: 'Game',
        props: {
            msg: String
        }
    }
</script>

