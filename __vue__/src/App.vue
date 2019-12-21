<template>
    <div id="app">
        <div class="d-flex flex-column-reverse align-items-center">
            <h1 class="display-1"> Graph </h1>
        </div>
        <div class="row-2">
            <GraphMenu ref="Graphman"/>
        </div>
    </div>
</template>

<script>
    import GraphMenu from "./components/GraphMenu";

    export default {
        name: 'app',
        components: {
            GraphMenu,
        },
    }
</script>

<style>

</style>
