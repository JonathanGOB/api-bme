<template>
    <div>
        <b-col style="margin-top: 25px">
            <strong>
                Settings
            </strong>
        </b-col>
        <b-container fluid>
            <b-row class="my-1" v-for="input in inputs" :key="input.key">
                <b-col sm="3">
                    <label :for="`type-${input.type}`">{{input.text}} <code></code>:</label>
                </b-col>
                <b-col sm="9">
                    <b-form-checkbox v-if="input.type == 'checkbox'" :value=input.text v-model="input.value"></b-form-checkbox>
                    <b-form-input v-if="input.type != 'checkbox'" v-model="input.value" :id="`type-${input.type}`" :type="input.type"></b-form-input>
                </b-col>
            </b-row>
            <b-button variant="outline-primary" v-on:click="sendData">change</b-button>
        </b-container>

    </div>
</template>

<script>
    export default {
        name: "Settings",
        data() {
            return {
                inputs:[
                    {text: 'live', type:'checkbox', key: '0', value:''},
                    {text: 'humidity', type: 'checkbox', key: '1', value:''},
                    {text: 'temperature', type: 'checkbox', key: '2', value:''},
                    {text: 'pressure', type: 'checkbox', key: '3', value:''},
                    {text: 'date from', type: 'date', key: '4', value:''},
                    {text: 'date to', type: 'date', key: '5', value:''},
                    {text: 'time from', type: 'time', key: '6', value:''},
                    {text: 'time to', type: 'time', key: '7', value:''},
                ]
            }
        },

        methods:{
            sendData: function () {
                this.$emit('inputs', this.inputs);
            }
        }
    }
</script>

<style scoped>

</style>