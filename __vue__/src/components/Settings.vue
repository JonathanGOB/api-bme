<template>
    <div>
        <b-container fluid>
            <b-row>live: <b-form-checkbox value="live"></b-form-checkbox></b-row>
            <b-row class="my-1" v-for="input in inputs" :key="input.key">
                <b-col sm="3">
                    <label :for="`type-${input.type}`">{{input.text}} <code></code>:</label>
                </b-col>
                <b-col sm="9">
                    <b-form-input :id="`type-${input.type}`" :type="input.type"></b-form-input>
                </b-col>
            </b-row>
            <b-button variant="outline-primary">change</b-button>
        </b-container>

    </div>
</template>

<script>
    export default {
        name: "Settings",
        data() {
            return {
                inputs:[
                    {text: 'humidity', type: 'text', key: '1'},
                    {text: 'temperature', type: 'text', key: '2'},
                    {text: 'pressure', type: 'text', key: '3'},
                    {text: 'date from', type: 'date', key: '4'},
                    {text: 'date to', type: 'date', key: '5'},
                    {text: 'color', type: 'color', key: '6'}
                ]
            }
        }
    }
</script>

<style scoped>

</style>