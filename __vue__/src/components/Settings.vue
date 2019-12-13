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
                    <b-form-checkbox v-if="input.type == 'checkbox'" v-model="input.value"></b-form-checkbox>
                    <datetime v-if="input.type != 'checkbox'" type="datetime" v-model="input.value" format="yyyy-MM-dd HH:mm:ss"></datetime>
                </b-col>
            </b-row>
            <b-button variant="outline-primary" v-on:click="sendData">change</b-button>
        </b-container>

    </div>
</template>

<script>
    import { Datetime } from 'vue-datetime';
    // You need a specific loader for CSS files
    import 'vue-datetime/dist/vue-datetime.css'

    export default {
        template: '...',
        components: {
            datetime: Datetime
        },
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
                ]
            }
        },

        methods:{
            sendData: function () {
                this.$emit('inputs', this.inputs);
                // eslint-disable-next-line no-console
                console.log(this.inputs)
            }
        }
    }
</script>

<style scoped>

</style>